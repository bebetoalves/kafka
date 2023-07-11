<template>
  <Line :data="data" :options="options" />
</template>

<script setup lang="ts">
  import { ref, watch } from 'vue';
  import { Line } from 'vue-chartjs';
  import { ChartData, ChartOptions } from 'chart.js';
  import { Sensor } from '../types';
  import { format } from 'date-fns';

  const props = defineProps<{ title: string; color: string; data: Sensor }>();

  let dataValues = <number[]>[];
  let dataLabels = <number[]>[];

  const data = ref<ChartData<'line'>>({ datasets: [] });

  const options = <ChartOptions<'line'>>{
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: props.title,
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
        },
      },
    },
  };

  watch(
    () => props.data,
    (newValue: Sensor) => {
      let removedOldData = false;

      if (dataValues.length >= 10) {
        dataValues.shift();
        removedOldData = true;
      }

      if (removedOldData) {
        dataLabels.shift();
      }

      dataLabels.push(newValue.timestamp);
      dataValues.push(newValue.value);

      const newData = () => ({
        labels: dataLabels,
        datasets: [
          {
            label: 'Values',
            data: dataValues,
            borderColor: props.color,
          },
        ],
      });

      data.value = newData();
    },
  );
</script>
