<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
         BrickShift
        </q-toolbar-title>

        <div>
          <q-btn flat @click="handleLogout()">Logout</q-btn>
          Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Essential Links
        </q-item-label>
        <q-item
          clickable
          tag="a"
        >
          <q-item-section>
            <q-item-label>Home</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from "../stores/auth";

import * as userMixin from "../mixins/userMixin"
import router from 'src/router';
import { api } from 'src/boot/axios';


const leftDrawerOpen = ref(false)
function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
api.interceptors.request.use((config) => {
  if(config.url.includes("login")) {
   return config;
  }
  const authStore = useAuthStore();
  config.headers.Authorization = "Token " + authStore.token;
  return config
});

function handleLogout() {
  userMixin.logOut()
}

</script>
