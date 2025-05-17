<template>
  <Dialog
    v-model:visible="pageVisible"
    :header="userProfile?.Name ?? '' + ' Details'"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <!-- Cleaner Info -->
    <div class="border-t pt-3">
      <h3 class="font-semibold text-gray-800 mb-1">User Info</h3>
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div><strong>Name:</strong> {{ userProfile?.Name ?? '' }}</div>
        <div><strong>Active:</strong> {{ userProfile?.Is_Active ? 'Yes' : 'No' }}</div>
        <div><strong>Privilege:</strong> {{ userProfile?.Privilege ?? '' }}</div>
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
        header="Edit User Profile"
        :style="{ width: '30rem' }"
      >
        <span class="text-surface-500 dark:text-surface-400 block mb-8">
          Update the user profile information.
        </span>

        <div class="flex flex-col gap-4 mb-6">
          <!-- Name -->
          <div class="flex items-center gap-4">
            <label for="name" class="font-semibold w-28">Name</label>
            <InputText id="name" v-model="editUserProfile.name" class="flex-auto" />
          </div>

          <!-- Privilege -->
          <div class="flex items-center gap-4">
            <label for="privilege" class="font-semibold w-28">Privilege</label>
            <InputText id="privilege" v-model="editUserProfile.privilege" class="flex-auto" />
          </div>

          <!-- Is Active -->
          <div class="flex items-center gap-4">
            <label for="isActive" class="font-semibold w-28">Active</label>
            <InputSwitch id="isActive" v-model="editUserProfile.is_active" />
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
<script setup lang="ts">
import { defineProps, defineEmits, ref, watchEffect } from 'vue'
import type { UserProfile, UpdateUserProfileType } from '@/types/interfaces'
const props = defineProps<{ userProfile: UserProfile }>()
const emit = defineEmits<{
  (e: 'update', details: UpdateUserProfileType): void
  (e: 'delete', userProfileID: number): void
}>()

const pageVisible = ref(false)
const updateFieldVisibile = ref(false)
const openPopup = () => {
  pageVisible.value = true
}
const editUserProfile = ref<UpdateUserProfileType>({
  name: props.userProfile?.Name ?? '',
  privilege: props.userProfile?.Privilege ?? '',
  is_active: props.userProfile?.Is_Active ?? false,
  userprofileID: props.userProfile?.UserProfileID ?? 0,
})
watchEffect(() => {
  if (pageVisible.value) {
    editUserProfile.value = {
      name: props.userProfile?.Name ?? '',
      privilege: props.userProfile?.Privilege ?? '',
      is_active: props.userProfile?.Is_Active ?? false,
      userprofileID: props.userProfile?.UserProfileID ?? 0,
    }
  }
})
const closePopup = () => {
  pageVisible.value = false
}

function handleUpdateClick() {}
function handleSuspendClick() {}

defineExpose({
  openPopup,
  closePopup,
})
</script>
