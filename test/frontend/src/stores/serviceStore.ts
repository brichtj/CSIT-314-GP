import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance

// Define the User type
interface Service {
  ServiceID: number
  CategoryID: number
  Title: string
  Description: string
  DatePosted: string // or `Date` if you parse it before use
  CleanerID: number
  LikeCount: number
  ViewCount: number
  MatchCount: number
  Price: number
  ImageLink: string
}
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

  return { services, getServices }
})
