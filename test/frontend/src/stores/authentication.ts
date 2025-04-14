import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import http from '../../globals.ts' // use the global axios instance

// Define the User type
interface User {
  id: number
  name: string
}

interface AuthState {
  user: User | null
  token: string | null
  error: string | null
  loading: boolean
}

// Define the store
export const useAuthenticationStore = defineStore('authentication', () => {
  // Auth state with types
  const user = ref<User | null>(null)
  const token = ref<string | null>(null)
  const error = ref<string | null>(null)
  const loading = ref<boolean>(false)

  // Login action
  async function login(username: string, password: string): Promise<boolean | any> {
    loading.value = true
    error.value = null
    const credentials = { username: username, password: password }
    try {
      const response = await http.post('/login', credentials)
      user.value = response.data.user
      return response
    } catch (err: any) {
      throw new Error(err)
    } finally {
      loading.value = false
    }
  }

  // Logout action
  function logout(): void {
    user.value = null
    token.value = null
    error.value = null
  }

  return { user, loading, error, login, logout }
})
