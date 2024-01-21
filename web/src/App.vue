<script setup lang="ts">
import Button from './components/Button.vue'
import CircleButton from './components/CircleButton.vue'
import Display from './components/RoonDisplay.vue'
import { sendCommand } from './utils/utils.ts'
</script>

<template>
  <notifications />
  <main>
    <div class="controller-container">
      <div>
        <div class="black-control-area-header">UD-701N</div>
        <div style="height: 2px; background-color: white"></div>
        <div class="button-grid button-central">
          <Button header="POWER" icon="fa-solid fa-power-off" @click="sendCommand('dac', 'power')"></Button>
          <Button header="DISPLAY" @click="sendCommand('dac', 'display')"></Button>
          <Button header="INFO" icon="fa-solid fa-info" @click="sendCommand('dac', 'info')"></Button>
          <Button header="VOL" icon="fa-solid fa-plus" @click="sendCommand('dac', 'volumeup')"></Button>
          <Button header="VOL" icon="fa-solid fa-minus" @click="sendCommand('dac', 'volumedown')"></Button>
        </div>
        <div style="height: 2px; background-color: white"></div>
        <div class="button-grid button-central">
          <Button header="NET" @click="sendCommand('dac', 'net')"></Button>
          <Button header="LINE" @click="sendCommand('dac', 'line')"></Button>
          <Button header="COAX1" @click="sendCommand('dac', 'coaxial1')"></Button>
          <Button header="COAX2" @click="sendCommand('dac', 'coaxial2')"></Button>
          <Button header="MUTE" icon="fa-solid fa-volume-xmark" @click="sendCommand('dac', 'mute')"></Button>
        </div>
        <div style="height: 2px; background-color: white"></div>
        <div class="button-grid button-central">
          <Button header="HP(6.3)" icon="fa-solid fa-headphones" @click="sendCommand('dac', 'hp63')"></Button>
          <div></div>
          <Button header="HP(XLR4)" icon="fa-solid fa-headphones" @click="sendCommand('dac', 'hpxlr4')"></Button>
          <div></div>
          <Button header="XLR" icon="fa-solid fa-bullhorn" @click="sendCommand('dac', 'xlr')"></Button>
        </div>
      </div>

      <div style="height: 10px; background-color: white"></div>

      <div>
        <div class="black-control-area-header">VRDS-701T</div>
        <div style="height: 2px; background-color: white"></div>
        <div class="button-grid button-central">
          <Button header="POWER" icon="fa-solid fa-power-off" @click="sendCommand('cd', 'power')"></Button>
          <Button header="DISP" @click="sendCommand('cd', 'display')"></Button>
          <Button header="INFO" icon="fa-solid fa-info" @click="sendCommand('cd', 'info')"></Button>
          <div></div>
          <Button header="OPEN" icon="fa-solid fa-eject" @click="sendCommand('cd', 'open')"></Button>
        </div>
        <div style="height: 2px; background-color: white"></div>
        <div class="button-grid button-central">
          <Button header="PLAY" icon="fa-solid fa-play" @click="sendCommand('cd', 'play')"></Button>
          <Button header="PAUSE" icon="fa-solid fa-pause" @click="sendCommand('cd', 'pause')"></Button>
          <Button header="STOP" icon="fa-solid fa-stop" @click="sendCommand('cd', 'stop')"></Button>
          <Button header="BWD" icon="fa-solid fa-backward-fast" @click="sendCommand('cd', 'backward')"></Button>
          <Button header="FWD" icon="fa-solid fa-forward-fast" @click="sendCommand('cd', 'forward')"></Button>
        </div>
      </div>

      <div style="height: 10px; background-color: white"></div>

      <div>
        <div class="black-control-area-header">Roon</div>
        <div style="height: 2px; background-color: white"></div>
        <div class="display-grid">
          <Display />
        </div>
        <div style="height: 2px; background-color: white"></div>
        <div class="button-grid button-central">
          <Button header="PLAY" icon="fa-solid fa-play" @click="sendCommand('roon', 'play')"></Button>
          <Button header="PAUSE" icon="fa-solid fa-pause" @click="sendCommand('roon', 'pause')"></Button>
          <Button header="STOP" icon="fa-solid fa-stop" @click="sendCommand('roon', 'stop')"></Button>
          <Button header="BWD" icon="fa-solid fa-backward-fast" @click="sendCommand('roon', 'backward')"></Button>
          <Button header="FWD" icon="fa-solid fa-forward-fast" @click="sendCommand('roon', 'forward')"></Button>
        </div>
      </div>

      <div style="height: 10px; background-color: white"></div>

      <div class="brand-grid">
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
        <div style="text-align: center">
          <div style="display: flex; flex-direction: column;">
            <span style="font-size: 26px; font-weight: bolder; ">
              Roon
            </span>
            <span style="font-size: 10px; font-weight: bold;">
              Lifetime Sub
            </span>
          </div>
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
  background-color: white;
  border: 1px solid black;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.button-grid {
  display: grid;
  background-color: lightgrey;
  grid-template-columns: 45px 45px 45px 45px 45px;
  grid-column-gap: 2px;
  grid-row-gap: 10px;
  margin: auto;
  padding: 10px;
  align-items: center;
  border-radius: 3px;
}

.button-central>.button-circle {
  place-self: center;
}

.display-grid {
  display: grid;
  background-color: lightgrey;
  margin: auto;
  padding: 10px;
  align-items: center;
  border-radius: 3px;
  font-size: 12px;
}

.brand-grid {
  display: grid;
  grid-template-columns: 90px 90px;
  grid-column-gap: 2px;
  grid-row-gap: 10px;
  margin: auto;
  padding: 10px;
  align-items: center;
  border-radius: 3px;
}


.black-control-area-header {
  background-color: black;
  color: white;
  border-radius: 2px;
  text-align: center;
  font-size: 11px;
  font-weight: bold;
}

.black-control-area-header-bottom {
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
