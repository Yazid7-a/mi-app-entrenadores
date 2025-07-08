// src/screens/ClientsScreen.tsx
import React, { useEffect, useState, useContext } from 'react'
import { View, StyleSheet, FlatList } from 'react-native'
import { Title, List, ActivityIndicator, Text } from 'react-native-paper'
import api from '../api/axios'
import { AuthContext } from '../context/AuthContext'

type Client = {
  id: number
  email: string
  is_active: boolean
  trainer_id?: number | null
}

export default function ClientsScreen() {
  const { token } = useContext(AuthContext)
  const [clients, setClients] = useState<Client[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError]     = useState<string | null>(null)

  useEffect(() => {
    const fetchClients = async () => {
      try {
        setLoading(true)
        const resp = await api.get<Client[]>('/clients', {
          headers: { Authorization: `Bearer ${token}` }
        })
        setClients(resp.data)
      } catch (err: any) {
        setError(err.response?.data?.detail || err.message)
      } finally {
        setLoading(false)
      }
    }
    fetchClients()
  }, [token])

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator animating size="large" />
      </View>
    )
  }

  if (error) {
    return (
      <View style={styles.center}>
        <Text>Error: {error}</Text>
      </View>
    )
  }

  return (
    <View style={styles.container}>
      <Title style={styles.title}>Tus Clientes</Title>
      {clients.length === 0 ? (
        <Text style={styles.empty}>No tienes clientes aún.</Text>
      ) : (
        <FlatList
          data={clients}
          keyExtractor={(item) => item.id.toString()}
          renderItem={({ item }) => (
            <List.Item
              title={item.email}
              description={item.is_active ? 'Activo' : 'Inactivo'}
              left={props => <List.Icon {...props} icon="account" />}
            />
          )}
        />
      )}
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex:1, padding:20 },
  title:     { marginBottom:16, textAlign:'center' },
  center:    { flex:1, justifyContent:'center', alignItems:'center' },
  empty:     { textAlign:'center', marginTop:20 }
})
