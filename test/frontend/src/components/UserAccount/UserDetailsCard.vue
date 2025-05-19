<template>
  <Dialog
    v-model:visible="pageVisible"
    :header="UserAccount?.Username ?? '' + ' Details'"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <!-- Cleaner Info -->
    <div class="border-t pt-3">
      <h3 class="font-semibold text-gray-800 mb-1">User Info</h3>
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div><strong>Name:</strong> {{ UserAccount.Username }}</div>
        <div><strong>Active:</strong> {{ UserAccount.IsActive ? 'Yes' : 'No' }}</div>
        <div><strong>Email:</strong> {{ UserAccount.Email }}</div>
        <div><strong>Phone:</strong> {{ UserAccount.Phone }}</div>
        <div><strong>Experience:</strong> {{ UserAccount.Experience }} years</div>
        <div><strong>Address:</strong> {{ UserAccount.Address ?? 'N/A' }}</div>
        <div><strong>Profile Name:</strong> {{ UserAccount.UserProfileName }}</div>
        <div><strong>Privilege:</strong> {{ UserAccount.Privilege }}</div>
        <div><strong>Profile ID:</strong> {{ UserAccount.UserProfile }}</div>
        <div><strong>Profile Active:</strong> {{ UserAccount.UPActive ? 'Yes' : 'No' }}</div>
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
        header="Edit User"
        :style="{ width: '30rem' }"
      >
        <span class="text-surface-500 dark:text-surface-400 block mb-8">
          Update the User information.
        </span>

        <div class="flex flex-col gap-4 mb-6">
          <div class="flex items-center gap-4">
            <label for="username" class="font-semibold w-28">Username</label>
            <InputText id="username" v-model="editUser.username" class="flex-auto" />
          </div>

          <div class="flex items-center gap-4">
            <label for="email" class="font-semibold w-28">Email</label>
            <InputText id="email" v-model="editUser.email" class="flex-auto" />
          </div>

          <div class="flex items-center gap-4">
            <label for="phone" class="font-semibold w-28">Phone</label>
            <InputText id="phone" v-model="editUser.phone" class="flex-auto" />
          </div>

          <div class="flex items-center gap-4">
            <label for="address" class="font-semibold w-28">Address</label>
            <InputText id="address" v-model="editUser.address" class="flex-auto" />
          </div>

          <div class="flex items-center gap-4">
            <label for="experience" class="font-semibold w-28">Experience</label>
            <InputNumber id="experience" v-model="editUser.Experience" class="flex-auto" :min="0" />
          </div>

          <div class="flex items-center gap-4">
            <label for="userProfile" class="font-semibold w-28">User Profile</label>
            <Dropdown
              id="userProfile"
              v-model="editUser.UserProfileID"
              :options="props.UserProfiles"
              optionLabel="Name"
              optionValue="UserProfileID"
              placeholder="Select a Profile"
              class="flex-auto"
            />
          </div>

          <div class="flex items-center gap-4">
            <label for="isActive" class="font-semibold w-28">Active</label>
            <InputSwitch id="isActive" v-model="editUser.IsActive" />
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
import { ref, computed, onMounted, watchEffect } from 'vue'
import Dialog from 'primevue/dialog'
import Button from 'primevue/button'
import Dropdown from 'primevue/dropdown'
import InputSwitch from 'primevue/inputswitch'
import { InputText } from 'primevue'
import type { CustomUserAccount, UpdateUserType, UserProfile } from '@/types/interfaces'
import { useToast } from 'primevue'
const toast = useToast()
const props = defineProps<{
  UserAccount: CustomUserAccount
  UserProfiles: UserProfile[]
}>()

const editUser = ref<UpdateUserType>({
  username: props.UserAccount?.Username ?? '',
  email: props.UserAccount?.Email ?? '',
  phone: props.UserAccount?.Phone ?? '',
  address: props.UserAccount?.Address ?? '',
  Experience: props.UserAccount?.Experience ?? 0,
  UserProfileID: props.UserAccount?.UserProfile ?? 0,
  IsActive: props.UserAccount?.IsActive ?? false,
  UserID: props.UserAccount?.UserID ?? 0,
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
  if (user && pageVisible.value) {
    editUser.value = {
      username: user.Username ?? '',
      email: user.Email ?? '',
      phone: user.Phone ?? '',
      address: user.Address ?? '',
      Experience: user.Experience ?? 0,
      UserProfileID: user.UserProfile ?? 0,
      IsActive: user.IsActive ?? false,
      UserID: user.UserID ?? 0,
    }
  }
})
import InputNumber from 'primevue/inputnumber'

const handleUpdateClick = () => {
  const { username, email, phone, Experience } = editUser.value

  if (!username || !email || !phone || Experience === null || Experience === undefined) {
    toast.add({
      severity: 'error',
      summary: 'Validation Error',
      detail: 'please ensure you filled out all necessary fields',
      life: 3000,
    })
    return
  }

  // Proceed with your update logic here

  emit('update', editUser.value)
  updateFieldVisibile.value = false
}
function handleSuspendClick() {
  emit('delete', props.UserAccount?.UserID ?? 0)
}
const emit = defineEmits<{
  (e: 'update', details: UpdateUserType): void
  (e: 'delete', serviceID: number): void
}>()
defineExpose({
  openPopup,
  closePopup,
})
</script>
