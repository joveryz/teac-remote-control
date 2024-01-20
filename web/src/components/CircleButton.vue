<script setup>
defineProps({
  icon: {
    type: String,
    default: 'fa-regular fa-circle'
  }
})
</script>

<template>
  <div class="button-circle">
    <font-awesome-icon :icon="icon" />
  </div>
</template>

<style scoped>
.button-circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  border: 1px solid black;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.button-circle:hover {
  background-color: #eee;
}
</style>
