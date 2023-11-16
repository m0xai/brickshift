<script setup>
import { ref } from "vue";
import * as EventValidator from "src/services/validators/event-validator";

defineProps({
  events: {
    type: Array,
    required: true
  }
})

function handleCreateEvent() {
  // Emit values to parent
  const event = {
    name: name.value,
    date: date.value,
    start: start.value,
    end: end.value
  }
  emit("pushEvent", event)
}

const name = ref("")
const date = ref("2023-11-03")
const start = ref('10:00')
const end = ref("11:00")

const emit = defineEmits(["pushEvent"])

</script>

<template>
  <q-form
  @submit="handleCreateEvent"
  class="flex"
  >
    <q-input
      fill
      v-model="name"
      label="Employee Name"
      :rules="[val => !!val || 'Field is required']"
    />
    <q-input filled v-model="date"  label="Date"
             :rules="[EventValidator.requiredRule, EventValidator.dayRule]"
    >
      <template v-slot:append>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-date v-model="date" mask="YYYY-MM-DD" today-btn first-day-of-week="1">
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>

    <q-input filled v-model="start" mask="time" :rules="[EventValidator.requiredRule, EventValidator.timeRule]" label="Start">
      <template v-slot:append>
        <q-icon name="access_time" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-time v-model="start" format24h>
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-time>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>

    <q-input filled v-model="end" mask="time" :rules="[EventValidator.requiredRule, EventValidator.timeRule]" label="End">
      <template v-slot:append>
        <q-icon name="access_time" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-time v-model="end" format24h>
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-time>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>

    <div>
      <q-btn label="Submit" type="submit" color="primary"/>
      <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
    </div>
  </q-form>

</template>
