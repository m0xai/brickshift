<script setup>
import { defineProps, ref } from "vue";
import * as EventValidator from "src/services/validators/event-validator";
import { QForm, useQuasar } from "quasar";
import { api } from "boot/axios";

defineOptions({ name: "EventEdit" });
const emit = defineEmits(["updateEvent"]);
const props = defineProps({ eventItem: {} });

const $q = useQuasar();

const qform = ref(null);
const isDialogOpen = ref(false);

const editFormFields = ref({
	id: 0,
	name: "",
	description: "",
	date: new Date(),
	start: "00:00:00",
	end: "00:00:00",
});

function setFieldValues() {
	editFormFields.value.id = props.eventItem.id;
	editFormFields.value.name = props.eventItem.name;
	editFormFields.value.description = props.eventItem.description;
	editFormFields.value.date = props.eventItem.date;
	editFormFields.value.start = props.eventItem.start;
	editFormFields.value.end = props.eventItem.end;
}

function resetForm() {
	editFormFields.value.id = 0;
	editFormFields.value.name = "";
	editFormFields.value.description = "";
	editFormFields.value.date = new Date();
	editFormFields.value.start = "00:00:00";
	editFormFields.value.end = "00:00";
}

async function handleEventUpdate() {
	const isValid = await qform.value?.validate();
	if (isValid) {
		api
			.put("calgen/events/" + editFormFields.value.id + "/", { ...editFormFields.value })
			.then((response) => {
				emit("updateEvent", editFormFields.value);
				$q.notify({
					message: "Schicht successfully updated.",
					position: "top-right",
					color: "positive",
				});
				isDialogOpen.value = false;
			})
			.catch((err) => {
				$q.notify({
					message: "Task update failed: " + err.message,
					position: "top-right",
					color: "negative",
				});
			});
	} else {
		$q.notify({
			message: "Task update failed: Please ensure that all fields contain valid information.",
			position: "top-right",
			color: "negative",
		});
	}
}
</script>

<template>
	<q-btn fab-mini flat icon="edit" @click="isDialogOpen = true" />

	<q-dialog
		v-model="isDialogOpen"
		persistent
		transition-hide="scale"
		transition-show="scale"
		@hide="resetForm()"
		@show="setFieldValues()"
	>
		<q-card class="text-white" style="width: 500px">
			<q-card-section class="bg-primary flex">
				<div class="text-h6">Edit Schicht fuer {{ props.eventItem.name }}</div>
				<q-space />
				<q-btn v-close-popup dense flat icon="close" round />
			</q-card-section>

			<q-card-section>
				<q-form ref="qform">
					<q-input v-model="editFormFields.name" class="q-mb-md" filled label="Name" />
					<q-input
						v-model="editFormFields.description"
						class="q-mb-md"
						filled
						label="Description"
						type="textarea"
					/>
					<q-input
						v-model="editFormFields.date"
						:rules="[EventValidator.requiredRule, EventValidator.dayRule]"
						filled
						mask="####-##-##"
					>
						<template v-slot:append>
							<q-icon class="cursor-pointer" name="event">
								<q-popup-proxy cover transition-hide="scale" transition-show="scale">
									<q-date v-model="editFormFields.date">
										<div class="row items-center justify-end">
											<q-btn v-close-popup color="primary" flat label="Close" />
										</div>
									</q-date>
								</q-popup-proxy>
							</q-icon>
						</template>
					</q-input>

					<q-input
						v-model="editFormFields.start"
						:rules="[EventValidator.requiredRule, EventValidator.timeRule]"
						filled
						mask="time"
					>
						<template v-slot:append>
							<q-icon class="cursor-pointer" name="access_time">
								<q-popup-proxy cover transition-hide="scale" transition-show="scale">
									<q-time v-model="editFormFields.start" format24h>
										<div class="row items-center justify-end">
											<q-btn v-close-popup color="primary" flat label="Close" />
										</div>
									</q-time>
								</q-popup-proxy>
							</q-icon>
						</template>
					</q-input>

					<q-input
						v-model="editFormFields.end"
						:rules="[EventValidator.requiredRule, EventValidator.timeRule]"
						filled
						mask="time"
					>
						<template v-slot:append>
							<q-icon class="cursor-pointer" name="access_time">
								<q-popup-proxy cover transition-hide="scale" transition-show="scale">
									<q-time v-model="editFormFields.end" format24h>
										<div class="row items-center justify-end">
											<q-btn v-close-popup color="primary" flat label="Close" />
										</div>
									</q-time>
								</q-popup-proxy>
							</q-icon>
						</template>
					</q-input>
				</q-form>
			</q-card-section>

			<q-card-actions class="flex justify-between q-mx-sm">
				<q-btn v-close-popup class="" color="primary" flat label="Cancel" />
				<q-btn class="text-primary" color="primary" label="Save" @click="handleEventUpdate()" />
			</q-card-actions>
		</q-card>
	</q-dialog>
</template>
