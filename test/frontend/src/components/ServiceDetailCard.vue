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
        :src="service.ImageLink || placeholderImage"
        alt="Service Image"
        class="w-full h-60 object-cover rounded-md"
      />
      <h2 class="text-xl font-semibold">{{ service.Title }}</h2>
      <p class="text-gray-700">{{ service.Description }}</p>

      <div class="grid grid-cols-2 gap-4 text-sm text-gray-600">
        <div><strong>Service ID:</strong> {{ service.ServiceID }}</div>
        <div><strong>Category ID:</strong> {{ service.CategoryID }}</div>
        <div><strong>Cleaner ID:</strong> {{ service.CleanerID }}</div>
        <div><strong>Posted:</strong> {{ formattedDate }}</div>
        <div><strong>Price:</strong> ${{ service.Price.toFixed(2) }}</div>
        <div><strong>Likes:</strong> {{ service.LikeCount }}</div>
        <div><strong>Views:</strong> {{ service.ViewCount }}</div>
        <div><strong>Matches:</strong> {{ service.MatchCount }}</div>
      </div>
    </div>

    <template #footer>
      <Button label="Close" icon="pi pi-times" @click="closePopup" />
    </template>
  </Dialog>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import Dialog from 'primevue/dialog'
import Button from 'primevue/button'
import type { Service } from '@/types/interfaces'

const props = defineProps<{
  service: Service | null
}>()

const visible = ref(false)

const openPopup = () => {
  visible.value = true
}

const closePopup = () => {
  visible.value = false
}

const formattedDate = computed(() => {
  if (!props.service?.DatePosted) return ''
  return new Date(props.service.DatePosted).toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
})

const placeholderImage = 'https://via.placeholder.com/600x300?text=No+Image'

defineExpose({
  openPopup,
})
</script>
