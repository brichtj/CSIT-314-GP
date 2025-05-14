import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import { type CustomMatch, type CustomService, type Service } from '@/types/interfaces'

// Define the User type

// Define the store
export const useServiceStore = defineStore('service', () => {
  // Auth state with types
  const services = ref<Service[]>([])
  const shortListedServices = ref<Service[]>([])
  const matches = ref<Service[]>([])
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

  async function viewService(serviceID: number, type: string): Promise<CustomService | null> {
    try {
      let url = ''
      if (type == 'HomeOwner') url = '/ViewServiceHomeOwner'
      if (type == 'Cleaner') url = '/ViewServiceCleaner'
      if (type == 'shortlist') url = '/ViewServiceShortlist'
      else url = '/ViewServiceCleaner'
      const response = await http.get(url, {
        params: { ServiceID: serviceID },
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
  async function viewMatch(serviceID: number): Promise<CustomMatch | null> {
    try {
      let url = '/ViewMatchHistory'
      const response = await http.get(url, {
        params: { ServiceID: serviceID },
      })
      return response.data.message
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
  }
})
