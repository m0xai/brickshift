import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore(
	"auth",
	() => {
		const token = ref("");

		function setToken(input) {
			token.value = input;
		}

		return { token, setToken };
	},
	{
		persist: true,
	}
);
