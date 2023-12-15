<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useAuthStore } from "stores/auth";
import useRouter from "src/router";
import { api } from "src/boot/axios";
import LogoutBtn from "components/LogoutBtn.vue";
import { useQuasar } from "quasar";
import { useSettingsStore } from "stores/settings";
import AppSidebar from "components/sidebar/AppSidebar.vue";
import { useWeeksStore } from "stores/weeks";

const $q = useQuasar();
const router = useRouter();
const settingsStore = useSettingsStore();

const leftDrawerOpen = ref(false);

function toggleLeftDrawer() {
	leftDrawerOpen.value = !leftDrawerOpen.value;
}

api.interceptors.request.use((config) => {
	if (config.url.includes("login")) {
		return config;
	}
	const authStore = useAuthStore();
	config.headers.Authorization = "Token " + authStore.token;
	return config;
});

function toggleDarkMode() {
	settingsStore.toggle();
}

watch(
	() => settingsStore.isDark,
	() => {
		$q.dark.toggle();
	}
);

onMounted(() => {
	if (settingsStore.isDark) {
		$q.dark.set(true);
	}
});

const modeSwitchIcon = computed(() => {
	return $q.dark.isActive ? "light_mode" : "dark_mode";
});

const weekStore = useWeeksStore();
const weeks = ref([]);

async function getWeeks() {
	const response = await api.get("calgen/weeks/");

	if (response.status !== 200) {
		notify({ message: "An error occured while getting week data.", color: "negative" });
	}

	return response.data;
}

onMounted(() => {
	weekStore.setWeeks(getWeeks());
	weeks.value = weekStore.getWeeks();
});
</script>

<template>
	<q-layout view="lHh Lpr lFf">
		<q-header elevated>
			<q-toolbar>
				<q-btn aria-label="Menu" dense flat icon="menu" round @click="toggleLeftDrawer" />

				<q-toolbar-title> BrickShift</q-toolbar-title>

				<div>
					<LogoutBtn />
					<q-btn :icon="modeSwitchIcon" flat @click="toggleDarkMode()" />
				</div>
			</q-toolbar>
		</q-header>

		<q-drawer
			v-model="leftDrawerOpen"
			:width="200"
			bordered
			elevated
			persistent
			show-if-above
			side="left"
		>
			<AppSidebar :weeks="weeks" />
		</q-drawer>

		<q-page-container class="q-ma-lg flex flex-center">
			<router-view />
		</q-page-container>
	</q-layout>
</template>
