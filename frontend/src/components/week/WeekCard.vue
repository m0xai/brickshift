<script setup>
import CreateAgendaDialog from "components/event/CreateAgendaDialog.vue";
import EventTable from "components/EventTable.vue";
import { api } from "boot/axios";
import { defineComponent, onMounted, ref } from "vue";

defineComponent({ name: "WeekCard" });

const props = defineProps({ weekId: Number });

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
	api
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

<template>
	<q-card>
		<q-card-section>
			<h4 class="text-h4 q-my-md">Schichtplan</h4>
			<div class="text-subtitle1">09.11 - 15.11</div>
			<p>
				Alle Schichtpläne sind in der folgenden Tabelle aufgeführt. Um einen neuen Schichtplan
				hinzuzufügen, nutzen Sie bitte das obenstehende Formular. Wenn Sie einen Plan löschen
				möchten, klicken Sie einfach auf das Mülleimersymbol auf der rechten Seite eines
				Schichteintrags.
			</p>
			<CreateAgendaDialog />
		</q-card-section>
		<event-table
			:events="events"
			@deleteEvent="handleEventDelete($event)"
			@updateEvent="handleEventUpdate"
		/>
		<div class="q-my-md flex flex-center">
			<q-btn :disable="false" color="primary" @click="handleEventFeedDownload"
				>Download Calendar ( .ics)
			</q-btn>
		</div>
	</q-card>
</template>

<style scoped></style>
