<script setup>
import { ref, defineProps } from "vue";

const persistent = ref(false);

defineOptions({ name: "EventEdit" });

const props = defineProps({ eventItem: {} });

const inputName = ref("");
const inputDescription = ref("");
const inputDate = ref(new Date());
const inputStart = ref("00:00:00");
const inputEnd = ref("00:00");

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
  <q-btn @click="persistent = true" icon="edit" />

  <q-dialog
    v-model="persistent"
    persistent
    transition-show="scale"
    transition-hide="scale"
    @hide="resetForm()"
    @show="setFieldValues()"
  >
    <q-card class="text-white" style="width: 400px">
      <q-card-section class="bg-primary">
        <div class="text-h6">Edit Schicht fuer {{ props.eventItem.name }}</div>
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

      <q-card-actions align="right">
        <q-btn flat label="Cancel" v-close-popup class="text-negative" />
        <q-btn label="Save" color="primary" class="text-primary" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>
