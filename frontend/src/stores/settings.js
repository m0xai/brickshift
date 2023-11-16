import { defineStore } from "pinia";
import { ref } from "vue";

export const useSettingsStore = defineStore(
	"settings",
	() => {
		const isDark = ref(false);

		function toggle() {
			isDark.value = !isDark.value;
		}

		return { isDark, toggle };
	},
	{
		persist: true,
	}
);
