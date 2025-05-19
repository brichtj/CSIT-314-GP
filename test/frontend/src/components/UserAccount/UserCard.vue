<template>
  <Card
    class="w-[280px] shadow-md rounded-2xl text-center flex flex-col items-center"
    style="width: 300px"
    :style="{ opacity: user.IsActive ? 1 : 0.4 }"
  >
    <template #header>
      <div class="relative"></div>
    </template>

    <template #title>
      <div class="text-xl font-semibold truncate w-full">{{ user.Username }}</div>
    </template>

    <template #content>
      <div
        class="flex flex-col items-start text-left px-4 py-2 space-y-1 text-sm text-gray-700 w-full"
      >
        <div><strong>User ID:</strong> {{ user.UserID }}</div>
        <div><strong>Email:</strong> {{ user.Email }}</div>
        <div><strong>Phone:</strong> {{ user.Phone }}</div>
        <div><strong>Active:</strong> {{ user.IsActive ? 'Yes' : 'No' }}</div>
        <div><strong>User Profile:</strong> {{ user.UserProfile }}</div>
        <div><strong>Address Provided:</strong> {{ user.Address ? 'Yes' : 'No' }}</div>
        <div><strong>Experience:</strong> {{ user.Experience ?? 'None' }}</div>
      </div>
    </template>
    <template #footer>
      <div style="justify-content: space-between; justify-items: center">
        <Button label="View Details" @click="emit('view', props.user.UserID)" />
      </div>
    </template>
  </Card>
</template>
<style scoped>
h3 {
  font-weight: 800; /* very bold */
  text-decoration: underline;
  color: #1f2937; /* Tailwind's text-gray-800 */
  margin-bottom: 0.25rem; /* similar to mb-1 */
}
</style>

<script setup lang="ts">
import Card from 'primevue/card'
import Button from 'primevue/button'
import { computed, ref } from 'vue'
import type { UserAccount } from '@/types/interfaces'
const props = defineProps<{ user: UserAccount }>()

const emit = defineEmits<{
  (e: 'view', userID: number): void
}>()
</script>

<style scoped>
/* Optional: Tailwind line-clamp plugin must be enabled or truncate manually */
/* .line-clamp-3 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
} */
</style>
