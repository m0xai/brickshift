<script setup>
const columns = [
  {
    name: "name",
    label: "Name",
    required: false,
    field: "name"
  },
  {name: "date", label: "Date", field: "date"},
  {name: "start", label: "Start", field: "start"},
  {name: "end", label: "End", field: "end"}
]

const rows = [
  {
    name: "Kerem",
    date: `${new Date().getDay()}/${new Date().getMonth()}`,
    start: `${new Date().getHours()}:${new Date().getMinutes()}`,
    end: `${new Date().getHours()}:${new Date().getMinutes()}`,
  }
]
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
            :rows="rows"
            row-key="name"
          />
        </div>
    </q-card>

  </div>

</template>
