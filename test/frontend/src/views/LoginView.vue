<script setup lang="ts">
import { ref } from 'vue'
import { useAuthenticationStore } from '@/stores/authentication'
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import Card from 'primevue/card'
import Message from 'primevue/message'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const error = ref<boolean>(false)
const auth = useAuthenticationStore()

const router = useRouter()

const handleLogin = async () => {
  router.push('/home')
  try {
    const value = await auth.login(username.value, password.value)
    console.log(value)
    if (value.data.authentication) {
      //push route
      error.value = false
      errorMessage.value = ''
      router.push('/home')
    } else {
      //handle incorrect username/ password
      error.value = true
      errorMessage.value = 'Incorrect username/password'
    }
  } catch (err: unknown) {
    //handle error(network)
    error.value = true
    errorMessage.value = 'Network Error, please try again'
  }
}
</script>

<template>
  <div class="container">
    <Card class="centered-div">
      <template #title><h2>Login to Santa's helpers</h2></template>
      <template #content>
        <div class="space-y-6">
          <div>
            <label for="username" class="label">Username</label>
            <InputText
              id="username"
              v-model="username"
              class="input-field"
              placeholder="Enter username"
            />
          </div>

          <div>
            <label for="password" class="label">Password</label>
            <Password
              id="password"
              v-model="password"
              class="input-field"
              toggleMask
              :feedback="false"
              placeholder="Enter password"
            />
          </div>

          <Button label="Login" icon="pi pi-sign-in" :loading="auth.loading" class="login-btn" @click="handleLogin" />

          <Message v-if="error" severity="error" class="mt-2">
            {{ errorMessage }}
          </Message>

          <Message v-if="auth.user" severity="success" class="mt-2">
            Welcome, {{ auth.user.name }}!
          </Message>
        </div>
      </template>
    </Card>
  </div>
</template>

<style scoped>
/* Main container styling */
.container {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  height: 100vh; /* Full viewport height */
  width: 100vw;
  background: linear-gradient(145deg, #fffbf0, #ffd700); /* Light gold and cream background */
  padding: 1rem;
}

/* Card styling */
.centered-div {
  width: 100%;
  max-width: 500px; /* Width adjusted for a more compact layout */
  background-color: #fffdf7; /* Soft cream background */
  border: 2px solid #FFD700; /* Gold border */
  border-radius: 16px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  text-align: center;
}

/* Title Styling */
.title {
  font-family: 'Comic Sans MS', sans-serif; /* Fun and playful font */
  color: #e53935; /* Christmas red */
  font-size: 1.8rem; /* Larger font size */
  margin-bottom: 1.5rem; /* Space below title */
  text-align: center;
  letter-spacing: 1px; /* Slight letter spacing for a festive effect */
}

/* Label for inputs */
.label {
  font-weight: bold;
  font-size: 1rem;
  color: #212121;
  margin-bottom: 0.5rem;
}

/* Input Fields */
.input-field {
  width: 100%;
  border: 2px solid #FFD700; /* Gold border */
  border-radius: 8px;
  padding: 0.8rem;
  background-color: #fff;
  color: #212121;
  margin-bottom: 1rem;
}

.input-field:focus {
  border-color: #C62828; /* Red border on focus */
  box-shadow: 0 0 0 2px rgba(198, 40, 40, 0.2);
}

/* Button Styling */
.login-btn {
  background-color: #c62828; /* Christmas red button */
  color: #fffdf7;
  font-weight: bold;
  border-radius: 8px;
  padding: 0.8rem 1.6rem;
  transition: background-color 0.3s ease;
  margin-top: 1rem;
  width: 100%;
}

.login-btn:hover {
  background-color: #a32121; /* Darker red on hover */
}

/* Error message styling */
.error-message {
  background-color: #ffebee; /* Light red background for errors */
  color: #C62828;
  border-radius: 8px;
  padding: 0.6rem;
  font-size: 1rem;
  margin-top: 1rem;
}

/* Success message styling */
.success-message {
  background-color: #c8e6c9; /* Light green background for success */
  color: #2E7D32;
  border-radius: 8px;
  padding: 0.6rem;
  font-size: 1rem;
  margin-top: 1rem;
}

/* MEDIA QUERIES FOR RESPONSIVENESS */

/* Mobile devices (up to 600px) */
@media (max-width: 600px) {
  .centered-div {
    max-width: 90%; /* Allow the card to be more flexible on smaller screens */
    padding: 1rem; /* Reduce padding for smaller screens */
  }

  .title {
    font-size: 1.5rem; /* Slightly smaller title */
  }

  .input-field {
    padding: 0.6rem; /* Reduce input field padding */
  }

  .login-btn {
    padding: 0.7rem 1.4rem; /* Reduce button padding for small screens */
  }

  .error-message,
  .success-message {
    font-size: 0.9rem; /* Adjust font size for smaller text */
  }
}

/* Tablets (600px to 900px) */
@media (min-width: 601px) and (max-width: 900px) {
  .centered-div {
    max-width: 80%; /* Make the card a little smaller */
  }

  .title {
    font-size: 1.6rem; /* Smaller title for medium devices */
  }

  .input-field {
    padding: 0.7rem; /* Reduce padding on medium devices */
  }

  .login-btn {
    padding: 0.75rem 1.5rem; /* Slightly smaller button */
  }
}

/* Large devices (desktops) */
@media (min-width: 901px) {
  .centered-div {
    max-width: 500px; /* Keep card width fixed */
    padding: 2rem; /* Larger padding */
  }

  .title {
    font-size: 1.8rem; /* Larger title for desktops */
  }

  .input-field {
    padding: 0.8rem; /* Larger input field padding */
  }

  .login-btn {
    padding: 0.8rem 1.6rem; /* Standard button size for desktops */
  }
}
</style>
