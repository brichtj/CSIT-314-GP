import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import 'primeicons/primeicons.css'
const app = createApp(App)

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
})
app.use(createPinia())
app.use(router)
router.beforeEach((to, from, next) => {
  const defaultTitle = 'Cleaner'
  if (typeof to.meta.title === 'string') {
    document.title = to.meta.title
  } else {
    document.title = defaultTitle
  }
  next()
})

app.mount('#app')
