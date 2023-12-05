<script setup>
import { api } from "src/boot/axios";
import EventEdit from "components/event/EventEdit.vue";
import { lightFormat } from "date-fns";

const columns = [
	{ name: "details", label: "Details", align: "center" },
	{
		name: "name",
		label: "Name",
		required: false,
		field: "name",
		align: "left",
	},
	{ name: "date", label: "Date", field: "date", align: "center" },
	{ name: "start", label: "Start", field: "start", align: "center" },
	{ name: "end", label: "End", field: "end", align: "center" },
	{ name: "actions", label: "Action(s)", align: "center" },
];

defineProps({
	events: {
		type: Array,
		required: true,
	},
});

const emit = defineEmits(["deleteEvent", "updateEvent"]);

function handleEventDelete(event) {
	api.delete("calgen/events/" + event.id + "/").then((resp) => {
		emit("deleteEvent", event);
	});
}

function handleEventUpdate(eventItem) {
	// Just forward updated event to parent
	emit("updateEvent", eventItem);
}
</script>

<template>
	<div class="q-pa-md">
		<q-table :columns="columns" :rows="events" row-key="name" title="Schicht">
			<template v-slot:body="props">
				<q-tr :props="props">
					<q-td key="details" auto-width>
						<q-btn
							:icon="props.expand ? 'remove' : 'add'"
							color="accent"
							dense
							round
							size="sm"
							@click="props.expand = !props.expand"
						/>
					</q-td>
					<q-td key="name" :props="props">
						{{ props.row.name }}
					</q-td>
					<q-td key="date" :props="props">
						{{ lightFormat(new Date(props.row.date), "dd-MM-yyyy") }}
					</q-td>
					<q-td key="start" :props="props">
						{{ props.row.start }}
					</q-td>
					<q-td key="end" :props="props">
						{{ props.row.end }}
					</q-td>
					<q-td key="actions" :props="props">
						<EventEdit :event-item="props.row" @updateEvent="handleEventUpdate" />
						<q-btn fab-mini flat icon="delete" @click="handleEventDelete(props.row)"></q-btn>
					</q-td>
				</q-tr>
				<q-tr v-show="props.expand" :props="props">
					<q-td v-if="!props.row.description" colspan="100%">
						<div class="text-center">No description provided.</div>
					</q-td>
					<q-td v-else colspan="100%">
						<div class="text-left">{{ props.row.description }}</div>
					</q-td>
				</q-tr>
			</template>
		</q-table>
	</div>
</template>
