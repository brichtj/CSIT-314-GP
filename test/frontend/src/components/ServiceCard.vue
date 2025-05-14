<template>
  <Card :header="header" class="w-20rem shadow-2">
    <template #title>{{ service.name }}</template>
    <template #content>
      <p>{{ service.description }}</p>
    </template>
    <template #footer>
      <Button label="Book Now" icon="pi pi-check" @click="emit('book', service)" />
    </template>
  </Card>
</template>

<script setup lang="ts">
import Card from 'primevue/card'
import Button from 'primevue/button'

interface Service {
  id: number
  name: string
  description: string
  image: string
}

const props = defineProps<{ service: Service }>()
const emit = defineEmits<{
  (e: 'book', service: Service): void
}>()

const header = `<img src="${props.service.image}" alt="Service" class="w-full h-10rem object-cover" />`
</script>
