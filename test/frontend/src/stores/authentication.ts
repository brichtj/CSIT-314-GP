import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance

// Define the User type
interface User {
  Address: string
  Email: string
  Experience: number
  IsActive: boolean
  Phone: string
  Privilege: string // narrow this union if there are other known values
  UPActive: boolean
  UserID: number
  UserProfile: number
  UserProfileName: string
  Username: string
}

// Define the store
export const useAuthenticationStore = defineStore('authentication', () => {
  // Auth state with types
  const user = ref<User | null>(null)
  const token = ref<string | null>(null)

  // Login action
  async function login(username: string, password: string): Promise<boolean | any> {
    const credentials = { username: username, password: password }
    try {
      const response = await http.post('/login', credentials)
      //console.log('LOGIN RESPONSE:', response.data)
      user.value = response.data.message
      console.log(user.value)
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
