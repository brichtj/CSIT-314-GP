<template>
  <div>
    <SearchBar @search="searchServices" details="Search services" />

    <div style="display: flex; flex-wrap: wrap; gap: 16px; /* space between cards */ padding: 16px">
      <ServiceCard
        v-for="service in services"
        :key="service.ServiceID"
        :service="service"
        @book="handleBookClick"
        @shortList="handleShortListClick"
        :view-only="false"
      />
    </div>
    <ServiceDetailCard
      ref="popup"
      :service="service"
      @book="handleConfirmBookClick"
      :view-only="false"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import Navbar from '../components/NavBar.vue'
import SearchBar from '../components/SearchBar.vue'
import ServiceCard from '../components/ServiceCard.vue'
import { useServiceStore } from '@/stores/serviceStore'
import ServiceDetailCard from '@/components/ServiceDetailCard.vue'
import type { CustomService } from '@/types/interfaces'
import { useAuthenticationStore } from '@/stores/authentication'

//serviceStore
const serviceStore = useServiceStore()
const authStore = useAuthenticationStore()

const services = computed(() => serviceStore.services)
onMounted(() => {
  serviceStore.getServices(1, ' ')
})
async function searchServices(query: string) {
  await serviceStore.getServices(1, query)
  //do loading and stuff here
}

const popup = ref()
const service = ref<CustomService | null>(null)
async function handleBookClick(serviceID: number) {
  try {
    service.value = await serviceStore.viewService(
      serviceID,
      'HomeOwner',
      authStore.user?.UserID ?? 1,
    )
    popup.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
async function handleConfirmBookClick(serviceID: number, offerPrice: number) {
  try {
    if (authStore.user?.UserID)
      await serviceStore.confirmService(authStore.user?.UserID, serviceID, offerPrice)
    else alert('You must be logged in to book a service.')
  } catch (err) {
    console.log(err)
  }
}
async function handleShortListClick(serviceID: number) {
  try {
    if (authStore.user?.UserID)
      await serviceStore.shortListService(serviceID, authStore.user.UserID)
    else alert('You must be logged in to shortlist a service.')
  } catch (err) {
    console.log(err)
  }
}
</script>
