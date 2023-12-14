<script setup>
import { ref } from "vue";
import { useQuasar } from "quasar";
import { api } from "boot/axios";

const $q = useQuasar();
const imageObj = ref(null);

const previewImageUrl = ref("");

function counterLabelFn({ totalSize }) {
	return `${totalSize}`;
}

function imageUploadChange(image) {
	console.log(image);
	if (image) {
		previewImageUrl.value = URL.createObjectURL(imageObj.value);
	}
}

const predictions_response = ref(null);

function submitImagePlan() {
	if (!imageObj.value) {
		$q.notify({ message: "Please select a valid file to upload", color: "negative" });
	}
	const form = new FormData();
	form.append("image", imageObj.value);
	// TODO: set this fields by user's current calendar week page
	form.append("year", 2023);
	form.append("calendar_week", 31);

	api
		.post("/ki/upload/", form)
		.then((response) => {
			console.log(response);
			predictions_response.value = response.data;
			previewImageUrl.value = "";
		})
		.catch((err) => {
			console.error("Fehler: ", err);
		});
}

const resultCols = [
	{ name: "tag_id", label: "ID", field: "tag_id", align: "left" },
	{ name: "tag_name", label: "Tag Name", field: "tag_name", align: "left" },
	{ name: "probability", label: "Probability", field: "probability", align: "left" },
];

function clearImageUploadInput() {
	previewImageUrl.value = "";
	imageObj.value = null;
	predictions_response.value = null;
}

function showRejectedError() {
	$q.notify({
		color: "negative",
		position: "top-right",
		message: "The file you choose is not suitable for upload.",
	});
}
</script>

<template>
	<div class="flex column fa-align-center full-width">
		<p>Select a file to import all events at once</p>
		<q-form>
			<q-file
				v-model="imageObj"
				:counter-label="counterLabelFn"
				accept=".jpg, image/*"
				clearable
				counter
				filled
				hint="Allowed types are: jpg, jpeg, png, heif, webp and max filesize is 40MB"
				label="Pick photo to scan for weekly schedule"
				max-file-size="41943040"
				@clear="clearImageUploadInput"
				@rejected="showRejectedError"
				@update:model-value="imageUploadChange"
			>
				<template v-slot:prepend>
					<q-icon name="attach_file" />
				</template>
			</q-file>
		</q-form>
		<q-img v-if="previewImageUrl" :src="previewImageUrl" class="q-mt-md" spinner-color="blue" />
		<div v-if="previewImageUrl" class="flex justify-end q-mt-lg">
			<q-btn class="q-mr-md" color="danger" flat label="Reset" @click="clearImageUploadInput" />
			<q-btn color="primary" icon="cloud_upload" label="Send" @click="submitImagePlan" />
		</div>
		<q-table
			v-if="!previewImageUrl && predictions_response"
			:cols="resultCols"
			:pagination="{ rowsPerPage: 10 }"
			:rows="predictions_response"
			row-key="tag_id"
		></q-table>
	</div>
</template>
