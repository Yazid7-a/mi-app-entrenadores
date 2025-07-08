import React, { useState, useContext } from 'react';
import { View, StyleSheet }             from 'react-native';
import { TextInput, Button, Title, Snackbar } from 'react-native-paper';
import { NativeStackScreenProps }        from '@react-navigation/native-stack';
import { RootStackParamList }           from '../navigation/RootNavigator';
import { AuthContext }                  from '../context/AuthContext';

type Props = NativeStackScreenProps<RootStackParamList, 'Login'>;

export default function LoginScreen({ navigation }: Props) {
  const { login } = useContext(AuthContext);
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading]   = useState(false);
  const [error, setError]       = useState<string | null>(null);

  const handleLogin = async () => {
    setLoading(true);
    setError(null);
    try {
      await login(email, password);
      navigation.replace('Dashboard');
    } catch (err: any) {
      const msg = err.response?.data?.detail || err.message;
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Title style={styles.title}>Iniciar Sesión</Title>

      <TextInput
        label="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
        style={styles.input}
      />

      <TextInput
        label="Contraseña"
        value={password}
        onChangeText={setPassword}
        secureTextEntry
        style={styles.input}
      />

      <Button
        mode="contained"
        onPress={handleLogin}
        loading={loading}
        style={styles.button}
      >
        Entrar
      </Button>

      <Button onPress={() => navigation.navigate('Signup')}>
        ¿No tienes cuenta? Regístrate
      </Button>

      <Snackbar
        visible={!!error}
        onDismiss={() => setError(null)}
        duration={4000}
      >
        {error}
      </Snackbar>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex:1, padding:20, justifyContent:'center' },
  title:     { textAlign:'center', marginBottom:20 },
  input:     { marginBottom:16 },
  button:    { marginVertical:12 },
});
