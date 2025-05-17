<template>
  <Card style="width: 300px" :style="{ opacity: category.IsActive ? 1 : 0.4 }">
    <!-- Diagonal Red Line if Inactive -->
    <template #header>
      <div class="relative"></div>
    </template>

    <template #title>
      <div class="text-xl font-semibold truncate w-full">{{ category.Title }}</div>
    </template>

    <template #content>
      <div
        class="flex flex-col items-start text-left px-4 py-2 space-y-1 text-sm text-gray-700 w-full"
      >
        <div><strong>Category:</strong> {{ category.Title }}</div>
        <div><strong>Description:</strong> {{ category.Description }}</div>
        <div><strong>Active:</strong> {{ category.IsActive ? 'Yes' : 'No' }}</div>
      </div>
    </template>

    <template #footer>
      <div class="flex justify-center">
        <Button label="Edit Category" @click="emit('edit', category.CategoryID)" />
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
  (e: 'edit', categoryID: number): void
}>()
</script>
