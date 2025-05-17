<template>
  <Card
    class="w-[280px] shadow-md rounded-2xl text-center flex flex-col items-center"
    style="width: 300px"
  >
    <template #header>
      <div class="relative"></div>
    </template>

    <template #title>
      <div class="text-xl font-semibold truncate w-full">{{ category.Name }}</div>
    </template>

    <template #content>
      <div
        class="flex flex-col items-start text-left px-4 py-2 space-y-1 text-sm text-gray-700 w-full"
      >
        <div><strong>Profile ID:</strong> {{ category.UserProfileID }}</div>
        <div><strong>Privilege:</strong> {{ category.Privilege }}</div>
        <div><strong>Active:</strong> {{ category.Is_Active ? 'Yes' : 'No' }}</div>
      </div>
    </template>

    <template #footer>
      <div class="flex justify-center">
        <Button label="Edit Profile" @click="emit('edit', category.UserProfileID)" />
      </div>
    </template>
  </Card>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'
import type { CategoryType, UserProfile } from '@/types/interfaces'
import { Card, Button } from 'primevue'

const props = defineProps<{ category: CategoryType }>()

const emit = defineEmits<{
  (e: 'edit', userID: number): void
}>()
</script>
