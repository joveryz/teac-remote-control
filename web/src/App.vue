<script setup lang="ts">
import Button from './components/Button.vue'
import CircleButton from './components/CircleButton.vue'
import { sendCommand } from './utils/utils.ts'
</script>

<template>
  <notifications />
  <main>
    <div class="controller-container">
      <div>
        <div class="black-button-header" style="grid-column-start: 1; grid-column-end: 4">UD-701N</div>
        <div class="button-grid button-central">
          <Button header="POWER" icon="fa-solid fa-power-off" @click="sendCommand('dac', 'power')"></Button>
          <Button header="DISPLAY" @click="sendCommand('dac', 'display')"></Button>
          <Button header="INFO" icon="fa-solid fa-info" @click="sendCommand('dac', 'info')"></Button>
          <div style="height: 2px; margin-bottom: 1px; background-color: black; grid-column-start: 1; grid-column-end: 4">
          </div>
          <Button header="NET" @click="sendCommand('dac', 'net')"></Button>
          <div></div>
          <Button header="LINE" @click="sendCommand('dac', 'line')"></Button>
          <Button header="COAXIAL1" @click="sendCommand('dac', 'coaxial1')"></Button>
          <div></div>
          <Button header="COAXIAL2" @click="sendCommand('dac', 'coaxial2')"></Button>
          <div style="height: 2px; margin-bottom: 1px; background-color: black; grid-column-start: 1; grid-column-end: 4">
          </div>
          <Button header="HP(6.3)." icon="fa-solid fa-headphones" @click="sendCommand('dac', 'hp63')"></Button>
          <Button header="HP(XLR4)" icon="fa-solid fa-headphones" @click="sendCommand('dac', 'hpxlr4')"></Button>
          <Button header="XLR" icon="fa-solid fa-bullhorn" @click="sendCommand('dac', 'xlr')"></Button>
          <div style="height: 2px; margin-bottom: 1px; background-color: black; grid-column-start: 1; grid-column-end: 4">
          </div>
          <Button header="MUTE" @click="sendCommand('dac', 'mute')"></Button>
          <Button header="VOLUME" icon="fa-solid fa-plus" @click="sendCommand('dac', 'volumeup')"></Button>
          <Button header="VOLUME" icon="fa-solid fa-minus" @click="sendCommand('dac', 'volumedown')"></Button>
        </div>
      </div>

      <div style="height: 10px; background-color: white"></div>
      <div>
        <div class="black-button-header" style="grid-column-start: 1; grid-column-end: 4">VRDS-701T</div>
        <div class="button-grid button-central">
          <Button header="POWER" icon="fa-solid fa-power-off" @click="sendCommand('cd', 'power')"></Button>
          <div></div>
          <Button header="OPEN" icon="fa-solid fa-eject" @click="sendCommand('cd', 'open')"></Button>
          <Button header="DISPLAY" @click="sendCommand('cd', 'display')"></Button>
          <div></div>
          <Button header="INFO" icon="fa-solid fa-info" @click="sendCommand('cd', 'info')"></Button>
          <div style="height: 2px; margin-bottom: 1px; background-color: black; grid-column-start: 1; grid-column-end: 4">
          </div>
          <Button header="PLAY" icon="fa-solid fa-play" @click="sendCommand('cd', 'play')"></Button>
          <Button header="PAUSE" icon="fa-solid fa-pause" @click="sendCommand('cd', 'pause')"></Button>
          <Button header="STOP" icon="fa-solid fa-stop" @click="sendCommand('cd', 'stop')"></Button>
          <Button header="BACKWARD" icon="fa-solid fa-backward-fast" @click="sendCommand('cd', 'backward')"></Button>
          <div></div>
          <Button header="FORWARD" icon="fa-solid fa-forward-fast" @click="sendCommand('cd', 'forward')"></Button>
        </div>
      </div>

      <div style="height: 10px; background-color: white"></div>
      <div style="text-align: center">
        <div style="display: flex; flex-direction: column;">
          <span style="font-size: 26px; font-weight: bolder; font-family: 'Times New Roman'">
            TEAC
          </span>
          <span style="font-size: 10px; font-weight: bold;">
            Reference 700
          </span>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
main {
  font-family: Arial, Helvetica, sans-serif;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.controller-container {
  padding: 10px;
  margin: 10px;
  width: 200px;
  background-color: white;
  border: 1px solid black;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.button-grid {
  display: grid;
  grid-template-columns: 60px 60px 60px;
  grid-column-gap: 2px;
  grid-row-gap: 10px;
  margin: auto;
  padding: 10px;
  align-items: center;
  border: 1px solid grey;
  border-radius: 3px;
}

.button-central>.button-circle {
  place-self: center;
}

.black-button-header {
  background-color: black;
  color: white;
  border-radius: 2px;
  text-align: center;
  font-size: 11px;
  font-weight: bold;
}

.black-button-header-bottom {
  background-color: white;
  color: black;
  border-radius: 2px;
  text-align: center;
  font-size: 16px;
  font-weight: bold;
}

.black-text {
  background-color: black;
  color: white;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
}
</style>
./components/ButtonClick./utils/CommandSender