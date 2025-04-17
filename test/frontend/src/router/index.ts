import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import PlatformDashboard from '../views/PlatformDashboard.vue'

// Optional placeholders for future roles
const CleanerDashboard = { template: '<div><h1>Cleaner Dashboard</h1></div>' }
const AdminPanel = { template: '<div><h1>Admin Panel</h1></div>' }

const routes = [
  {
    path: '/',
    redirect: '/login' // Optional: force all to login by default
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/platform-dashboard',
    name: 'platform-dashboard',
    component: PlatformDashboard
  },
  {
    path: '/cleaner-dashboard',
    name: 'cleaner-dashboard',
    component: CleanerDashboard
  },
  {
    path: '/admin-panel',
    name: 'admin-panel',
    component: AdminPanel
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router