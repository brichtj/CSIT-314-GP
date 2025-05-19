<template>
  <Dialog
    v-model:visible="visible"
    header="Create Service"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <div class="space-y-4 p-3">
      <!-- Title -->
      <div>
        <label class="block font-medium mb-1">Title</label>
        <InputText
          v-model="createServiceValues.Title"
          class="w-full"
          placeholder="Enter service title"
        />
      </div>

      <!-- Category Dropdown -->
      <div>
        <label class="block font-medium mb-1">Category</label>
        <Dropdown
          v-model="createServiceValues.CategoryID"
          :options="props.categories"
          optionLabel="Title"
          optionValue="CategoryID"
          class="w-full"
          placeholder="Select category"
        />
      </div>

      <!-- Description -->
      <div>
        <label class="block font-medium mb-1">Description</label>
        <InputText
          v-model="createServiceValues.Description"
          class="w-full"
          placeholder="Enter description"
        />
      </div>

      <!-- Price -->
      <div>
        <label class="block font-medium mb-1">Price</label>
        <InputNumber
          v-model="createServiceValues.Price"
          mode="currency"
          currency="USD"
          class="w-full"
          placeholder="Enter price"
        />
      </div>

      <!-- Image Link -->
      <div>
        <label class="block font-medium mb-1">Image Link</label>
        <InputText
          v-model="createServiceValues.ImageLink"
          class="w-full"
          placeholder="Enter image URL"
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
const toast = useToast()

const props = defineProps<{
  categories: { CategoryID: number; Title: string; Description: string; IsActive: boolean }[]
}>()
interface CreateServiceType {
  CategoryID: number
  Title: string
  Description: string
  Price: number
  ImageLink: string
}

const createServiceValues = ref<CreateServiceType>({
  CategoryID: props.categories[0]?.CategoryID ?? 0,
  Title: '',
  Description: '',
  Price: 0,
  ImageLink: '',
})
const visible = ref(false)

const openPopup = () => {
  visible.value = true
}

const closePopup = () => {
  visible.value = false
}

function handleCreateClick() {
  const { Title, Description, Price, CategoryID } = createServiceValues.value
  console.log(Title, Description, Price, CategoryID)
  if (!Title.trim() || !Description.trim() || Price <= 0 || CategoryID == 0) {
    toast.add({
      severity: 'error',
      summary: 'Validation Error',
      detail: 'Title, Description, Price and category are required. Price must be greater than 0.',
      life: 3000,
    })
    return
  }
  emit('create', createServiceValues.value)
}
const emit = defineEmits<{
  (e: 'create', details: CreateServiceType): void
}>()
defineExpose({
  openPopup,
  closePopup,
})
</script>
