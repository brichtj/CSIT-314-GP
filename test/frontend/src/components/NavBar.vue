<template>
  <Menubar :model="items" class="mb-3">
    <template #start>
      <span class="text-xl font-bold text-green-700">CleanMate</span>
    </template>
  </Menubar>
</template>

<script setup lang="ts">
import Menubar from 'primevue/menubar'

interface MenuItem {
  label: string
}

const items: MenuItem[] = [{ label: 'Home' }, { label: 'Bookings' }, { label: 'Profile' }]
</script>
