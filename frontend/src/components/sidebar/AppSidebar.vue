<script setup>
import { ref, watch } from "vue";
import { useQuasar } from "quasar";
import { lightFormat, parseISO } from "date-fns";

defineOptions({ name: "AppSidebar" });
const props = defineProps({ weeks: Object });

const { notify } = useQuasar();

const today = new Date();
const selectedYear = ref(today.getFullYear());
const years = [2023, 2024, 2025, 2026];
const currentYearWeeks = ref([]);

watch(
	() => [selectedYear.value, props.weeks],
	() => {
		setCurrentYearWeeks(props.weeks);
	}
);

function setCurrentYearWeeks(weeksList) {
	if (weeksList.length === 0) {
		notify({
			message: "An error occurred while getting selected year's week list",
			color: "negative",
		});
	}
	currentYearWeeks.value = weeksList?.filter((v) => v.year === selectedYear.value);
}
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
		<q-item
			v-for="week in currentYearWeeks"
			:key="week.id"
			:to="{ name: 'week', params: { id: week.id } }"
			clickable
			tag="a"
		>
			<q-item-section>
				<q-item-label
					><span class="text-bold">KW {{ week.number }}:</span>
					{{ lightFormat(parseISO(week.start), "dd.MM") }} -
					{{ lightFormat(parseISO(week.end), "dd.MM") }}
				</q-item-label>
			</q-item-section>
		</q-item>
	</q-list>
</template>
