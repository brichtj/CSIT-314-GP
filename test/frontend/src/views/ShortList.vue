<template>
  <div>
    <SearchBar @search="searchServices" details="Search Favourites" />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="service in services"
        :key="service.ServiceID"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <ServiceCard
          :service="service"
          @book="handleBookClick"
          @shortList="handleShortListClick"
          :view-only="true"
        />
      </div>
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

const services = computed(() => serviceStore.shortListedServices)
onMounted(() => {
  console.log('wass')
  serviceStore.getShortListedService(authStore.user?.UserID ?? 0, ' ')
})
async function searchServices(query: string) {
  await serviceStore.getShortListedService(authStore.user?.UserID ?? 0, query)
  //do loading and stuff here
}

const popup = ref()
const service = ref<CustomService | null>(null)
async function handleBookClick(serviceID: number) {
  try {
    service.value = await serviceStore.viewService(serviceID, 'shortlist', null)
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
