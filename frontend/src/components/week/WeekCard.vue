<script setup>
import CreateAgendaDialog from "components/event/CreateAgendaDialog.vue";
import EventTable from "components/EventTable.vue";
import { api } from "boot/axios";
import { defineComponent, ref, watch } from "vue";
import { useQuasar } from "quasar";

defineComponent({ name: "WeekCard" });

const props = defineProps({ weekId: Number, weekObj: Object });

const { notify } = useQuasar();

const events = ref([]);

watch(
	() => props.weekId,
	(val) => {
		api
			.get("calgen/events/", { params: { weekId: val } })
			.then((resp) => {
				events.value = resp.data;
			})
			.catch((err) => {
				console.log(err);
				notify({
					message:
						"An error occurred while fetching week data. ERROR: " + err.response.data.message,
					color: "negative",
				});
			});
	},
	{ immediate: true } // To get events on page load
);

function handlePushEvent(input) {
	api.post("calgen/events/", input).then((resp) => {
		events.value.push(resp.data);
	});
}

function handleEventUpdate(eventItem) {
	const eventIndexToUpdate = events.value.findIndex((v) => v.id === eventItem.id);
	events.value[eventIndexToUpdate] = { ...eventItem };
}

function handleEventDelete($event) {
	events.value = events.value.filter((v) => v.id !== $event.id);
}

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
		<q-card-section v-if="weekObj">
			<h4 class="text-h4 q-my-md">Schichtplan (KW {{ weekObj.number }})</h4>
			<div class="text-subtitle1">{{ weekObj.start }} - {{ weekObj.end }}</div>
			<p>
				Alle Schichtpläne sind in der folgenden Tabelle aufgeführt. Um einen neuen Schichtplan
				hinzuzufügen, nutzen Sie bitte das obenstehende Formular. Wenn Sie einen Plan löschen
				möchten, klicken Sie einfach auf das Mülleimersymbol auf der rechten Seite eines
				Schichteintrags.
			</p>
			<CreateAgendaDialog :weekId="weekId" @pushEvent="handlePushEvent" />
		</q-card-section>
		<event-table
			:events="events"
			@deleteEvent="handleEventDelete($event)"
			@updateEvent="handleEventUpdate"
		/>
		<div class="q-my-md flex flex-center">
			<q-btn :disable="!events.length > 0" color="primary" @click="handleEventFeedDownload"
				>Download Calendar ( .ics)
			</q-btn>
		</div>
	</q-card>
</template>
