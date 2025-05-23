import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView,
      meta: { title: 'CleanMate' },
    },
    {
      path: '/',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/shortList',
      name: 'shortList',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ShortList.vue'),
    },
    {
      path: '/bookings',
      name: 'bookings',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/HistoryView.vue'),
    },
    {
      path: '/CleanerView',
      name: 'cleanerView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/CleanerView.vue'),
    },
    {
      path: '/UserView',
      name: 'userView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/UserAdmin/UserView.vue'),
    },
    {
      path: '/UserProfileView',
      name: 'userProfileView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/UserAdmin/UserProfileView.vue'),
    },
    {
      path: '/CategoryView',
      name: 'categoryView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Management/CategoryView.vue'),
    },
    {
      path: '/ReportsView',
      name: 'reportView',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Management/ReportsView.vue'),
    },
  ],
})

export default router
