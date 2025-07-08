import React, { createContext, useState, useEffect, ReactNode } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import api from '../api/axios';

type AuthContextType = {
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  signup: (email: string, password: string, code: string) => Promise<void>;
};

export const AuthContext = createContext<AuthContextType>({
  token: null,
  login: async () => {},
  logout: async () => {},
  signup: async () => {},
});

export function AuthProvider({ children }: { children: ReactNode }) {
  const [token, setToken] = useState<string | null>(null);

  // Cargar token al inicio
  useEffect(() => {
    AsyncStorage.getItem('token').then(t => {
      if (t) {
        setToken(t);
        api.defaults.headers.common['Authorization'] = `Bearer ${t}`;
      }
    });
  }, []);

  const login = async (email: string, password: string) => {
    const { data } = await api.post('/auth/login', { email, password });
    const t = data.access_token as string;
    await AsyncStorage.setItem('token', t);
    api.defaults.headers.common['Authorization'] = `Bearer ${t}`;
    setToken(t);
  };

  const logout = async () => {
    await AsyncStorage.removeItem('token');
    delete api.defaults.headers.common['Authorization'];
    setToken(null);
  };

  const signup = async (email: string, password: string, code: string) => {
    // Crear usuario
    const { data: user } = await api.post('/auth/signup', {
      email,
      password,
      role: 'client'
    });
    // Usar la invitación
    await api.post(`/invitations/use/${code}`, null, {
      params: { client_id: (user as any).id },
    });
  };

  return (
    <AuthContext.Provider value={{ token, login, logout, signup }}>
      {children}
    </AuthContext.Provider>
  );
}
