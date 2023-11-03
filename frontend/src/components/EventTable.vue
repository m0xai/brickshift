<script setup>
import axios from "axios";

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
  { name: 'actions', label: 'action' }
]

defineProps({
  events: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(["deleteEvent"])
function handleEventDelete(event) {
    axios.delete("http://localhost:8000/calgen/events/" + event.id + "/").then((resp) => {
        emit("deleteEvent", event)
    })
}

</script>

<template>
  <div>
    <q-card>
      <h4 class="text-h4">Schichtplan</h4>
      <q-card-section>
        <p>Aliqua laborum nulla sunt nulla laboris duis ut. Ipsum reprehenderit sint nulla veniam occaecat reprehenderit magna incididunt sint.</p>
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
