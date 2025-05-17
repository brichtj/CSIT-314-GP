import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import PrimeVue from 'primevue/config'
import Aura from '@primeuix/themes/aura'
import 'primeicons/primeicons.css'
import ToastService from 'primevue/toastservice'
import Toast from 'primevue/toast'

const app = createApp(App)

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
})
app.use(createPinia())
app.use(ToastService)
app.use(router)
app.component('Toast', Toast)
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
