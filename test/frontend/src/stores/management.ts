import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import type { CategoryType, CreateCategoryType, UpdateCategoryType } from '@/types/interfaces.ts'

// Define the User type

// Define the store
export const useManagementStore = defineStore('management', () => {
  // Auth state with types

  const categories = ref<CategoryType[]>([])

  async function searchCategory(searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchCategory', {
        params: { keyword: searchTerm },
      })
      categories.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function viewCategory(CategoryID: number): Promise<CategoryType> {
    try {
      const response = await http.get('/ViewCategory', {
        params: { CategoryID: CategoryID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  // Actions
  async function CreateCategory(details: CreateCategoryType): Promise<boolean> {
    try {
      const response = await http.post('/CreateCategory', details)
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function updateCategory(details: UpdateCategoryType): Promise<boolean> {
    try {
      const response = await http.put('/UpdateCategory', details)
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function suspendCategory(CategoryID: number): Promise<boolean> {
    try {
      const response = await http.put('/SuspendCategory', { UserProfileID: CategoryID })
      return true
    } catch (err: any) {
      throw err
    }
  }
  return {
    categories,
    searchCategory,
    viewCategory,
    CreateCategory,
    updateCategory,
    suspendCategory,
  }
})
