<template>
  <div>
    <SearchBar @search="searchUserProfile" details="Search User Profiles" />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="userProfile in userProfiles"
        :key="userProfile.UserProfileID"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <UserProfileCard :user-profile="userProfile" @view="handleViewClick" :view-only="false" />
      </div>
    </div>
    <UserProfileDetailsCard
      ref="createUserProfilePopup"
      :userProfile="userProfileIndi!"
      @update="handleUpdateClick"
      @delete="handleDeleteClick"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import type { UserProfile, CreateUserProfileType, UpdateUserProfileType } from '@/types/interfaces'
import { useToast } from 'primevue'
import UserProfileDetailsCard from '@/components/UserProfile/UserProfileDetailsCard.vue'
import UserProfileCard from '@/components/UserProfile/UserProfileCard.vue'
import SearchBar from '@/components/SearchBar.vue'
const toast = useToast()

const userStore = useUserStore()
const userProfiles = computed(() => userStore.userProfiles)
const userProfileIndi = ref<UserProfile>()
const createUserProfilePopup = ref()

onMounted(async () => {
  await userStore.searchUserProfiles(' ')
})

async function searchUserProfile(searchTerm: string) {
  await userStore.searchUserProfiles(searchTerm)
}

function handleViewClick(userProfile: UserProfile) {
  userProfileIndi.value = userProfile
  createUserProfilePopup.value.openPopup()
}

async function handleUpdateClick(updatedUserProfile: UpdateUserProfileType) {
  //   try {
  //     await userStore.updateUserProfile(updatedUserProfile)
  //     toast.add({
  //       severity: 'success',
  //       summary: 'User Profile Updated',
  //       detail: 'User profile updated successfully.',
  //       life: 3000,
  //     })
  //     createUserProfilePopup.value.closePopup()
  //   } catch (err) {
  //     toast.add({
  //       severity: 'error',
  //       summary: 'Error Updating User Profile',
  //       detail: err.message,
  //       life: 3000,
  //     })
  //   }
}

async function handleDeleteClick(userProfileId: number) {
  //   try {
  //     await userStore.deleteUserProfile(userProfileId)
  //     toast.add({
  //       severity: 'success',
  //       summary: 'User Profile Deleted',
  //       detail: 'User profile deleted successfully.',
  //       life: 3000,
  //     })
  //   } catch (err) {
  //     toast.add({
  //       severity: 'error',
  //       summary: 'Error Deleting User Profile',
  //       detail: err.message,
  //       life: 3000,
  //     })
  //   }
}
</script>
