<script setup>
import { defineComponent } from "vue";
import WeekCard from "components/week/WeekCard.vue";
import { useRoute } from "vue-router";

defineComponent({ name: "WeekPage" });

const route = useRoute();
</script>

<template>
	<WeekCard :weekId="Number(route.params.id)" />
</template>

<style scoped></style>
