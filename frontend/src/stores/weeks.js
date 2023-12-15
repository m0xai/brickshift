import { defineStore } from "pinia";
import { ref } from "vue";

export const useWeeksStore = defineStore(
	"weeks",
	() => {
		const weeks = ref([]);

		async function setWeeks(weekList) {
			weeks.value = await weekList;
		}

		function getWeeks() {
			return weeks.value;
		}

		return { setWeeks, getWeeks, weeks };
	},
	{ persist: true }
);
