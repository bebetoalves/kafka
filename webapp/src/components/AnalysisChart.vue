<template>
  <Line :data="data" :options="options" />
</template>

<script setup lang="ts">
  import { ref, watch } from 'vue';
  import { Analysis } from '../types';
  import { Line } from 'vue-chartjs';
  import { ChartData, ChartOptions } from 'chart.js';
  import { format } from 'date-fns';

  const props = defineProps<{ data: Analysis }>();

  const dataLabels = <number[]>[];
  const dataMinValue = <number[]>[];
  const dataMaxValue = <number[]>[];
  const dataAvgValue = <number[]>[];

  const data = ref<ChartData<'line'>>({ labels: [], datasets: [] });

  const options = <ChartOptions<'line'>>{
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Analysis',
      },
    },
    scales: {
      x: {
        type: 'time',
        time: {
          tooltipFormat: 'HH:mm:ss',
        },
        title: {
          display: true,
          text: 'Time',
        },
        ticks: {
          callback: function (value: number) {
            return format(new Date(value * 1000), 'HH:mm:ss');
          },
          autoSkip: true,
          maxTicksLimit: 20,
        },
      },
    },
  };

  watch(
    () => props.data,
    (newValue: Analysis) => {
      let removedOldData = false;

      if (dataMinValue.length >= 30) {
        dataMinValue.shift();
        dataMaxValue.shift();
        dataAvgValue.shift();
        removedOldData = true;
      }

      if (removedOldData) {
        dataLabels.shift();
      }

      dataLabels.push(newValue.timestamp);
      dataMinValue.push(newValue.min);
      dataMaxValue.push(newValue.max);
      dataAvgValue.push(newValue.avg);

      const newData = () => ({
        labels: dataLabels,
        datasets: [
          {
            label: 'Min',
            data: dataMinValue,
            borderColor: '#0ea5e9',
            fill: false,
          },
          {
            label: 'Max',
            data: dataMaxValue,
            borderColor: '#ef4444',
            fill: false,
          },
          {
            label: 'Avg',
            data: dataAvgValue,
            borderColor: '#22c55e',
            fill: false,
          },
        ],
      });

      data.value = newData();
    },
  );
</script>
