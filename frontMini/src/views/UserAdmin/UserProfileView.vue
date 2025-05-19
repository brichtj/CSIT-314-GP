<template>
  <div>
    <SearchBar @search="searchUserProfile" details="Search User Profiles" />
    <Button
      label="Create Profile"
      class="bg-blue-500 hover:bg-blue-600 text-white"
      severity="info"
      @click="handleCreateClick"
    />
    <div style="display: flex; flex-wrap: wrap; gap: 16px; /* space between cards */ padding: 16px">
      <UserProfileCard
        v-for="userProfile in userProfiles"
        :key="userProfile.UserProfileID"
        :user-profile="userProfile"
        @edit="handleViewClick"
        :view-only="false"
      />
    </div>

    <UserProfileDetailsCard
      ref="editUserProfilePopUp"
      :userProfile="userProfileIndi!"
      @update="handleUpdateClick"
      @suspend="handleSuspendClick"
    />
  </div>
  <CreateUserProfile ref="createUserProfilePopUp" @create="handleCreate" />
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import type { UserProfile, CreateUserProfileType, UpdateUserProfileType } from '@/types/interfaces'
import { useToast, Button } from 'primevue'
import UserProfileDetailsCard from '@/components/UserProfile/UserProfileDetailsCard.vue'
import UserProfileCard from '@/components/UserProfile/UserProfileCard.vue'
import SearchBar from '@/components/SearchBar.vue'
import CreateUserProfile from '@/components/UserProfile/CreateUserProfile.vue'
const toast = useToast()

const userStore = useUserStore()
const userProfiles = computed(() => userStore.userProfiles)
const userProfileIndi = ref<UserProfile>()
const editUserProfilePopUp = ref()
const createUserProfilePopUp = ref()

onMounted(async () => {
  await userStore.searchUserProfiles(' ')
})

async function searchUserProfile(searchTerm: string) {
  await userStore.searchUserProfiles(searchTerm)
}

async function handleViewClick(userProfileID: number) {
  console.log(userProfileID)
  userProfileIndi.value = await userStore.viewUserProfile(userProfileID)
  editUserProfilePopUp.value.openPopup()
}

async function handleUpdateClick(updatedUserProfile: UpdateUserProfileType) {
  try {
    await userStore.updateUserProfile(updatedUserProfile)
    toast.add({
      severity: 'success',
      summary: 'User Profile Updated',
      detail: 'User profile updated successfully.',
      life: 3000,
    })
    editUserProfilePopUp.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error Updating User Profile',
      detail: err,
      life: 3000,
    })
  }
}

async function handleSuspendClick(userProfileId: number) {
  try {
    await userStore.suspendUserProfile(userProfileId)
    toast.add({
      severity: 'success',
      summary: 'User Profile Deleted',
      detail: 'User profile deleted successfully.',
      life: 3000,
    })
    editUserProfilePopUp.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error Deleting User Profile',
      detail: err,
      life: 3000,
    })
  }
}

function handleCreateClick() {
  createUserProfilePopUp.value.openPopup()
}
async function handleCreate(details: CreateUserProfileType) {
  try {
    await userStore.createUserProfile(details)
    toast.add({
      severity: 'success',
      summary: 'User Profile Created',
      detail: 'User profile created successfully.',
      life: 3000,
    })
    createUserProfilePopUp.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error Creating User Profile',
      detail: err,
      life: 3000,
    })
  }
}
</script>
