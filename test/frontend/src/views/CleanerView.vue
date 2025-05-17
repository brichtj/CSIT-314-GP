<template>
  <div>
    <SearchBar @search="searchServices" details="Search your services" />

    <Button
      label="Add"
      class="bg-blue-500 hover:bg-blue-600 text-white"
      severity="info"
      @click="handleAddClick"
    />

    <div class="p-grid p-justify-start p-px-4">
      <div
        v-for="service in services"
        :key="service.ServiceID"
        class="p-col-12 p-md-4 p-lg-3 p-mb-3"
      >
        <ServiceCard :service="service" @book="handleViewClick" :view-only="true" />
      </div>
    </div>
    <CleanerServiceDetailcard
      ref="editServicePopUp"
      :service="service"
      @update="handleUpdateClick"
      @delete="handleDeleteClick"
      :view-only="false"
      :actual-likes="actualLikes"
      :actual-views="actualViews"
      :categories="categories"
    />
    <CreateService ref="createServicePopUp" @create="handleCreateClick" :categories="categories">
    </CreateService>
  </div>
  <Toast />
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import Navbar from '../components/NavBar.vue'
import SearchBar from '../components/SearchBar.vue'
import ServiceCard from '../components/ServiceCard.vue'
import { useServiceStore } from '@/stores/serviceStore'
import CleanerServiceDetailcard from '@/components/CleanerServiceDetailcard.vue'
import type { CustomService } from '@/types/interfaces'
import { useAuthenticationStore } from '@/stores/authentication'
import Button from 'primevue/button'
import { useToast } from 'primevue/usetoast'
import CreateService from '@/components/CreateService.vue'
//serviceStore
const serviceStore = useServiceStore()
const authStore = useAuthenticationStore()

const toast = useToast()
const services = computed(() => serviceStore.services)
onMounted(() => {
  serviceStore.getServicesForCleaner(authStore.user?.UserID ?? 1, ' ')
})
async function searchServices(query: string) {
  await serviceStore.getServicesForCleaner(authStore.user?.UserID ?? 1, query)
  //do loading and stuff here
}

const createServicePopUp = ref()
const editServicePopUp = ref()
const service = ref<CustomService | null>(null)
const actualLikes = ref(0)
const actualViews = ref(0)
const categories = ref([])
async function handleViewClick(serviceID: number) {
  try {
    actualViews.value = await serviceStore.viewViews(serviceID)
    actualLikes.value = await serviceStore.viewShortListedCount(serviceID)
    categories.value = await serviceStore.getCategories(' ')
    service.value = await serviceStore.viewService(
      serviceID,
      'HomeOwner',
      authStore.user?.UserID ?? 1,
    )
    editServicePopUp.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
async function handleUpdateClick(details: any) {
  try {
    if (authStore.user?.Username.length ?? 0 > 0) {
      let result = await serviceStore.updateService(details)
      if (result) {
        toast.add({
          severity: 'success',
          summary: 'Saved',
          detail: 'Service saved successfully',
          life: 3000,
        })
        editServicePopUp.value.closePopup()
      } else
        toast.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Failed to update',
          life: 3000,
        })
    } else throw 'Please login to update a service'
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: err,
      life: 3000,
    })
  }
}

async function handleAddClick() {
  try {
    categories.value = await serviceStore.getCategories(' ')
    createServicePopUp.value.openPopup()
  } catch (err) {
    console.log(err)
  }
}
async function handleDeleteClick(serviceID: number) {
  try {
    if (authStore.user?.Username.length ?? 0 > 0) {
      await serviceStore.deleteService(serviceID, authStore.user!.UserID)
      toast.add({
        severity: 'success',
        summary: 'Deleted',
        detail: 'Service deleted successfully',
        life: 3000,
      })
      editServicePopUp.value.closePopup()
    } else {
      throw 'Please login to delete a service'
    }
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: err,
      life: 3000,
    })
  }
}

async function handleCreateClick(details: any) {
  try {
    if ((authStore.user?.UserID ?? 0 > 0) && authStore.user?.UserID) {
      details.CleanerID = authStore.user.UserID
      let result = await serviceStore.createService(details)
      if (result) {
        toast.add({
          severity: 'success',
          summary: 'Saved',
          detail: 'Service saved successfully',
          life: 3000,
        })
        createServicePopUp.value.closePopup()
      } else
        toast.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Failed to create',
          life: 3000,
        })
    } else throw 'Please login to create a service'
  } catch (err) {
    toast.add({
      severity: 'error',
      summary: 'Error',
      detail: err,
      life: 3000,
    })
  }
}
</script>
