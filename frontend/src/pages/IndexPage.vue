<template>
  <q-page class="flex flex-center">
    <create-event-form :events="events" />
    <event-table :events="events" />
  </q-page>
</template>

<script setup>
import { defineComponent } from "vue";
import EventTable from "components/EventTable.vue";
import CreateEventForm from "components/CreateEventForm.vue";

defineComponent({name: "IndexPage"})

const events = [
  {
    name: "Kerem",
    date: `${new Date().getDay()}/${new Date().getMonth()}`,
    start: `${new Date().getHours()}:${new Date().getMinutes()}`,
    end: `${new Date().getHours()}:${new Date().getMinutes()}`,
  }
]
</script>
