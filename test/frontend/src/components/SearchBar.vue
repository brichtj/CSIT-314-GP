<template>
  <div class="p-inputgroup w-full mb-4 px-4">
    <InputText
      v-model="searchText"
      placeholder="Search cleaning services..."
      class="w-full"
      @input="$emit('search', searchText)"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import InputText from 'primevue/inputtext'

const searchText = ref('')
defineEmits<{
  (e: 'search', query: string): void
}>()
</script>
