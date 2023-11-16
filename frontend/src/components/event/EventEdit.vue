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

function setFieldValues() {
  inputName.value = props.eventItem.name;
  inputDescription.value = props.eventItem.description;
  inputDate.value = props.eventItem.date;
  inputStart.value = props.eventItem.start;
  inputEnd.value = props.eventItem.end;
}
function resetForm() {
  inputName.value = "";
  inputDescription.value = "";
  inputDate.value = new Date();
  inputStart.value = "00:00:00";
  inputEnd.value = "00:00";
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
        <q-form>
          <q-input v-model="inputName" class="q-mb-md" filled label="Name" />
          <q-input v-model="inputDescription" label="Description" type="textarea" filled class="q-mb-md"/>
          <q-input
            filled
            v-model="inputDate"
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
                  <q-date v-model="inputDate">
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
            v-model="inputStart"
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
                  <q-time v-model="inputStart" format24h>
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
            v-model="inputEnd"
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
                  <q-time v-model="inputEnd" format24h>
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
