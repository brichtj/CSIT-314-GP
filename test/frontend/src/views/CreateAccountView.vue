<template>
  <div class="max-w-md mx-auto mt-10 p-4 border rounded">
    <h1 class="text-xl font-bold mb-4">Create Account</h1>
    <form @submit.prevent="submitForm">
      <input v-model="form.username" type="text" placeholder="Username" class="input" required />

      <select v-model="form.userProfile" class="input" required @change="handleProfileChange">
        <option disabled value="">Select Role</option>
        <option value="HomeOwner">Homeowner</option>
        <option value="Cleaner">Cleaner</option>
        <option value="UserAdmin">User Admin</option>
        <option value="PlatformManager">Platform Manager</option>
      </select>

      <input v-model="form.email" type="email" placeholder="Email" class="input" required />
      <input v-model="form.phone" type="text" placeholder="Phone Number" class="input" required />
      <input
        v-model="form.address"
        type="text"
        placeholder="Address"
        class="input"
        :disabled="form.userProfile !== 'HomeOwner'"
      />
      <input
        v-model="form.experience"
        type="text"
        placeholder="Experience"
        class="input"
        :disabled="form.userProfile !== 'Cleaner'"
      />

      <input v-model="form.password" type="password" placeholder="Password" class="input" required />

      <button type="submit" class="btn">Create</button>
    </form>

    <p v-if="message" class="mt-4">{{ message }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import http from '../../globals'

const form = ref({
  username: '',
  password: '',
  userProfile: '',
  email: '',
  phone: '',
  address: '',
  experience: ''
})

const message = ref('')

const handleProfileChange = () => {
  if (form.value.userProfile !== 'HomeOwner') form.value.address = ''
  if (form.value.userProfile !== 'Cleaner') form.value.experience = ''
}

const submitForm = async () => {
  try {
    let url = ''
    let payload = {}

    if (form.value.userProfile === 'HomeOwner') {
      url = '/CreateHomeOwnerAccount'
      payload = {
        username: form.value.username,
        password: form.value.password,
        email: form.value.email,
        phone: form.value.phone,
        address: form.value.address
      }
    } else if (form.value.userProfile === 'Cleaner') {
      url = '/CreateCleanerAccount'
      payload = {
        username: form.value.username,
        password: form.value.password,
        email: form.value.email,
        phone: form.value.phone,
        experience: form.value.experience
      }
    } else {
      message.value = 'Only Cleaner or HomeOwner registration is supported for now.'
      return
    }

    const response = await http.post(url, payload)
    message.value = response.data.message
  } catch (error) {
    message.value = error?.response?.data?.message || 'Registration failed'
  }
}
</script>

<style scoped>
.input {
  display: block;
  margin-bottom: 1rem;
  padding: 0.5rem;
  width: 100%;
  border: 1px solid #ccc;
  border-radius: 0.375rem;
}
.btn {
  padding: 0.5rem 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
}
</style>
