<template>
  <div>
    <SearchBar @search="searchUser" details="Search Users" />

    <Button
      label="Add User"
      class="bg-blue-500 hover:bg-blue-600 text-white"
      severity="info"
      @click="handleCreateUserClick"
    />
    <div class="p-grid p-justify-start p-px-4">
      <div v-for="user in users" :key="user.UserID" class="p-col-12 p-md-4 p-lg-3 p-mb-3">
        <UserCard :user="user" @view="handleViewClick" :view-only="false" />
      </div>
    </div>
    <UserDetailsCard
      ref="popup"
      :UserAccount="userAccountCustom!"
      :UserProfiles="userProfiles"
      @update="handleUpdateClick"
      @delete="handleDeleteClick"
    />
  </div>
  <CreateUser ref="createUserPopup" :UserProfiles="userProfiles" @create="handleCreateUser" />
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import SearchBar from '../../components/SearchBar.vue'
import UserCard from '@/components/UserAccount/UserCard.vue'
import { useUserStore } from '@/stores/user'
import UserDetailsCard from '@/components/UserAccount/UserDetailsCard.vue'
import {
  type CreateUserType,
  type CustomUserAccount,
  type UpdateUserType,
  type UserProfile,
} from '@/types/interfaces'
import { useAuthenticationStore } from '@/stores/authentication'
import { useToast } from 'primevue'
import Button from 'primevue/button'
import CreateUser from '@/components/UserAccount/CreateUser.vue'
const toast = useToast()
//serviceStore
const userStore = useUserStore()
const authStore = useAuthenticationStore()

const users = computed(() => userStore.userAccounts)
const userProfiles = ref<UserProfile[]>([]) //to pass into userDetailsCard
const userAccountCustom = ref<CustomUserAccount>()

onMounted(async () => {
  userProfiles.value = await userStore.searchUserProfiles(' ')
})
async function searchUser(query: string) {
  await userStore.searchUser(query)
  //do loading and stuff here
}

const popup = ref()
const createUserPopup = ref()
async function handleUpdateClick(details: UpdateUserType) {
  try {
    await userStore.updateUserAccount(details)
    popup.value.closePopup()
    toast.add({
      severity: 'success',
      summary: 'Saved',
      detail: 'User created successfully',
      life: 3000,
    })
  } catch (err) {
    console.log(err)
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: err,
      life: 3000,
    })
  }
}

async function handleDeleteClick(UserID: number) {
  try {
    await userStore.suspendUser(UserID)
    toast.add({
      severity: 'success',
      summary: 'Suspend',
      detail: 'User suspended successfully',
      life: 3000,
    })
    popup.value.closePopup()
  } catch (err) {
    console.log(err)
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: err,
      life: 3000,
    })
  }
}
async function handleViewClick(serviceID: number) {
  //let result =await userStore.getUserProfiles()
  try {
    userAccountCustom.value = await userStore.viewUser(serviceID)
    popup.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
async function handleCreateUserClick() {
  createUserPopup.value.openPopup()
}

async function handleCreateUser(details: CreateUserType) {
  try {
    await userStore.CreateUserAccount(details)
    toast.add({
      severity: 'success',
      summary: 'User Created',
      detail: 'User created successfully.',
      life: 3000,
    })
    createUserPopup.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error Creating User',
      detail: err,
      life: 3000,
    })
  }
}
// async function handleConfirmBookClick(serviceID: number, offerPrice: number) {
//   try {
//     if (authStore.user?.UserID)
//       await userStore.confirmService(authStore.user?.UserID, serviceID, offerPrice)
//     else alert('You must be logged in to book a service.')
//   } catch (err) {
//     console.log(err)
//   }
// }
</script>
