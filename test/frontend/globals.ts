import axios from 'axios'

const http = axios.create({
  baseURL: 'http://127.0.0.1:5000', // Set your API base URL here
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
})
export default http
