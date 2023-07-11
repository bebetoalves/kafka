<template>
  <LineChart v-bind="lineChartProps" />
</template>

<script setup lang="ts">
  import { computed, ref, watch } from 'vue';
  import { Analysis } from '../types';
  import { LineChart, useLineChart } from 'vue-chart-3';
  import { ChartData } from 'chart.js';

  const props = defineProps<{ data: Analysis }>();

  const dataLabels = ref<number[]>([]);
  const dataMinValue = ref<number[]>([]);
  const dataMaxValue = ref<number[]>([]);
  const dataAvgValue = ref<number[]>([]);

  const data = computed<ChartData<'line'>>(() => ({
    labels: dataLabels.value,
    datasets: [
      {
        label: 'Min',
        data: dataMinValue.value,
        borderColor: '#0ea5e9',
        fill: false,
      },
      {
        label: 'Max',
        data: dataMaxValue.value,
        borderColor: '#ef4444',
        fill: false,
      },
      {
        label: 'Avg',
        data: dataAvgValue.value,
        borderColor: '#22c55e',
        fill: false,
      },
    ],
  }));

  const options = {
    scales: {
      x: {
        type: 'time',
        time: {
          tooltipFormat: 'HH:mm:ss',
        },
      },
    },
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
  };

  const { lineChartProps } = useLineChart({
    chartData: data,
    options,
  });

  watch(
    () => props.data,
    (newValue: Analysis) => {
      dataLabels.value.push(newValue.timestamp);
      dataMinValue.value.push(newValue.min);
      dataMaxValue.value.push(newValue.max);
      dataAvgValue.value.push(newValue.avg);

      if (dataLabels.value.length > 10) {
        dataLabels.value.shift();
        dataMinValue.value.shift();
        dataMaxValue.value.shift();
        dataAvgValue.value.shift();
      }
    },
  );
</script>
