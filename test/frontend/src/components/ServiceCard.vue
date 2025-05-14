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
      <div class="text-xl font-semibold truncate w-full">{{ service.Title }}</div>
    </template>

    <template #content>
      <div class="flex flex-col items-center">
        <div class="mt-2 text-sm text-gray-500">Posted: {{ formattedDate }}</div>
        <div class="mt-2 text-base font-semibold text-green-600">
          ${{ service.Price.toFixed(2) }}
        </div>
      </div>
    </template>
    <template #footer>
      <div style="justify-content: space-between; justify-items: center">
        <Button label="Book Now" @click="emit('book', props.service.ServiceID)" />
        <Button
          @click="
            () => {
              toggleLove()
              emit('shortList', props.service.ServiceID)
            }
          "
          :icon="loved ? 'pi pi-heart-fill' : 'pi pi-heart'"
          severity="danger"
          content="Like"
          :label="service.LikeCount.toString()"
        />
      </div>
    </template>
  </Card>
</template>

<script setup lang="ts">
import Card from 'primevue/card'
import Button from 'primevue/button'
import { computed, ref } from 'vue'
import type { Service } from '@/types/interfaces'

const props = defineProps<{ service: Service }>()

const emit = defineEmits<{
  (e: 'book', serviceID: number): void
  (e: 'shortList', serviceID: number): void
}>()

const header = `<img src="${props.service.ImageLink}" alt="Service" class='w-full h-40 object-cover' />`
const defaultImage = 'https://www.purevpn.com/wp-content/uploads/2023/03/What-is-IMGUR_.png' // 👈 Update with your actual default path
const imageSrc = ref(props.service.ImageLink)
function handleImageError(event: Event) {
  imageSrc.value = defaultImage
}

const loved = ref(false)
function toggleLove() {
  loved.value = !loved.value
}

const formattedDate = computed(() => {
  const date = new Date(props.service.DatePosted)
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
