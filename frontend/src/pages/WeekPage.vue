<script setup>
import { defineComponent, onMounted } from "vue";
import WeekCard from "components/week/WeekCard.vue";
import { useRoute } from "vue-router";

defineComponent({ name: "WeekPage" });

const route = useRoute();

onMounted(() => {
	console.log(route.params);
});
</script>

<template>
	<WeekCard />
</template>

<style scoped></style>
