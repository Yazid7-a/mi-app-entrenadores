import React, { useState, useEffect } from 'react';
import { View, StyleSheet, FlatList } from 'react-native';
import { Title, Button, Card, Paragraph } from 'react-native-paper';
import axios from 'axios';
import { NativeStackScreenProps } from '@react-navigation/native-stack';
import { RootStackParamList } from '../navigation/RootNavigator';

type Props = NativeStackScreenProps<RootStackParamList, 'Invite'>;

interface Invitation {
  code: string;
  trainer_id: number;
  used: boolean;
  expires_at: string | null;
}

export default function InvitationScreen({ navigation }: Props) {
  const [invitations, setInvitations] = useState<Invitation[]>([]);
  const [loading, setLoading] = useState(false);

  const fetchInvitations = async () => {
    try {
      const { data } = await axios.get<Invitation[]>(
        'http://10.0.2.2:8000/invitations'
      );
      setInvitations(data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreate = async () => {
    setLoading(true);
    try {
      const { data } = await axios.post<Invitation>(
        'http://10.0.2.2:8000/invitations',
        { trainer_id: 1 } // TODO: sustituir 1 por el ID real del trainer
      );
      setInvitations(prev => [data, ...prev]);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchInvitations();
  }, []);

  return (
    <View style={styles.container}>
      <Title>Tus Invitaciones</Title>
      <Button
        mode="contained"
        onPress={handleCreate}
        loading={loading}
        style={styles.button}
      >
        Crear nueva invitación
      </Button>

      <FlatList
        data={invitations}
        keyExtractor={item => item.code}
        renderItem={({ item }) => (
          <Card style={styles.card}>
            <Card.Content>
              <Paragraph>Código: {item.code}</Paragraph>
              <Paragraph>Usada: {item.used ? 'Sí' : 'No'}</Paragraph>
              <Paragraph>
                Expira: {item.expires_at ?? 'Nunca'}
              </Paragraph>
            </Card.Content>
          </Card>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20 },
  button: { marginVertical: 12 },
  card: { marginBottom: 12 },
});
