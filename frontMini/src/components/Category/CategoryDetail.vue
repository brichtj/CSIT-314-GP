<template>
  <Dialog
    v-model:visible="pageVisible"
    :header="category?.Title ?? '' + ' Details'"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <!-- Cleaner Info -->
    <div class="border-t pt-3">
      <h3 class="font-semibold text-gray-800 mb-1">Category Information</h3>
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div><strong>Category:</strong> {{ category?.Title ?? '' }}</div>
        <div><strong>Active:</strong> {{ category?.IsActive ? 'Yes' : 'No' }}</div>
        <div><strong>Description:</strong> {{ category?.Description ?? '' }}</div>
      </div>
    </div>

    <template #footer>
      <div class="flex justify-between items-center w-full">
        <div class="flex items-center space-x-2">
          <Button
            label="Update"
            icon="pi pi-pencil"
            @click="updateFieldVisibile = true"
            severity="help"
          />
          <Button
            label="Suspend"
            icon="pi pi-trash"
            @click="handleSuspendClick"
            severity="danger"
          />
        </div>
        <div class="flex space-x-2">
          <Button label="Close" icon="pi pi-times" @click="closePopup" severity="warn" />
        </div>
      </div>

      <Dialog
        v-model:visible="updateFieldVisibile"
        modal
        header="Edit Category"
        :style="{ width: '30rem' }"
      >
        <span class="text-surface-500 dark:text-surface-400 block mb-8">
          Update the Category information.
        </span>

        <div class="flex flex-col gap-4 mb-6">
          <!-- Name -->
          <div class="flex items-center gap-4">
            <label for="name" class="font-semibold w-28">Name</label>
            <InputText id="name" v-model="editCategory.Title" class="flex-auto" />
          </div>

          <!-- Privilege -->
          <div class="flex items-center gap-4">
            <label for="privilege" class="font-semibold w-28">Description</label>
            <InputText id="privilege" v-model="editCategory.Description" class="flex-auto" />
          </div>

          <!-- Is Active -->
          <div class="flex items-center gap-4">
            <label for="isActive" class="font-semibold w-28">Active</label>
            <InputSwitch id="isActive" v-model="editCategory.Is_Active" />
          </div>
        </div>

        <div class="flex justify-end gap-2">
          <Button
            type="button"
            label="Cancel"
            severity="secondary"
            @click="updateFieldVisibile = false"
          />
          <Button type="button" label="Confirm" @click="handleUpdateClick" />
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
import { defineProps, defineEmits, ref, watchEffect } from 'vue'
import type { UpdateCategoryType, CategoryType } from '@/types/interfaces'
import { Button, Dialog, InputText } from 'primevue'
import InputSwitch from 'primevue/inputswitch'
const props = defineProps<{ category: CategoryType }>()
const emit = defineEmits<{
  (e: 'update', details: UpdateCategoryType): void
  (e: 'suspend', categoryID: number): void
}>()

const pageVisible = ref(false)
const updateFieldVisibile = ref(false)
const openPopup = () => {
  pageVisible.value = true
}
const editCategory = ref<UpdateCategoryType>({
  Title: props.category?.Title ?? '',
  Description: props.category?.Description ?? '',
  Is_Active: props.category?.IsActive ?? false,
  CategoryID: props.category?.CategoryID ?? 0,
})
watchEffect(() => {
  if (pageVisible.value) {
    editCategory.value = {
      Title: props.category?.Title ?? '',
      Description: props.category?.Description ?? '',
      Is_Active: props.category?.IsActive ?? false,
      CategoryID: props.category?.CategoryID ?? 0,
    }
  }
})
const closePopup = () => {
  pageVisible.value = false
}

function handleUpdateClick() {
  updateFieldVisibile.value = false
  emit('update', editCategory.value)
}
function handleSuspendClick() {
  emit('suspend', props.category?.CategoryID ?? 0)
}

defineExpose({
  openPopup,
  closePopup,
})
</script>
