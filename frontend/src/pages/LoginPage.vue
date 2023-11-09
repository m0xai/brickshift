<script setup>
import { defineComponent, ref } from "vue";
import axios from "axios";
import { useAuthStore } from "../stores/auth";

defineComponent({name: "LoginPage"})
const username = ref("")
const password = ref("")

const authStore = useAuthStore();

// Add logic to implement user's login
function submitLogin() {
  if(username.value && password.value) {
    axios.post("http://127.0.0.1:8000/api/login/", {
      "username": username.value,
      "password": password.value
    }, {}).then((response) => {
      authStore.setToken(response.data.token)
    })
  }
}

</script>

<template>
  <q-layout view="lHh Lpr lFf">
    <div class="flex flex-center">
      <q-card class="login-wrapper">
        <h2 class="text-h2">Login</h2>
        <q-card-section>
          <q-form>
            <q-input v-model="username" label="Username" class="q-my-md" />
            <q-input v-model="password" label="Password" class="q-my-md" />
          </q-form>
          <a href="#" class="q-my-md" >Password Vergessen?</a>
          <q-card-actions class="q-my-lg">
            <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
            <q-btn label="Submit" type="submit" color="primary" @click="submitLogin"/>
          </q-card-actions>
        </q-card-section>
      </q-card>
    </div>
  </q-layout>
</template>

<style scoped>
.login-wrapper {
  width: 100%;
  max-width: 400px;
}
</style>
