<template>
  <div>
    <SearchBar @search="searchServices" details="Search Matches" />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="service in matches"
        :key="service.ServiceID"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <HistoryCard :match="service" @view="handleViewClick" />
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
import HistoryCard from '@/components/HistoryCard.vue'
import { useServiceStore } from '@/stores/serviceStore'
import type { CustomMatch } from '@/types/interfaces'
import { useAuthenticationStore } from '@/stores/authentication'
import HistoryDetailCard from '@/components/HistoryDetailCard.vue'

//serviceStore
const serviceStore = useServiceStore()
const authStore = useAuthenticationStore()

const matches = computed(() => serviceStore.matches)
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
async function handleViewClick(matchID: number) {
  try {
    match.value = await serviceStore.viewMatch(matchID)
    popup.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
</script>
