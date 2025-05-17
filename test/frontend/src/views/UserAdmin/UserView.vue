<template>
  <div>
    <SearchBar @search="searchUser" details="Search Users" />

    <div class="p-grid p-justify-start p-px-4">
      <div v-for="user in users" :key="user.UserID" class="p-col-12 p-md-4 p-lg-3 p-mb-3">
        <UserCard :user="user" @view="handleViewClick" :view-only="false" />
      </div>
    </div>
    <ServiceDetailCard ref="popup" :service="service" :view-only="false" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import Navbar from '../../components/NavBar.vue'
import SearchBar from '../../components/SearchBar.vue'
import UserCard from '@/components/UserAccount/UserCard.vue'
import { useUserStore } from '@/stores/user'
import ServiceDetailCard from '@/components/ServiceDetailCard.vue'
import type { CustomService } from '@/types/interfaces'
import { useAuthenticationStore } from '@/stores/authentication'

//serviceStore
const userStore = useUserStore()
const authStore = useAuthenticationStore()

const users = computed(() => userStore.userAccounts)
onMounted(() => {})
async function searchUser(query: string) {
  await userStore.searchUser(query)
  //do loading and stuff here
}

const popup = ref()
const service = ref<CustomService | null>(null)
async function handleViewClick(serviceID: number) {
  //   try {
  //     service.value = await userStore.viewService(serviceID, 'HomeOwner', authStore.user?.UserID ?? 1)
  //     popup.value.openPopup()
  //   } catch (err) {
  //     console.log(err)
  //   }
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
