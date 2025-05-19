<template>
  <Card
    class="w-[280px] shadow-md rounded-2xl text-center flex flex-col items-center"
    style="width: 300px"
  >
    <template #header>
      <div class="relative">
        <img
          :src="imageSrc"
          alt="Service"
          class="mx-auto object-cover rounded-md"
          style="width: 200px; height: 200px"
          @error="handleImageError"
        />
      </div>
    </template>

    <template #title>
      <div class="text-xl font-semibold truncate w-full">{{ match.Title }}</div>
    </template>

    <template #content>
      <div class="flex flex-col items-center">
        <div class="mt-2 text-sm text-gray-500">Confirmed on: {{ formattedDate }}</div>
        <div class="mt-2 text-base font-semibold text-green-600">
          Deal: ${{ match.DealPrice.toFixed(2) }}
        </div>
      </div>
    </template>
    <template #footer>
      <div style="justify-content: space-between; justify-items: center">
        <Button label="View Details" @click="emit('view', props.match.MatchID)" />
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
import type { SimpleMatch } from '@/types/interfaces'

const props = defineProps<{ match: SimpleMatch }>()

const emit = defineEmits<{
  (e: 'view', matchID: number): void
}>()

const defaultImage = 'https://www.purevpn.com/wp-content/uploads/2023/03/What-is-IMGUR_.png' // 👈 Update with your actual default path
const imageSrc = ref(props.match.ImageLink)
function handleImageError(event: Event) {
  imageSrc.value = defaultImage
}

const loved = ref(false)
function toggleLove() {
  loved.value = !loved.value
}

const formattedDate = computed(() => {
  const date = new Date(props.match.DealDate)
  return date.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
  })
})
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
