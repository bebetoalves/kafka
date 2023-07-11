import { reactive } from 'vue';
import { io } from 'socket.io-client';
import { Sensor, Analysis } from './types';

export const state = reactive<{
  heat: Sensor;
  humidity: Sensor;
  analysis: Analysis;
}>({
  heat: {} as Sensor,
  humidity: {} as Sensor,
  analysis: {} as Analysis,
});

export const socket = io('http://localhost:8000');

socket.on('push', (data: Sensor & Analysis) => {
  if (data.name === 'analysis') {
    state.analysis = data;
  } else if (data.name === 'heat') {
    state.heat = data;
  } else {
    state.humidity = data;
  }
});
