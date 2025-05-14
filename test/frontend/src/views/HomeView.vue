<template>
  <div>
    <Navbar />
    <SearchBar @search="filterServices" />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="service in filteredServices"
        :key="service.id"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <ServiceCard :service="service" @book="bookService" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import Navbar from '../components/NavBar.vue'
import SearchBar from '../components/SearchBar.vue'
import ServiceCard from '../components/ServiceCard.vue'

interface Service {
  id: number
  name: string
  description: string
  image: string
}

const services = ref<Service[]>([
  {
    id: 1,
    name: 'Basic Cleaning',
    description: 'Dust, mop, sanitize.',
    image: 'https://via.placeholder.com/300x200',
  },
  {
    id: 2,
    name: 'Deep Cleaning',
    description: 'Thorough cleaning in every corner.',
    image: 'https://via.placeholder.com/300x200',
  },
  {
    id: 3,
    name: 'Move Out Cleaning',
    description: 'Perfect before moving in or out.',
    image: 'https://via.placeholder.com/300x200',
  },
])

const searchQuery = ref('')

const filteredServices = computed(() =>
  services.value.filter((s) => s.name.toLowerCase().includes(searchQuery.value.toLowerCase())),
)

function filterServices(query: string) {
  searchQuery.value = query
}

function bookService(service: Service) {
  alert(`Booked: ${service.name}`)
}
</script>
