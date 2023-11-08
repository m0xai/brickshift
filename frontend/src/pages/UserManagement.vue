<script setup>
const columns = [
  {
    name: 'firstName',
    field: 'firstName',
    required: true,
    label: 'First Name',
    align: 'left',
    sortable: true
  },
  { name: 'lastName', field: 'lastName', label: 'Last Name', align: 'left', sortable: true },
  { name: 'username', field: "username", label: 'Username', align: 'left', sortable: true},
  { name: 'email', field: "email", label: 'Email', align: 'left', sortable: true},
  { name: 'actions', label: 'Actions', align: 'center' },
]

const rows = [
  {
    firstName: 'Max',
    lastName: "Mustermann",
    username: 'max',
    email: "max@mustermann.com"
  },
  {
    firstName: 'Jane',
    lastName: "Doe",
    username: "jane",
    email: "jane@doe.com"
  },
  {
    firstName: 'john',
    lastName: "Doe",
    username: "john",
    email: "john@doe.com"
  },
]

</script>

<template>
<h2>User Management</h2>
  <p>Only Admin(s) can see this page</p>
  <div class="q-pa-md">
    <q-table
      title="Users"
      :rows="rows"
      :columns="columns"
      row-key="name"
    >
      <template v-slot:top>
        <q-input dense debounce="300" color="primary" label="Search Users" v-model="filter">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-space />
        <q-btn color="primary" :disable="loading" label="Add User" @click="addUser" />
      </template>
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn icon="edit" @click="handleUserDelete(props.row)"></q-btn>
          <q-btn icon="delete" @click="handleUserDelete(props.row)"></q-btn>
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<style scoped>

</style>
