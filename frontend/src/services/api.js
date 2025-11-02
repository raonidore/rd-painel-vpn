import axios from 'axios'

const api = axios.create({
  baseURL: 'http://192.168.99.3:8000' // Substitua pelo IP do seu servidor
})

export default api