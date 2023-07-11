<template>
  <main class="flex flex-col mb-10">
    <div class="bg-blue-900 py-4 border-b-2 border-yellow-500 shadow-md">
      <div class="px-4 container mx-auto">
        <h3 class="text-white font-display font-bold text-2xl">WebApp</h3>
      </div>
    </div>

    <section class="container mx-auto p-4">
      <div class="grid grid-cols-2 grid-rows-1 gap-4">
        <div class="bg-white p-4 rounded-lg shadow">
          <SensorChart title="Heat Sensor" color="#f43f5e" :data="state.heat" />
        </div>
        <div class="bg-white p-4 rounded-lg shadow">
          <SensorChart title="Humidity Sensor" color="#6366f1" :data="state.humidity" />
        </div>
        <div class="col-span-2 bg-white p-4 rounded-lg shadow">
          <AnalysisChart :data="state.analysis" />
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
  import { state } from './socket';
  import SensorChart from './components/SensorChart.vue';
  import AnalysisChart from './components/AnalysisChart.vue';
</script>
