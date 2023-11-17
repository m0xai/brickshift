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
			})
			.catch((err) => {
				$q.notify({
					message: "Username or password incorrect",
					position: "top-right",
					color: "negative",
				});
			});
	}
}
</script>

<template>
	<q-layout view="lHh Lpr lFf">
		<div class="flex flex-center window-height">
			<q-card class="login-wrapper">
				<q-card-section>
					<h2 class="text-h2 q-mb-lg q-mt-md">Login</h2>
					<q-form>
						<q-input
							v-model="username"
							label="Username"
							:rules="[(val) => !!val || 'This field is required']"
							class="q-my-md"
						/>
						<q-input
							v-model="password"
							type="password"
							label="Password"
							:rules="[(val) => !!val || 'This field is required']"
							class="q-my-md"
						/>
					</q-form>
					<a href="#" class="q-my-md text-primary">Password Vergessen?</a>
					<q-card-actions class="q-my-lg">
						<q-btn
							label="Login"
							:disable="username.length == 0 || password.length == 0"
							type="submit"
							color="primary"
							class="full-width"
							@click="submitLogin"
						/>
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
