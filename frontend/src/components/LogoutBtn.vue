<script setup>
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "stores/auth";
import { useQuasar } from "quasar";

defineComponent({name: "LogoutBtn"})

const $q = useQuasar();

const router = useRouter()
const authStore = useAuthStore()
function handleLogout() {
  router.push("login")
  $q.notify({message: "You have successfully logged out", position: "top-right", color: "positive"})
  authStore.setToken("")
}
</script>

<template>
  <q-btn flat @click="handleLogout()">Logout</q-btn>
</template>
