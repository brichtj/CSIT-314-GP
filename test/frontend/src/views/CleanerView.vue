<template>
  <div>
    <SearchBar @search="searchServices" details="Search your services" />

    <Button label="Add" class="bg-blue-500 hover:bg-blue-600 text-white" severity="info" />

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
          :view-only="false"
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
import Button from 'primevue/button'

//serviceStore
const serviceStore = useServiceStore()
const authStore = useAuthenticationStore()

const services = computed(() => serviceStore.services)
onMounted(() => {
  serviceStore.getServicesForCleaner(authStore.user?.UserID ?? 1, ' ')
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
