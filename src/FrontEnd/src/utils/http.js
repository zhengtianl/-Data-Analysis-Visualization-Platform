import axios from 'axios'

const http = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  timeout: 100000
})

// 添加响应拦截器
http.interceptors.response.use((response)=> {
    return response.data
  }, (error)=> {
    return Promise.reject(error)
})

export { http }