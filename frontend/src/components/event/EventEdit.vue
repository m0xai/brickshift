<script setup>
import { ref, defineProps } from "vue";
import * as EventValidator from "src/services/validators/event-validator"


defineOptions({ name: "EventEdit" });

const props = defineProps({ eventItem: {} });

const inputName = ref("");
const inputDescription = ref("");
const inputDate = ref(new Date());
const inputStart = ref("00:00:00");
const inputEnd = ref("00:00");
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
        <q-btn label="Save" color="primary" class="text-primary" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>
