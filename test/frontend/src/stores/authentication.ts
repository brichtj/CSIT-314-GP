import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance
import type { User } from '@/types/interfaces'

// Define the User type

// Define the store
export const useAuthenticationStore = defineStore('authentication', () => {
  // Auth state with types
  const user = ref<User | null>({
    Address: '',
    Email: '',
    Experience: 0,
    IsActive: false,
    Phone: '',
    Privilege: '',
    UPActive: false,
    UserID: 42,
    UserProfile: 0,
    UserProfileName: 'HomeOwner',
    Username: '',
  })
  const token = ref<string | null>(null)

  // Login action
  async function login(username: string, password: string): Promise<boolean | any> {
    const credentials = { username: username, password: password }
    try {
      const response = await http.post('/login', credentials)
      //console.log('LOGIN RESPONSE:', response.data)
      user.value = response.data.message
      //console.log(user.value)
      //user.value = response.data.user
      //return response
      return true
    } catch (err: any) {
      //console.log(err.response.data.message)

      throw err
    }
  }

  // Logout action
  function logout(): void {
    user.value = null
    token.value = null
  }

  return { user, login, logout }
})
