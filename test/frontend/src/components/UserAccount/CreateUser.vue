<template>
  <Dialog
    v-model:visible="visible"
    header="Create User"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <div class="space-y-4 p-3">
      <!-- Username -->
      <div>
        <label class="block font-medium mb-1">Username</label>
        <InputText
          v-model="createUserValues.username"
          class="w-full"
          placeholder="Enter username"
        />
      </div>

      <!-- Email -->
      <div>
        <label class="block font-medium mb-1">Email</label>
        <InputText v-model="createUserValues.email" class="w-full" placeholder="Enter email" />
      </div>

      <!-- Phone -->
      <div>
        <label class="block font-medium mb-1">Phone</label>
        <InputText
          v-model="createUserValues.phone"
          class="w-full"
          placeholder="Enter phone number"
        />
      </div>

      <!-- Address -->
      <div>
        <label class="block font-medium mb-1">Address</label>
        <InputText v-model="createUserValues.address" class="w-full" placeholder="Enter address" />
      </div>

      <!-- Experience -->
      <div>
        <label class="block font-medium mb-1">Experience (years)</label>
        <InputNumber
          v-model="createUserValues.Experience"
          class="w-full"
          placeholder="Enter experience"
        />
      </div>

      <!-- User Profile Dropdown -->
      <div>
        <label class="block font-medium mb-1">User Profile</label>
        <Dropdown
          v-model="createUserValues.UserProfileID"
          :options="UserProfiles"
          optionLabel="Name"
          optionValue="UserProfileID"
          class="w-full"
          placeholder="Select user profile"
        />
      </div>
    </div>

    <template #footer>
      <div class="flex justify-between items-center w-full">
        <div class="flex items-center space-x-2">
          <Button label="Confirm" icon="pi pi-check" @click="handleCreateClick" severity="info" />
        </div>
        <div class="flex space-x-2">
          <Button label="Close" icon="pi pi-times" @click="closePopup" severity="warn" />
        </div>
      </div>
    </template>
  </Dialog>
</template>

<style scoped>
h3 {
  font-weight: 800; /* very bold */
  text-decoration: underline;
  color: #1f2937; /* Tailwind's text-gray-800 */
  margin-bottom: 0.25rem; /* similar to mb-1 */
}
</style>

<script setup lang="ts">
import { ref, computed, onMounted, watchEffect } from 'vue'
import Dialog from 'primevue/dialog'
import Button from 'primevue/button'
import Dropdown from 'primevue/dropdown'
import { InputText } from 'primevue'
import InputNumber from 'primevue/inputnumber'
import { useToast } from 'primevue/usetoast'
import type { CreateUserType, UserProfile } from '@/types/interfaces'
const toast = useToast()

const props = defineProps<{
  UserProfiles: UserProfile[]
}>()

const createUserValues = ref<CreateUserType>({
  username: '',
  email: '',
  phone: '',
  address: '',
  Experience: 0,
  UserProfileID: 0,
})
const visible = ref(false)

const openPopup = () => {
  console.log('fuck')
  visible.value = true
}

const closePopup = () => {
  visible.value = false
}

function handleCreateClick() {
  const { username, email, phone, Experience, UserProfileID } = createUserValues.value

  if (!username.trim() || !email.trim() || !phone.trim() || UserProfileID === 0) {
    toast.add({
      severity: 'error',
      summary: 'Validation Error',
      detail: 'Username, Email, Phone, and User Profile are required.',
      life: 3000,
    })
    return
  }

  emit('create', createUserValues.value)
}
const emit = defineEmits<{
  (e: 'create', details: CreateUserType): void
}>()
defineExpose({
  openPopup,
  closePopup,
})
</script>
