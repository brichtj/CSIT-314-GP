import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import {
  type CustomMatch,
  type CustomService,
  type Service,
  type SimpleMatch,
} from '@/types/interfaces'

// Define the User type

// Define the store
export const useServiceStore = defineStore('service', () => {
  // Auth state with types
  const services = ref<Service[]>([])
  const shortListedServices = ref<Service[]>([])
  const matches = ref<SimpleMatch[]>([])
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

  async function getServicesForCleaner(CleanerID: number, searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchServiceByCleanerID', {
        params: { CleanerID: CleanerID, Title: searchTerm },
      })
      services.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }
  interface LikesAndViewsResponse {
    Likes: number
    Views: number
  }
  async function getLikesAndViewsForService(ServiceID: number): Promise<LikesAndViewsResponse> {
    try {
      const totalViews = await http.get('/ViewTotalViewbyID', {
        params: { ServiceID: ServiceID },
      })
      const totalLikes = await http.get('/ViewTotalshortlistedCountbyID', {
        params: { ServiceID: ServiceID },
      })
      return {
        Likes: totalLikes.data.message,
        Views: totalViews.data.message,
      }
    } catch (err: any) {
      throw err
    }
  }
  async function viewService(
    serviceID: number,
    type: string,
    HomeOwnerID: number | null,
  ): Promise<CustomService | null> {
    try {
      let url = ''
      if (type == 'HomeOwner') url = '/ViewServiceHomeOwner'
      else if (type == 'Cleaner') url = '/ViewServiceCleaner'
      else if (type == 'shortlist') url = '/ViewServiceShortlist'
      else url = '/ViewServiceCleaner'
      const response = await http.get(url, {
        params:
          type == 'HomeOwner'
            ? { ServiceID: serviceID, HomeOwnerID: HomeOwnerID }
            : { ServiceID: serviceID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  async function confirmService(
    HomeOwnerID: number,
    ServiceID: number,
    Price: number,
  ): Promise<boolean> {
    try {
      const response = await http.post('/CreateMatch', {
        HomeOwnerID: HomeOwnerID,
        ServiceID: ServiceID,
        Price: Price,
      })
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function shortListService(serviceID: number, HomeOwnerID: number): Promise<boolean> {
    try {
      const response = await http.post('/ShortlistService', {
        HomeOwnerID: HomeOwnerID,
        serviceID: serviceID,
      })
      return true
    } catch (err: any) {
      throw err
    }
  }
  async function getShortListedService(HomeOwnerID: number, searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchShortlistForHomeOwner', {
        params: { HomeOwnerID: HomeOwnerID, Title: searchTerm },
      })
      shortListedServices.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function getMatchesHomeOwner(HomeOwnerID: number, searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchMatchHomeOwner', {
        params: { HomeOwnerID: HomeOwnerID, searchTerm: searchTerm },
      })
      matches.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }
  async function getMatchesCleaner(CleanerID: number, searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchMatchCleaner', {
        params: { CleanerID: CleanerID, searchTerm: searchTerm },
      })
      matches.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }
  async function viewMatch(matchID: number, userProfile: string): Promise<CustomMatch | null> {
    try {
      let url = ''
      if (userProfile == 'Cleaner') url = '/ViewMatchHistoryCleaner'
      else if (userProfile == 'HomeOwner') url = '/ViewMatchHistoryHomeOwner'
      const response = await http.get(url, {
        params: { MatchID: matchID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  async function viewViews(ServiceID: number): Promise<number> {
    try {
      const response = await http.get('/ViewTotalViewbyID', {
        params: { ServiceID: ServiceID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }
  async function viewShortListedCount(ServiceID: number): Promise<number> {
    try {
      const response = await http.get('/ViewTotalshortlistedCountbyID', {
        params: { ServiceID: ServiceID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }
  async function getCategories(searchTerm: string): Promise<[]> {
    try {
      const response = await http.get('/SearchCategory', {
        params: { keyword: searchTerm },
      })

      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  async function updateService(service: any): Promise<boolean> {
    try {
      const response = await http.put('/UpdateService', service)
      return response.data.success
    } catch (err: any) {
      throw err
    }
  }

  async function deleteService(ServiceID: number, CleanerID: number): Promise<boolean> {
    try {
      const response = await http.delete('/DeleteService', {
        params: { ServiceID: ServiceID, CleanerID: CleanerID },
      })
      return response.data.success
    } catch (err: any) {
      throw err
    }
  }

  async function createService(details: any): Promise<boolean> {
    try {
      const response = await http.post('/CreateService', details)
      return response.data.success
    } catch (err: any) {
      throw err
    }
  }

  return {
    services,
    getServices,
    viewService,
    confirmService,
    shortListService,
    getShortListedService,
    shortListedServices,
    getMatchesHomeOwner,
    matches,
    viewMatch,
    getMatchesCleaner,
    getServicesForCleaner,
    viewViews,
    viewShortListedCount,
    getCategories,
    updateService,
    deleteService,
    createService,
  }
})
