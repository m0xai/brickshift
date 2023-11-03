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


function handleEventFeedDownload() {
  if(!events.value.length > 0) {
    return
  }

  const method = 'GET';
  const url = 'http://localhost:8000/calgen/latest/feed.ics';
  const fileName = `feed_${new Date().toISOString()}.ics`
  axios
      .request({
        url,
        method,
        responseType: 'blob',
      })
      .then(({ data }) => {
        const downloadUrl = window.URL.createObjectURL(new Blob([data]));
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.setAttribute('download', fileName);
        document.body.appendChild(link);
        link.click();
        link.remove();
      });
}
</script>
