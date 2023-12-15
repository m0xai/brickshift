<script setup>
import { defineComponent, onMounted, ref } from "vue";
import WeekCard from "components/week/WeekCard.vue";
import { useRoute } from "vue-router";
import { api } from "boot/axios";

defineComponent({ name: "WeekPage" });

const route = useRoute();

const weekObj = ref(null);
const getWeek = api.get("calgen/weeks/" + route.params.id);
onMounted(() => {
	getWeek.then((resp) => {
		weekObj.value = resp.data;
	});
});
</script>

<template>
	<WeekCard :weekId="Number(route.params.id)" :weekObj="weekObj" />
</template>

<style scoped></style>
