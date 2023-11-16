<script setup>
import { ref, defineProps } from "vue";
import * as EventValidator from "src/services/validators/event-validator"
import { QForm, useQuasar } from "quasar";
import { api } from "boot/axios";

defineOptions({ name: "EventEdit" });
const emit = defineEmits(["updateEvent"])
const props = defineProps({ eventItem: {} });

const $q = useQuasar();

const qform = ref(null);
const isDialogOpen = ref(false);

const editFormFields = ref({
  name:  "",
  description: "",
  date: new Date(),
  start: "00:00:00",
  end:  "00:00:00"
})

function setFieldValues() {
  editFormFields.value.name = props.eventItem.name;
  editFormFields.value.description = props.eventItem.description;
  editFormFields.value.date = props.eventItem.date;
  editFormFields.value.start = props.eventItem.start;
  editFormFields.value.end = props.eventItem.end;
}
function resetForm() {
  editFormFields.value.name = "";
  editFormFields.value.description = "";
  editFormFields.value.date = new Date();
  editFormFields.value.start = "00:00:00";
  editFormFields.value.end = "00:00";
}

async function handleEventUpdate() {
  const isValid = await qform.value?.validate();
  if(isValid) {
    api.put("calgen/events/" + props.eventItem.id + "/", {...editFormFields.value}).then((response) => {
      emit("updateEvent", props.eventItem.id, editFormFields.value)
      $q.notify({message: "Schicht successfully updated.", position: "top-right", color: "positive"})
      isDialogOpen.value = false;
    }).catch((err) => {
      $q.notify({message: "Task update failed: " + err.message, position: "top-right", color: "negative"})
    })
  } else {
    $q.notify({message: "Task update failed: Please ensure that all fields contain valid information.", position: "top-right",
      color: "negative"})
  }
}

</script>

<template>
  <q-btn fab-mini flat @click="isDialogOpen = true" icon="edit" />

  <q-dialog
    v-model="isDialogOpen"
    persistent
    transition-show="scale"
    transition-hide="scale"
    @hide="resetForm()"
    @show="setFieldValues()"
  >
    <q-card class="text-white" style="width: 500px">
      <q-card-section class="bg-primary flex">
        <div class="text-h6">Edit Schicht fuer {{ props.eventItem.name }}</div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </q-card-section>

      <q-card-section>
        <q-form ref="qform">
          <q-input v-model="editFormFields.name" class="q-mb-md" filled label="Name" />
          <q-input v-model="editFormFields.description" label="Description" type="textarea" filled class="q-mb-md"/>
          <q-input
            filled
            v-model="editFormFields.date"
            mask="####-##-##"
            :rules="[EventValidator.requiredRule, EventValidator.dayRule]"
          >
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-date v-model="editFormFields.date">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>

          <q-input
            filled
            v-model="editFormFields.start"
            mask="time"
            :rules="[EventValidator.requiredRule, EventValidator.timeRule]"
          >
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-time v-model="editFormFields.start" format24h>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>

          <q-input
            filled
            v-model="editFormFields.end"
            mask="time"
            :rules="[EventValidator.requiredRule, EventValidator.timeRule]"
          >
            <template v-slot:append>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy
                  cover
                  transition-show="scale"
                  transition-hide="scale"
                >
                  <q-time v-model="editFormFields.end" format24h>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </q-form>
      </q-card-section>

      <q-card-actions class="flex justify-between q-mx-sm">
        <q-btn flat label="Cancel" class="" color="primary" v-close-popup />
        <q-btn label="Save" color="primary" class="text-primary" @click="handleEventUpdate()"/>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>
