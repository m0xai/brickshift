<template>
	<q-page class="flex flex-center column">
		<create-event-form :events="events" @pushEvent="handlePushEvent($event)" />
		<event-table
			:events="events"
			@deleteEvent="handleEventDelete($event)"
			@updateEvent="handleEventUpdate"
		/>
		<q-btn
			:disable="!events.length > 0"
			class="q-mt-md"
			color="primary"
			@click="handleEventFeedDownload"
			>Download Calendar ( .ics)
		</q-btn>
	</q-page>
</template>

<script setup>
import { defineComponent, onMounted, ref } from "vue";
import EventTable from "components/EventTable.vue";
import CreateEventForm from "components/CreateEventForm.vue";
import { api } from "src/boot/axios";

defineComponent({ name: "IndexPage" });

function handlePushEvent(input) {
	api.post("calgen/events/", input).then((resp) => {
		events.value.push(input);
	});
}

function handleEventUpdate(eventItem) {
	const eventIndexToUpdate = events.value.findIndex((v) => v.id === eventItem.id);
	events.value[eventIndexToUpdate] = { ...eventItem };
}

function handleEventDelete($event) {
	events.value = events.value.filter((v) => v.id !== $event.id);
}

const events = ref([]);

onMounted(() => {
	api.get("calgen/events/").then((resp) => {
		events.value = resp.data;
	});
});

function handleEventFeedDownload() {
	if (!events.value.length > 0) {
		return;
	}

	const method = "GET";
	const url = "http://localhost:8000/calgen/latest/feed.ics";
	const fileName = `feed_${new Date().toISOString()}.ics`;
	axios
		.request({
			url,
			method,
			responseType: "blob",
		})
		.then(({ data }) => {
			const downloadUrl = window.URL.createObjectURL(new Blob([data]));
			const link = document.createElement("a");
			link.href = downloadUrl;
			link.setAttribute("download", fileName);
			document.body.appendChild(link);
			link.click();
			link.remove();
		});
}
</script>
