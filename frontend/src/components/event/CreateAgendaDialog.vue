<script setup>
import { ref } from "vue";
import CreateAgendaDialogForm from "components/event/CreateAgendaDialogForm.vue";
import CreateAgendaDialogUpload from "components/event/CreateAgendaDialogUpload.vue";

defineOptions({ name: "CreateAgendaDialog" });

const props = defineProps({
	weekId: Number,
});

const emit = defineEmits(["pushEvent"]);

const persistent = ref(false);

const tab = ref("upload");

function handleEventCreate($event) {
	console.log("E: ", $event);
}
</script>

<template>
	<div class="flex justify-end">
		<q-btn color="primary" label="Upload / Insert" @click="persistent = true" />
	</div>

	<q-dialog v-model="persistent" persistent transition-hide="scale" transition-show="scale">
		<q-card style="min-width: 600px">
			<q-card-section class="row items-center">
				<div class="text-h6">Upload Agenda / Create Event</div>
				<q-space />
				<q-btn v-close-popup dense flat icon="close" round />
			</q-card-section>

			<q-card-section class="q-pt-none">
				<q-tabs v-model="tab" align="justify" class="text-primary" dense narrow-indicator>
					<q-tab :ripple="false" icon="cloud_upload" label="Upload" name="upload" />
					<q-tab :ripple="false" icon="view_agenda" label="Form" name="form" />
				</q-tabs>
				<q-tab-panels v-model="tab" animated>
					<q-tab-panel name="upload">
						<CreateAgendaDialogUpload />
					</q-tab-panel>

					<q-tab-panel name="form">
						<CreateAgendaDialogForm :weekId="weekId" @pushEvent="emit('pushEvent', $event)" />
					</q-tab-panel>
				</q-tab-panels>
			</q-card-section>
		</q-card>
	</q-dialog>
</template>
