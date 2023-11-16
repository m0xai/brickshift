<script setup>
import { defineComponent, ref } from "vue";
import { useAuthStore } from "stores/auth";
import { api } from "src/boot/axios";
import { useRouter } from "vue-router";
import { useQuasar } from "quasar";

defineComponent({ name: "LoginPage" });
const $q = useQuasar();
const router = useRouter();
const authStore = useAuthStore();

const username = ref("");
const password = ref("");

// Add logic to implement user's login
function submitLogin() {
	if (username.value && password.value) {
		api
			.post(
				"api/login/",
				{
					username: username.value,
					password: password.value,
				},
				{}
			)
			.then((response) => {
				authStore.setToken(response.data.token);
				router.push("/");
				$q.notify({
					message: "You have successfully logged in!",
					position: "top-right",
					color: "positive",
				});
			});
	}
}
</script>

<template>
  <q-layout view="lHh Lpr lFf">
    <div class="flex flex-center">
    <div class="flex flex-center window-height">
      <q-card class="login-wrapper">
        <h2 class="text-h2">Login</h2>
        <q-card-section>
          <q-form>
            <q-input v-model="username" label="Username" class="q-my-md" />
            <q-input v-model="password"  type="password" label="Password" class="q-my-md" />
          </q-form>
          <a href="#" class="q-my-md text-primary">Password Vergessen?</a>
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
  border: 1px solid var(--q-primary);
}
</style>
