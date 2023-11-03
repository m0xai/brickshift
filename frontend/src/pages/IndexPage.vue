<template>
  <q-page class="flex flex-center">
    <create-event-form @pushEvent="handlePushEvent($event)" :events="events" />
    <event-table  :events="events" />
    <q-btn @click="handleEventFeedSubmit">Create Calendar</q-btn>
  </q-page>
</template>

<script setup>
import { defineComponent, ref } from "vue";
import EventTable from "components/EventTable.vue";
import CreateEventForm from "components/CreateEventForm.vue";
import axios from "axios";

defineComponent({name: "IndexPage"})

function handlePushEvent(input) {
  events.value.push(input)
  console.log("Pusheda", input)
}

const events = ref([])

function handleEventFeedSubmit() {
  if(!events.value.length > 0) {
    return
  }
  axios.post("http://localhost:8000/calgen/create-event-feed/", events.value)
    .then((resp) => {
      console.log("Rsp: ", resp)
    })
}
</script>
