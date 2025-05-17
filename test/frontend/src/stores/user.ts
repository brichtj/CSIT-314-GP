import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import type {
  CreateUserType,
  CustomUserAccount,
  UpdateUserType,
  UserAccount,
} from '@/types/interfaces'

// Define the User type

// Define the store
export const useUserStore = defineStore('user', () => {
  // Auth state with types

  const userAccounts = ref<UserAccount[]>([])

  async function searchUser(searchTerm: string): Promise<boolean> {
    try {
      const response = await http.get('/SearchUserAccount', {
        params: { searchTerm: searchTerm },
      })
      userAccounts.value = response.data.message
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function viewUser(UserID: number): Promise<CustomUserAccount> {
    try {
      const response = await http.get('/ViewUser', {
        params: { UserID: UserID },
      })
      return response.data.message
    } catch (err: any) {
      throw err
    }
  }

  // Actions
  async function CreateUserAccount(details: CreateUserType): Promise<boolean> {
    try {
      const response = await http.post('/CreateUser', details)
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function updateUserAccount(details: UpdateUserType): Promise<boolean> {
    try {
      const response = await http.put('/UpdateUserAccount', details)
      return true
    } catch (err: any) {
      throw err
    }
  }

  async function suspendUser(UserProfileID: number): Promise<boolean> {
    try {
      const response = await http.put('/SuspendUser', { UserProfileID: UserProfileID })
      return true
    } catch (err: any) {
      throw err
    }
  }

  return { userAccounts, searchUser, viewUser, CreateUserAccount, updateUserAccount, suspendUser }
})
