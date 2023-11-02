<script setup>
import { ref } from "vue";

defineProps({
  events: {
    type: Array,
    required: true
  }
})

function handleCreateEvent() {
  // Emit values to parent
  console.log("Creation submitted")
}

const name = ref("")
const date = ref("2023/11/21")
const start = ref('10:00')
const end = ref("11:00")

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
    />
    <q-input filled v-model="date" mask="date" :rules="['date']" label="Date">
      <template v-slot:append>
        <q-icon name="event" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-date v-model="date" today-btn>
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-date>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>

    <q-input filled v-model="start" mask="time" :rules="['time']" label="Start">
      <template v-slot:append>
        <q-icon name="access_time" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-time v-model="end">
              <div class="row items-center justify-end">
                <q-btn v-close-popup label="Close" color="primary" flat />
              </div>
            </q-time>
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>

    <q-input filled v-model="end" mask="time" :rules="['time']" label="End">
      <template v-slot:append>
        <q-icon name="access_time" class="cursor-pointer">
          <q-popup-proxy cover transition-show="scale" transition-hide="scale">
            <q-time v-model="end">
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
