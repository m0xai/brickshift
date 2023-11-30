<script setup>
import { ref } from "vue";
import CreateAgendaDialogForm from "components/event/CreateAgendaDialogForm.vue";
import CreateAgendaDialogUpload from "components/event/CreateAgendaDialogUpload.vue";

defineOptions({ name: "CreateAgendaDialog" });

const persistent = ref(false);

const tab = ref("upload");
</script>

<template>
	<div class="flex justify-end">
		<q-btn label="Upload / Insert" color="primary" @click="persistent = true" />
	</div>

	<q-dialog v-model="persistent" persistent transition-show="scale" transition-hide="scale">
		<q-card style="min-width: 600px">
			<q-card-section class="row items-center">
				<div class="text-h6">Upload Agenda / Create Event</div>
				<q-space />
				<q-btn icon="close" flat round dense v-close-popup />
			</q-card-section>

			<q-card-section class="q-pt-none">
				<q-tabs v-model="tab" narrow-indicator dense align="justify" class="text-primary">
					<q-tab :ripple="false" name="upload" icon="cloud_upload" label="Upload" />
					<q-tab :ripple="false" name="form" icon="view_agenda" label="Form" />
				</q-tabs>
				<q-tab-panels v-model="tab" animated>
					<q-tab-panel name="upload">
						<CreateAgendaDialogUpload />
					</q-tab-panel>

					<q-tab-panel name="form">
						<CreateAgendaDialogForm />
					</q-tab-panel>
				</q-tab-panels>
			</q-card-section>
		</q-card>
	</q-dialog>
</template>
