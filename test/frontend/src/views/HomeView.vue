<template>
  <div>
    <Navbar />
    <SearchBar @search="searchServices" />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="service in services"
        :key="service.ServiceID"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <ServiceCard :service="service" @book="handleBookClick" @shortList="" />
      </div>
    </div>
    <ServiceDetailCard ref="popup" :service="service" />
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import Navbar from '../components/NavBar.vue'
import SearchBar from '../components/SearchBar.vue'
import ServiceCard from '../components/ServiceCard.vue'
import { useServiceStore } from '@/stores/serviceStore'
import ServiceDetailCard from '@/components/ServiceDetailCard.vue'
import { Service } from '@/types/interfaces'

//serviceStore
const serviceStore = useServiceStore()

const services = computed(() => serviceStore.services)
onMounted(() => {
  serviceStore.getServices(1, ' ')
})
async function searchServices(query: string) {
  console.log(query)
  await serviceStore.getServices(1, query)
  //do loading and stuff here
}

const popup = ref()
const service = ref<Service | null>(null)
async function handleBookClick(serviceID: number) {
  try {
    service.value = await serviceStore.viewService(serviceID)
    popup.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
</script>
