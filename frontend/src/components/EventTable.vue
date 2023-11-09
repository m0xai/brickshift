<script setup>
import axios from "axios";
import { api } from "src/boot/axios";

const columns = [
  {
    name: "name",
    label: "Name",
    required: false,
    field: "name"
  },
  {name: "date", label: "Date", field: "date"},
  {name: "start", label: "Start", field: "start"},
  {name: "end", label: "End", field: "end"},
  { name: 'actions', label: 'Action(s)' }
]

defineProps({
  events: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(["deleteEvent"])
function handleEventDelete(event) {
    api.delete("calgen/events/" + event.id + "/").then((resp) => {
        emit("deleteEvent", event)
    })
}

</script>

<template>
  <div>
    <q-card>
      <q-card-section>
        <h4 class="text-h4">Schichtplan</h4>
        <p>All shift schedules are displayed in the table below. To add a new shift schedule, please utilize the form
          above. If you wish to delete a schedule, simply click on the trash icon located on the right side of a
          shift entry.</p>
      </q-card-section>
        <div class="q-pa-md">
          <q-table
            title="Schicht"
            :columns="columns"
            :rows="events"
            row-key="name">
              <template v-slot:body-cell-actions="props">
                  <q-td :props="props">
                      <q-btn icon="delete" @click="handleEventDelete(props.row)"></q-btn>
                  </q-td>
              </template>
          </q-table>
        </div>
    </q-card>

  </div>

</template>
