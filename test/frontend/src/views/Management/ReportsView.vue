<template>
  <SearchBar @search="searchCategory" details="Search Category" />
  <Button
    label="Add Category"
    class="bg-blue-500 hover:bg-blue-600 text-white"
    severity="info"
    @click="handleCreateClick"
  />
  <div style="display: flex; flex-wrap: wrap; gap: 16px; /* space between cards */ padding: 16px">
    <CategoryCard
      v-for="category in categories"
      :key="category.CategoryID"
      class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      :category="category"
      @edit="handleViewClick"
      :view-only="false"
    />
  </div>
  <CategoryDetail
    ref="editCategoryPopUp"
    :category="categoryIndividual!"
    @update="handleUpdateClick"
    @suspend="handleSuspendClick"
  />
  <CreateCategory ref="createCategoryPopUp" @create="handleCreate" />
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useManagementStore } from '@/stores/management'
import {
  type CreateCategoryType,
  type UpdateCategoryType,
  type CategoryType,
} from '@/types/interfaces'
import { useToast, Button } from 'primevue'
import CategoryCard from '@/components/Category/CategoryCard.vue'
import CategoryDetail from '@/components/Category/CategoryDetail.vue'
import CreateCategory from '@/components/Category/CreateCategory.vue'
import SearchBar from '@/components/SearchBar.vue'
const toast = useToast()

const managementStore = useManagementStore()
const categories = computed(() => managementStore.categories)
const categoryIndividual = ref<CategoryType>()
const editCategoryPopUp = ref()
const createCategoryPopUp = ref()

onMounted(async () => {
  await managementStore.searchCategory(' ')
})

async function searchCategory(searchTerm: string) {
  await managementStore.searchCategory(searchTerm)
}

async function handleViewClick(categoryID: number) {
  categoryIndividual.value = await managementStore.viewCategory(categoryID)
  editCategoryPopUp.value.openPopup()
}

async function handleUpdateClick(category: UpdateCategoryType) {
  try {
    await managementStore.updateCategory(category)
    toast.add({
      severity: 'success',
      summary: 'Category Updated',
      detail: 'Category updated successfully.',
      life: 3000,
    })
    editCategoryPopUp.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error Updating Category',
      detail: err,
      life: 3000,
    })
  }
}

async function handleSuspendClick(categoryID: number) {
  try {
    await managementStore.suspendCategory(categoryID)
    toast.add({
      severity: 'success',
      summary: 'Category suspended ',
      detail: 'Category suspended successfully.',
      life: 3000,
    })
    editCategoryPopUp.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error suspending Category',
      detail: err,
      life: 3000,
    })
  }
}

function handleCreateClick() {
  createCategoryPopUp.value.openPopup()
}
async function handleCreate(details: CreateCategoryType) {
  try {
    await managementStore.CreateCategory(details)
    toast.add({
      severity: 'success',
      summary: 'Category Created',
      detail: 'Category created successfully.',
      life: 3000,
    })
    createCategoryPopUp.value.closePopup()
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error Creating Category',
      detail: err,
      life: 3000,
    })
  }
}
</script>
