<template>
  <Dialog
    v-model:visible="visible"
    header="Service Details"
    :modal="true"
    :closable="false"
    :style="{ width: '600px' }"
  >
    <div v-if="service" class="space-y-3">
      <img
        :src="imageSrc"
        alt="Service"
        class="mx-auto object-cover rounded-md"
        style="width: 200px; height: 200px"
        @error="handleImageError"
      />
      <h2 class="text-xl font-semibold">{{ service.Title }}</h2>
      <p class="text-gray-700">{{ service.Description }}</p>

      <!-- Service Info -->
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600 border-t pt-3">
        <div><strong>Date Posted:</strong> {{ formattedDate }}</div>
        <div><strong>Price:</strong> ${{ service.Price.toFixed(2) }}</div>
        <div><strong>Likes:</strong> {{ service.LikeCount }}</div>
      </div>

      <!-- Category Info -->
      <div class="border-t pt-3">
        <h3 class="font-extrabold underline text-gray-800 mb-1">Category Info</h3>
        <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
          <div><strong>Title:</strong> {{ service.CatTitle }}</div>
          <div class="col-span-2">
            <strong>Description:</strong>
            <p class="ml-2">{{ service.CatDesc }}</p>
          </div>
        </div>
      </div>

      <!-- Cleaner Info -->
      <div class="border-t pt-3">
        <h3 class="font-semibold text-gray-800 mb-1">Cleaner Info</h3>
        <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
          <div><strong>Name:</strong> {{ service.CleanerName }}</div>
          <div><strong>Active:</strong> {{ service.UActive ? 'Yes' : 'No' }}</div>
          <div><strong>Email:</strong> {{ service.Email }}</div>
          <div><strong>Phone:</strong> {{ service.Phone }}</div>
          <div><strong>Experience:</strong> {{ service.Experience }} years</div>
        </div>
      </div>
    </div>
    <!-- Match Info -->
    <div class="border-t pt-3">
      <h3 class="font-semibold text-gray-800 mb-1">Match Info</h3>
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div><strong>Deal Price:</strong> ${{ service?.DealPrice.toFixed(2) }}</div>
        <div>
          <strong>Deal Date:</strong>
          {{ new Date(service?.DealDate ?? Date.now()).toLocaleDateString() }}
        </div>
      </div>
    </div>

    <!-- Homeowner Info -->
    <div class="border-t pt-3">
      <h3 class="font-semibold text-gray-800 mb-1">Homeowner Info</h3>
      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div><strong>Name:</strong> {{ service?.HomeOwnerName }}</div>
        <div><strong>Address:</strong> {{ service?.Address }}</div>
      </div>
    </div>
    <template #footer>
      <div class="flex justify-between items-center w-full" v-if="!viewOnly">
        <div class="flex space-x-2">
          <Button label="Close" icon="pi pi-times" @click="closePopup" severity="warn" />
        </div>
      </div>
    </template>
  </Dialog>
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
import { ref, computed, onMounted, watchEffect } from 'vue'
import Dialog from 'primevue/dialog'
import Button from 'primevue/button'
import type { CustomMatch } from '@/types/interfaces'

const props = defineProps<{
  service: CustomMatch | null
  viewOnly: boolean
}>()
const visible = ref(false)

const offerPrice = ref<number | null>(null)
const defaultImage = 'https://www.purevpn.com/wp-content/uploads/2023/03/What-is-IMGUR_.png' // 👈 Update with your actual default path
const imageSrc = ref(props.service?.ImageLink ?? defaultImage)
function handleImageError(event: Event) {
  imageSrc.value = defaultImage
}

const openPopup = () => {
  console.log(props.service)
  visible.value = true
}

const closePopup = () => {
  visible.value = false
}
watchEffect(() => {
  imageSrc.value = props.service?.ImageLink ?? defaultImage
})
const formattedDate = computed(() => {
  if (!props.service?.DatePosted) return ''
  return new Date(props.service.DatePosted).toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
})

defineExpose({
  openPopup,
})
</script>
