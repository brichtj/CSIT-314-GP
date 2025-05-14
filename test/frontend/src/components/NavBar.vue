<template>
  <Menubar v-if="!isLoginPage" :model="menuItems" class="mb-3">
    <template #start>
      <span class="text-xl font-bold text-green-700">CleanMate</span>
    </template>
  </Menubar>
</template>

<script setup lang="ts">
import { useRouter, useRoute } from 'vue-router'
import { computed } from 'vue'
import Menubar from 'primevue/menubar'

// Simulated user logic (replace this with real auth logic)

const router = useRouter()
const route = useRoute()

// Hide navbar on the login page
const isLoginPage = computed(() => route.path === '/')

const menuItems = [
  {
    label: 'Home',
    command: () => router.push('/home'),
  },
  {
    label: 'Bookings',
    command: () => router.push('/bookings'),
  },
  {
    label: 'Favourites',
    command: () => router.push('/shortList'),
  },
  {
    label: 'Profile',
    command: () => router.push('/profile'),
  },
]
</script>
