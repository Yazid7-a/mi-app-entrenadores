// src/navigation/RootNavigator.tsx
import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'

import LoginScreen from '../screens/LoginScreen'
import SignupScreen from '../screens/SignupScreen'
import DashboardScreen from '../screens/dashboardscreen'
import InviteScreen from '../screens/invitationscreen'
import ClientsScreen from '../screens/ClientsScreen'

export type RootStackParamList = {
  Login: undefined
  Signup: undefined
  Dashboard: undefined
  Invite: undefined
  Clients: undefined
}

const Stack = createNativeStackNavigator<RootStackParamList>()

export default function RootNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login"    component={LoginScreen}    />
        <Stack.Screen name="Signup"   component={SignupScreen}   />
        <Stack.Screen name="Dashboard"component={DashboardScreen}/>
        <Stack.Screen name="Invite"   component={InviteScreen}   />
        <Stack.Screen name="Clients"  component={ClientsScreen}  />
      </Stack.Navigator>
    </NavigationContainer>
  )
}
