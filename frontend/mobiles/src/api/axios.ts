// src/api/axios.ts
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const API_HOST = '192.168.1.16';    
const API_PORT = '8000';

const api = axios.create({
  baseURL: `http://${API_HOST}:${API_PORT}`,
  timeout: 5000,
});

// Interceptor para inyectar el token en cada petición
api.interceptors.request.use(async config => {
  const token = await AsyncStorage.getItem('token');
  if (token) {
    config.headers = config.headers || {};
    config.headers['Authorization'] = `Bearer ${token}`;
  }
  return config;
});

export default api;
