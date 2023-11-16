<script setup>
import { defineComponent } from "vue";

defineComponent({ name: "ProfilePage" });
</script>

<template>
	<h3>Profile Page</h3>
	<form class="profile-form flex column">
		<q-input label="First Name"></q-input>
		<q-input label="Last Name"></q-input>
		<q-input label="Username"></q-input>
		<q-input label="Email"></q-input>
		<q-input label="Password"></q-input>
		<div class="form-actions">
			<q-btn class="q-ml-sm" color="primary" flat label="Reset" type="reset" />
			<q-btn color="primary" label="Submit" type="submit" />
		</div>
	</form>
</template>

<style scoped>
.profile-form {
	width: 100%;
	max-width: 600px;
}

.profile-form > label {
	margin: 1rem;
}
</style>
