// src/screens/DashboardScreen.tsx
import React from 'react'
import { View, StyleSheet } from 'react-native'
import { Title, Button } from 'react-native-paper'
import { NativeStackScreenProps } from '@react-navigation/native-stack'
import { RootStackParamList } from '../navigation/RootNavigator'

type Props = NativeStackScreenProps<RootStackParamList,'Dashboard'>

export default function DashboardScreen({ navigation }: Props) {
  return (
    <View style={styles.container}>
      <Title style={styles.title}>Panel Principal</Title>
      <Button
        mode="contained"
        style={styles.button}
        onPress={() => navigation.navigate('Invite')}
      >
        Administrar Invitaciones
      </Button>
      <Button
        mode="contained"
        style={styles.button}
        onPress={() => navigation.navigate('Clients')}
      >
        Ver Clientes
      </Button>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex:1, justifyContent:'center', padding:20 },
  title:     { textAlign:'center', marginBottom:24 },
  button:    { marginVertical:8 }
})
