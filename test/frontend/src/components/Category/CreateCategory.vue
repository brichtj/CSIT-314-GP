<template>
  <Dialog
    v-model:visible="visible"
    header="Create Category"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <div class="space-y-4 p-3">
      <!-- Name -->
      <div>
        <label class="block font-medium mb-1">Title</label>
        <InputText
          v-model="createCategoryValues.Title"
          class="w-full"
          placeholder="Enter Profile Name"
        />
      </div>

      <!-- Privilege -->
      <div>
        <label class="block font-medium mb-1">Description</label>
        <InputText
          v-model="createCategoryValues.Description"
          class="w-full"
          placeholder="Enter privilege"
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
import type {
  CreateCategoryType,
  CreateUserProfileType,
  CreateUserType,
  UserProfile,
} from '@/types/interfaces'
const toast = useToast()

const createCategoryValues = ref<CreateCategoryType>({
  Title: '',
  Description: '',
})
const visible = ref(false)

const openPopup = () => {
  visible.value = true
}

const closePopup = () => {
  visible.value = false
}

function handleCreateClick() {
  const { Title, Description } = createCategoryValues.value

  if (!Title.trim() || !Description.trim()) {
    toast.add({
      severity: 'error',
      summary: 'Validation Error',
      detail: 'Title and description is required',
      life: 3000,
    })
    return
  }

  emit('create', createCategoryValues.value)
}
const emit = defineEmits<{
  (e: 'create', details: CreateCategoryType): void
}>()
defineExpose({
  openPopup,
  closePopup,
})
</script>
