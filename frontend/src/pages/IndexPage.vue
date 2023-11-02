<template>
  <q-page class="flex flex-center">
    <create-event-form />
    <event-table />
  </q-page>
</template>

<script setup>
import { defineComponent } from "vue";
import EventTable from "components/EventTable.vue";
import CreateEventForm from "components/CreateEventForm.vue";

defineComponent({name: "IndexPage"})

</script>
