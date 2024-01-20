<script setup>
import CircleButton from './CircleButton.vue'
defineProps(['header', 'icon'])
</script>

<template>
  <div class="button-container">
    <div class="button-header">{{ header }}</div>
    <CircleButton :icon="icon"></CircleButton>
  </div>
</template>

<style scoped>
.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.button-header {
  font-size: 11px;
  font-weight: bold;
}
</style>
