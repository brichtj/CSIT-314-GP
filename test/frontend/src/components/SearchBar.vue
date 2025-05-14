<template>
  <div class="p-inputgroup w-full mb-4 px-4">
    <InputText
      v-model="searchText"
      placeholder="Search cleaning services..."
      class="w-full"
      @keyup.enter="handleSearch"
    />
    <button @click="handleSearch" class="p-button p-component p-button-icon">
      <i class="pi pi-search"></i>
      <!-- PrimeIcons search icon -->
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import InputText from 'primevue/inputtext'

const searchText = ref('')

const handleSearch = () => {
  // Emit the search event only when the button is clicked or Enter key is pressed
  if (searchText.value.trim()) {
    emit('search', searchText.value)
  }
}
const emit = defineEmits<{
  (e: 'search', query: string): void
}>()
</script>
