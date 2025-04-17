<template>
  <div class="home">
    <h1>Welcome, {{ roleDisplayName }}!</h1>
    <p>You are logged in as <strong>{{ user.username }}</strong>.</p>
    <button @click="logout">Logout</button>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const router = useRouter()
const user = ref(JSON.parse(localStorage.getItem('user') || '{}'))

const roleMap: Record<string, string> = {
  homeowner: "HomeOwner",
  platform_manager: "Platform Manager",
  cleaner: "Cleaner",
  admin: "Admin"
}

const roleDisplayName = roleMap[user.value.role] || 'User'

const logout = () => {
  localStorage.removeItem('user')
  router.push('/login')
}
</script>

<style scoped>
.home {
  text-align: center;
  padding: 2rem;
}
button {
  padding: 10px 15px;
  margin-top: 20px;
}
</style>