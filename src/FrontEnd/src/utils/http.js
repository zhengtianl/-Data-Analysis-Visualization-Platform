import axios from 'axios'

const http = axios.create({
  baseURL: 'http://172.26.135.85:5000',
  timeout: 100000
})

// 添加响应拦截器
http.interceptors.response.use((response)=> {
    return response.data
  }, (error)=> {
    return Promise.reject(error)
})

export { http }