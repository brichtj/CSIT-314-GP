<template></template>
<template>
  <Dialog
    v-model:visible="pageVisible"
    header="Service Details"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <div v-if="service" class="space-y-3">
      <img
        :src="imageSrc"
        alt="Service"
        class="mx-auto object-cover rounded-md"
        style="width: 200px; height: 200px"
        @error="handleImageError"
      />
      <h2 class="text-xl font-semibold">{{ service.Title }}</h2>
      <p class="text-gray-700">{{ service.Description }}</p>

      <!-- Service Info -->
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600 border-t pt-3">
        <div><strong>Date Posted:</strong> {{ formattedDate }}</div>
        <div><strong>Price:</strong> ${{ service.Price.toFixed(2) }}</div>
        <div><strong>Likes:</strong> {{ actualLikes }}</div>
        <div><strong>Views:</strong> {{ actualViews }}</div>
      </div>

      <!-- Category Info -->
      <div class="border-t pt-3">
        <h3 class="font-semibold text-gray-800 mb-1">Category Info</h3>
        <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
          <div><strong>Title:</strong> {{ service.CatTitle }}</div>
          <div class="col-span-2">
            <strong>Description:</strong>
            <p class="ml-2">{{ service.CatDesc }}</p>
          </div>
        </div>
      </div>

      <!-- Cleaner Info -->
      <div class="border-t pt-3">
        <h3 class="font-semibold text-gray-800 mb-1">Cleaner Info</h3>
        <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
          <div><strong>Name:</strong> {{ service.Username }}</div>
          <div><strong>Active:</strong> {{ service.UActive ? 'Yes' : 'No' }}</div>
          <div><strong>Email:</strong> {{ service.Email }}</div>
          <div><strong>Phone:</strong> {{ service.Phone }}</div>
          <div><strong>Experience:</strong> {{ service.Experience }} years</div>
        </div>
      </div>
    </div>

    <template #footer>
      <div class="flex justify-between items-center w-full" v-if="!viewOnly">
        <div class="flex items-center space-x-2">
          <Button
            label="Update"
            icon="pi pi-pencil"
            @click="updateFieldVisibile = true"
            severity="help"
          />
          <Button label="Delete" icon="pi pi-trash" @click="handleDeleteClick" severity="danger" />
        </div>
        <div class="flex space-x-2">
          <Button label="Close" icon="pi pi-times" @click="closePopup" severity="warn" />
        </div>
      </div>

      <Dialog
        v-model:visible="updateFieldVisibile"
        modal
        header="Edit Service"
        :style="{ width: '30rem' }"
      >
        <span class="text-surface-500 dark:text-surface-400 block mb-8">
          Update the service information.
        </span>

        <div class="flex flex-col gap-4 mb-6">
          <div class="flex items-center gap-4">
            <label for="title" class="font-semibold w-28">Title</label>
            <InputText id="title" v-model="editService.Title" class="flex-auto" />
          </div>
          <div>
            <Dropdown
              v-model="editService.CategoryID"
              :options="categories"
              optionLabel="Title"
              optionValue="CategoryID"
              placeholder="Select a Category"
              :filter="true"
            />
            <p v-if="editService.CategoryID">Selected ID: {{ editService.CategoryID }}</p>
          </div>
          <div class="flex items-center gap-4">
            <label for="description" class="font-semibold w-28">Description</label>
            <InputText id="description" v-model="editService.Description" class="flex-auto" />
          </div>
          <div class="flex items-center gap-4">
            <label for="price" class="font-semibold w-28">Price</label>
            <InputNumber
              id="price"
              v-model="editService.Price"
              class="flex-auto"
              mode="currency"
              currency="USD"
            />
          </div>
          <div class="flex items-center gap-4">
            <label for="image" class="font-semibold w-28">Image URL</label>
            <InputText id="image" v-model="editService.ImageLink" class="flex-auto" />
          </div>
        </div>

        <div class="flex justify-end gap-2">
          <Button
            type="button"
            label="Cancel"
            severity="secondary"
            @click="updateFieldVisibile = false"
          />
          <Button type="button" label="confirm" @click="handleUpdateClick" />
        </div>
      </Dialog>
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
import type { CreateUserType, CustomService, CustomUserAccount } from '@/types/interfaces'

const props = defineProps<{
  UserAccount: CustomUserAccount | null
  viewOnly: boolean
  actualViews: number
  actualLikes: number
  categories: { CategoryID: number; Title: string; Description: string; IsActive: boolean }[]
}>()

const editUser = ref<CreateUserType>({
  username: props.UserAccount?.Username ?? '',
  email: props.UserAccount?.Email ?? '',
  phone: props.UserAccount?.Phone ?? '',
  address: props.UserAccount?.Address ?? '',
  Experience: props.UserAccount?.Experience ?? 0,
  UserProfileID: props.UserAccount?.UserProfile ?? 0,
})
const pageVisible = ref(false)
const updateFieldVisibile = ref(false)

const openPopup = () => {
  pageVisible.value = true
}

const closePopup = () => {
  pageVisible.value = false
}
watchEffect(() => {
  const user = props.UserAccount
  if (user) {
    editUser.value = {
      username: user.Username ?? '',
      email: user.Email ?? '',
      phone: user.Phone ?? '',
      address: user.Address ?? '',
      Experience: user.Experience ?? 0,
      UserProfileID: user.UserProfile ?? 0,
    }
  }
})
import InputNumber from 'primevue/inputnumber'

function handleUpdateClick() {
  emit('update', editUser.value)
  updateFieldVisibile.value = false
}
function handleDeleteClick() {
  emit('delete', props.UserAccount?.UserID ?? 0)
  updateFieldVisibile.value = false
}
const emit = defineEmits<{
  (e: 'update', details: CustomUserAccount): void
  (e: 'delete', serviceID: number): void
}>()
defineExpose({
  openPopup,
  closePopup,
})
</script>
