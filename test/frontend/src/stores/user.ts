import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import type { UserAccount } from '@/types/interfaces'

// Define the User type

// Define the store
export const useUserStore = defineStore('user', () => {
  // Auth state with types

  const userAccounts = ref<UserAccount[]>([])

  async function searchUser(searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchUser', {
        params: { searchTerm: searchTerm },
      })
      userAccounts.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function viewUser(UserID: number): Promise<UserAccount> {
    try {
      const response = await http.get('/ViewUser', {
        params: { UserID: UserID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  return { userAccounts }
})
