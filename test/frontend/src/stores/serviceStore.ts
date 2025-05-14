import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import type { Service } from '@/types/interfaces'

// Define the User type

// Define the store
export const useServiceStore = defineStore('service', () => {
  // Auth state with types
  const services = ref<Service[]>([])
  //get services
  async function getServices(mode: number, searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchService', {
        params: { mode: mode, searchTerm: searchTerm },
      })
      services.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function viewService(serviceID: number): Promise<Service | null> {
    try {
      const response = await http.get('/ViewServiceHomeOwner', {
        params: { ServiceID: serviceID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  return { services, getServices, viewService }
})
