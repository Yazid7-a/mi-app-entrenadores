// App.tsx
import * as React from 'react';
import { Provider as PaperProvider } from 'react-native-paper';
import { NavigationContainer }      from '@react-navigation/native';
import { theme }                    from './src/theme/theme';
import RootNavigator                from "./src/navigation/RootNavigator";
import { AuthProvider }             from './src/context/AuthContext';

export default function App() {
  return (
    <PaperProvider theme={theme}>
      <AuthProvider>
        <NavigationContainer>
          <RootNavigator />
        </NavigationContainer>
      </AuthProvider>
    </PaperProvider>
  );
}
