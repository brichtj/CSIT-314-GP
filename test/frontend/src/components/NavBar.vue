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
import { useAuthenticationStore } from '@/stores/authentication'
const auth = useAuthenticationStore()
// Simulated user logic (replace this with real auth logic)

const router = useRouter()
const route = useRoute()

// Hide navbar on the login page
const isLoginPage = computed(() => route.path === '/')

// Define menu items dynamically
const menuItems = computed(() => {
  let items = []
  if (auth.user?.UserProfileName === 'HomeOwner') {
    items.push(
      ...[
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
          label: 'logout',
          command: () => {
            auth.logout()
            router.push('/')
          },
        },
      ],
    )
  } else if (auth.user?.UserProfileName === 'Cleaner') {
    items.push(
      ...[
        {
          label: 'Services',
          command: () => router.push('/CleanerView'),
        },
        {
          label: 'Bookings',
          command: () => router.push('/bookings'),
        },
        {
          label: 'logout',
          command: () => {
            auth.logout()
            router.push('/')
          },
        },
      ],
    )
  } else if (auth.user?.UserProfileName === 'UserAdmin') {
    items.push(
      ...[
        {
          label: 'User Accounts',
          command: () => router.push('/UserView'),
        },
        {
          label: 'User Profiles',
          command: () => router.push('/UserProfileView'),
        },
      ],
    )
  }

  return items
})
</script>
