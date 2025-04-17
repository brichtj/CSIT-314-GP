<template>
    <div class="dashboard">
      <h1>Welcome, Platform Manager!</h1>
      <p>You are logged in as <strong>{{ user.username }}</strong>.</p>
      <button @click="logout">Logout</button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { useRouter } from 'vue-router'
  import { ref } from 'vue'
  
  const router = useRouter()
  const user = ref(JSON.parse(localStorage.getItem('user') || '{}'))
  
  const logout = () => {
    localStorage.removeItem('user')
    router.push('/login')
  }
  </script>
  
  <style scoped>
  .dashboard {
    text-align: center;
    padding: 2rem;
  }
  button {
    padding: 10px 15px;
    margin-top: 20px;
  }
  </style>