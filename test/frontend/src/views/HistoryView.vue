<template>
  <div>
    <SearchBar @search="searchServices" details="Search Matches" />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="service in services"
        :key="service.ServiceID"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <ServiceCard :service="service" @book="handleViewClick" :view-only="true" />
      </div>
    </div>
    <HistoryDetailCard ref="popup" :service="match" :view-only="false" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import Navbar from '../components/NavBar.vue'
import SearchBar from '../components/SearchBar.vue'
import ServiceCard from '../components/ServiceCard.vue'
import { useServiceStore } from '@/stores/serviceStore'
import type { CustomMatch } from '@/types/interfaces'
import { useAuthenticationStore } from '@/stores/authentication'
import HistoryDetailCard from '@/components/HistoryDetailCard.vue'

//serviceStore
const serviceStore = useServiceStore()
const authStore = useAuthenticationStore()

const services = computed(() => serviceStore.matches)
onMounted(() => {
  if (authStore.user?.UserProfileName == 'HomeOwner') {
    serviceStore.getMatchesHomeOwner(authStore.user?.UserID ?? 0, ' ')
  }
})
async function searchServices(query: string) {
  await serviceStore.getShortListedService(authStore.user?.UserID ?? 0, query)
  //do loading and stuff here
}

const popup = ref()
const match = ref<CustomMatch | null>(null)
async function handleViewClick(serviceID: number) {
  try {
    match.value = await serviceStore.viewMatch(serviceID)
    popup.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
</script>
