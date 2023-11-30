<script setup>
import { ref } from "vue";
import * as EventValidator from "src/services/validators/event-validator";

function handleCreateEvent() {
	// Emit values to parent
	const event = {
		name: name.value,
		date: date.value,
		start: start.value,
		end: end.value,
	};
	emit("pushEvent", event);
}

const name = ref("");
const date = ref("2023-11-03");
const start = ref("10:00");
const end = ref("11:00");

const emit = defineEmits(["pushEvent"]);
</script>

<template>
	<q-form class="flex column" @submit="handleCreateEvent">
		<q-input
			v-model="name"
			:rules="[(val) => !!val || 'Field is required']"
			filled
			label="Employee Name"
		/>
		<q-input
			v-model="date"
			:rules="[EventValidator.requiredRule, EventValidator.dayRule]"
			filled
			label="Date"
		>
			<template v-slot:append>
				<q-icon class="cursor-pointer" name="event">
					<q-popup-proxy cover transition-hide="scale" transition-show="scale">
						<q-date v-model="date" first-day-of-week="1" mask="YYYY-MM-DD" today-btn>
							<div class="row items-center justify-end">
								<q-btn v-close-popup color="primary" flat label="Close" />
							</div>
						</q-date>
					</q-popup-proxy>
				</q-icon>
			</template>
		</q-input>

		<q-input
			v-model="start"
			:rules="[EventValidator.requiredRule, EventValidator.timeRule]"
			filled
			label="Start"
			mask="time"
		>
			<template v-slot:append>
				<q-icon class="cursor-pointer" name="access_time">
					<q-popup-proxy cover transition-hide="scale" transition-show="scale">
						<q-time v-model="start" format24h>
							<div class="row items-center justify-end">
								<q-btn v-close-popup color="primary" flat label="Close" />
							</div>
						</q-time>
					</q-popup-proxy>
				</q-icon>
			</template>
		</q-input>

		<q-input
			v-model="end"
			:rules="[EventValidator.requiredRule, EventValidator.timeRule]"
			filled
			label="End"
			mask="time"
		>
			<template v-slot:append>
				<q-icon class="cursor-pointer" name="access_time">
					<q-popup-proxy cover transition-hide="scale" transition-show="scale">
						<q-time v-model="end" format24h>
							<div class="row items-center justify-end">
								<q-btn v-close-popup color="primary" flat label="Close" />
							</div>
						</q-time>
					</q-popup-proxy>
				</q-icon>
			</template>
		</q-input>

		<div class="flex justify-end">
			<q-btn class="q-mr-md" flat label="Reset" type="reset" />
			<q-btn color="primary" icon="send" label="Send" type="submit" />
		</div>
	</q-form>
</template>
