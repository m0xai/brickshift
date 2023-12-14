<script setup>
import { onMounted, ref } from "vue";
import { api } from "boot/axios";
import { useQuasar } from "quasar";
import { lightFormat, parseISO } from "date-fns";

defineOptions({ name: "AppSidebar" });

const { notify } = useQuasar();

const today = new Date();
const selectedYear = ref(today.getFullYear());
const years = [2022, 2023, 2024, 2025];
const weeks = ref([]);

async function getWeeks() {
	const response = await api.get("calgen/weeks/");

	if (response.status !== 200) {
		notify({ message: "An error occured while getting week data.", color: "negative" });
	}

	weeks.value = response.data;
	return response.data;
}

onMounted(() => {
	getWeeks();
});
</script>

<template>
	<q-list>
		<q-select
			v-model="selectedYear"
			:options="years"
			item-aligned
			label="Year"
			standout="bg-teal text-white"
		/>
		<q-item-label header> Week List</q-item-label>
		<q-item v-for="week in weeks" :key="week.id" clickable tag="a">
			<q-item-section>
				<q-item-label
					><span class="text-bold">KW {{ week.number }}:</span>
					{{ lightFormat(parseISO(week.start), "dd-MM") }} -
					{{ lightFormat(parseISO(week.end), "dd-MM") }}
				</q-item-label>
			</q-item-section>
		</q-item>
	</q-list>
</template>
