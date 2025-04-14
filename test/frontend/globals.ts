import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:3000', // Set your API base URL here
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
})
export default http
