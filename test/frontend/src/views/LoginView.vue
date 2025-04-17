<template>
  <div class="login-container">
    <h1>Login</h1>

    <form @submit.prevent="loginUser">
      <label for="profile">Login As:</label>
      <select v-model="profile">
        <option value="homeowner">HomeOwner</option>
        <option value="cleaner">Cleaner</option>
        <option value="admin">Admin</option>
        <option value="platform_manager">Platform Manager</option>
      </select>

      <label for="username">Username:</label>
      <input type="text" v-model="username" required />

      <label for="password">Password:</label>
      <input type="password" v-model="password" required />

      <button type="submit">Login</button>
    </form>

    <p v-if="error" style="color: red">{{ error }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const profile = ref('homeowner')  // default value
const error = ref('')
const router = useRouter()

const loginUser = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/login', {
      login_profile: profile.value,
      username: username.value,
      password: password.value
    })
    console.log('Login success:', response.data)

    localStorage.setItem('user', JSON.stringify(response.data.user))
    
    const role = response.data.user.role

if (role === 'homeowner') {
  router.push('/home')
} else if (role === 'platform_manager') {
  router.push('/platform-dashboard')
} else if (role === 'cleaner') {
  router.push('/cleaner-dashboard')
} else if (role === 'admin') {
  router.push('/admin-panel')
}
  } catch (err: any) {
    error.value = err.response?.data?.error || 'Login failed'
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}
input,
select {
  display: block;
  width: 100%;
  margin: 10px 0 20px;
  padding: 8px;
}
button {
  padding: 10px 15px;
}
</style>