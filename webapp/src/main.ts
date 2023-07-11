import { createApp } from 'vue';
import App from './App.vue';
import { Chart, registerables } from 'chart.js';
import './style.css';
import 'chartjs-adapter-date-fns';

Chart.register(...registerables);

createApp(App).mount('#app');
