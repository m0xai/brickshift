<script setup>
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "stores/auth";

defineComponent({name: "LogoutBtn"})

const router = useRouter()
const authStore = useAuthStore()
function handleLogout() {
  router.push("/#/login")
  authStore.setToken("")
}
</script>

<template>
  <q-btn flat @click="handleLogout()">Logout</q-btn>
</template>
