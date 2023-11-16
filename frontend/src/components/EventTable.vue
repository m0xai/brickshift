<script setup>
import { api } from "src/boot/axios";
import EventEdit from "components/event/EventEdit.vue";

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

function handleEventUpdate(id, eventItem) {
	// Just forward updated event to parent
	emit("updateEvent", id, eventItem);
}
</script>

<template>
	<div>
		<q-card>
			<q-card-section>
				<h4 class="text-h4">Schichtplan</h4>
				<p>
					All shift schedules are displayed in the table below. To add a new shift schedule, please
					utilize the form above. If you wish to delete a schedule, simply click on the trash icon
					located on the right side of a shift entry.
				</p>
			</q-card-section>
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
							<q-td
								v-for="col in props.cols.filter(
									(v) => v.name !== 'details' && v.name !== 'actions'
								)"
								:key="col.name"
								:props="props"
							>
								{{ col.value }}
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
		</q-card>
	</div>
</template>
