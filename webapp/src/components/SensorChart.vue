<template>
  <LineChart v-bind="lineChartProps" />
</template>

<script setup lang="ts">
  import { computed, ref, watch } from 'vue';
  import { Sensor } from '../types';
  import { LineChart, useLineChart } from 'vue-chart-3';
  import { ChartData } from 'chart.js';

  const props = defineProps<{ title: string; color: string; data: Sensor }>();

  let dataValues = ref<number[]>([]);
  let dataLabels = ref<number[]>([]);

  const data = computed<ChartData<'line'>>(() => ({
    labels: dataLabels.value,
    datasets: [
      {
        label: 'Values',
        data: dataValues.value,
        borderColor: props.color,
        fill: false,
      },
    ],
  }));

  const options = {
    scales: {
      x: {
        type: 'time',
      },
    },
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
  };

  const { lineChartProps } = useLineChart({
    chartData: data,
    options,
  });

  watch(
    () => props.data,
    (newValue: Sensor) => {
      dataLabels.value.push(newValue.timestamp);
      dataValues.value.push(newValue.value);

      if (dataLabels.value.length > 10) {
        dataLabels.value.shift();
        dataValues.value.shift();
      }
    },
  );
</script>
