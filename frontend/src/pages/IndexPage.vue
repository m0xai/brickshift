<template>
  <q-page class="flex flex-center">
    <create-event-form @pushEvent="handlePushEvent($event)" :events="events" />
    <event-table  :events="events" />
  </q-page>
</template>

<script setup>
import { defineComponent } from "vue";
import EventTable from "components/EventTable.vue";
import CreateEventForm from "components/CreateEventForm.vue";

defineComponent({name: "IndexPage"})

function handlePushEvent(input) {
  console.log("Pusheda", input)
}

const events = [
]
</script>
