<script setup>
import { ref } from "vue";

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
</script>

<template>
	<div class="flex column fa-align-center full-width">
		<p>Select a file to import all events at once</p>
		<q-form>
			<q-file
				v-model="imageObj"
				label="Pick photo to scan for weekly schedule"
				filled
				counter
				:counter-label="counterLabelFn"
				hint="Allowed types are: jpg, jpeg, png, heif, webp and max filesize is 40MB"
				@update:model-value="imageUploadChange"
			>
				<template v-slot:prepend>
					<q-icon name="attach_file" />
				</template>
			</q-file>
			<q-img :src="previewImageUrl" spinner-color="blue" />
		</q-form>
	</div>
</template>
