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
        <div class="button-grid">
          <Button header="STANDBY/ON" icon="fa-solid fa-power-off" @click="sendCommand('cd', 'power')"></Button>
          <div></div>
          <Button header="OPEN/CLOSE" icon="fa-solid fa-eject" @click="sendCommand('cd', 'open')"></Button>
          <Button header="SOURCE" @click="sendCommand('cd', 'source')"></Button>
          <Button header="DISPLAY" @click="sendCommand('cd', 'display')"></Button>
          <Button header="DIMMER" @click="sendCommand('cd', 'dimmer')"></Button>
          <Button header="FILTER" @click="sendCommand('cd', 'filter')"></Button>
          <Button header="UPCONVERT" @click="sendCommand('cd', 'upconvert')"></Button>
          <Button header="INFO" @click="sendCommand('cd', 'info')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
        <div class="button-grid button-central">
          <Button header="&nbsp" icon="fa-solid fa-1" @click="sendCommand('cd', 'num1')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-2" @click="sendCommand('cd', 'num2')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-3" @click="sendCommand('cd', 'num3')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-4" @click="sendCommand('cd', 'num4')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-5" @click="sendCommand('cd', 'num5')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-6" @click="sendCommand('cd', 'num6')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-7" @click="sendCommand('cd', 'num7')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-8" @click="sendCommand('cd', 'num8')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-9" @click="sendCommand('cd', 'num9')"></Button>
          <Button header="PLUS10" icon="fa-solid fa-plus" @click="sendCommand('cd', 'numplus10')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-0" @click="sendCommand('cd', 'num0')"></Button>
          <Button header="CLEAR" @click="sendCommand('cd', 'clear')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
        <div class="button-grid">
          <Button header="&nbsp" icon="fa-solid fa-repeat" @click="sendCommand('cd', 'repeat')"></Button>
          <Button header="PLAYMODE" @click="sendCommand('cd', 'playmode')"></Button>
          <Button header="MENU" @click="sendCommand('cd', 'menu')"></Button>
          <div></div>
          <Button header="&#8744" icon="fa-solid fa-backward-fast" @click="sendCommand('cd', 'backward')"></Button>
          <Button header="&#8743" icon="fa-solid fa-forward-fast" @click="sendCommand('cd', 'next')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-stop" @click="sendCommand('cd', 'stop')"></Button>
          <Button header="ENTER" icon="fa-solid fa-pause" @click="sendCommand('cd', 'pause')"></Button>
          <Button header="ENTER" icon="fa-solid fa-play" @click="sendCommand('cd', 'play')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
        <div class="button-grid">
          <Button header="OUTPUT" @click="sendCommand('cd', 'output')"></Button>
          <div></div>
          <Button header="VOLUME" icon="fa-solid fa-plus" @click="sendCommand('cd', 'volumeup')"></Button>
          <Button header="MUTE" @click="sendCommand('cd', 'mute')"></Button>
          <div></div>
          <Button header="&nbsp" icon="fa-solid fa-minus" @click="sendCommand('cd', 'volumedown')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
      </div>
      <div style="text-align: center">
        <div style="display: flex; flex-direction: column;">
          <span style="font-size: 26px; font-weight: bolder; font-family: 'Times New Roman'">
            TEAC
          </span>
          <span style="font-size: 10px; font-weight: bold;">
            VRDS-701T
          </span>
        </div>
      </div>
    </div>
    <div class="controller-container">
      <div>
        <div class="button-grid">
          <Button header="STANDBY/ON" icon="fa-solid fa-power-off" @click="sendCommand('dac', 'power')"></Button>
          <div></div>
          <Button header="DIMMER" @click="sendCommand('dac', 'dimmer')"></Button>
        </div>
        <div class="button-grid button-central">
          <div class="black-button-header">NET</div>
          <div class="black-button-header">LINE</div>
          <div class="black-button-header">Bluetooth</div>
          <CircleButton @click="sendCommand('dac', 'net')"></CircleButton>
          <CircleButton @click="sendCommand('dac', 'line')"></CircleButton>
          <CircleButton icon="fa-brands fa-bluetooth" @click="sendCommand('dac', 'bluetooth')"></CircleButton>
          <div class="black-button-header" style="grid-column-start: 1; grid-column-end: 3">OPTICAL</div>
          <div class="black-button-header">USB</div>
          <CircleButton icon="fa-solid fa-1" @click="sendCommand('dac', 'optical1')"></CircleButton>
          <CircleButton icon="fa-solid fa-2" @click="sendCommand('dac', 'optical2')"></CircleButton>
          <CircleButton @click="sendCommand('dac', 'usb')"></CircleButton>
          <div class="black-button-header" style="grid-column-start: 1; grid-column-end: 3">COAXIAL</div>
          <div></div>
          <CircleButton icon="fa-solid fa-1" @click="sendCommand('dac', 'coaxial1')"></CircleButton>
          <CircleButton icon="fa-solid fa-2" @click="sendCommand('dac', 'coaxial2')"></CircleButton>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
        <div class="button-grid">
          <Button header="HP(6.3)." @click="sendCommand('dac', 'hp63')"></Button>
          <Button header="HP(XLR4)" @click="sendCommand('dac', 'hpxlr4')"></Button>
          <Button header="XLR" @click="sendCommand('dac', 'xlr')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
        <div class="button-grid">
          <Button header="INFO" @click="sendCommand('dac', 'info')"></Button>
          <div></div>
          <Button header="DISPLAY" @click="sendCommand('dac', 'display')"></Button>
          <Button header="UPCONVERT" @click="sendCommand('dac', 'upconvert')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-chevron-up" @click="sendCommand('dac', 'up')"></Button>
          <Button header="MENU" @click="sendCommand('dac', 'menu')"></Button>
          <Button header="FILTER" @click="sendCommand('dac', 'filter')"></Button>
          <Button header="&nbsp" icon="fa-solid fa-chevron-down" @click="sendCommand('dac', 'down')"></Button>
          <Button header="ENTER" @click="sendCommand('dac', 'enter')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
        <div class="button-grid">
          <div></div>
          <div></div>
          <Button header="VOLUME" icon="fa-solid fa-plus" @click="sendCommand('dac', 'volumeup')"></Button>
          <Button header="MUTE" @click="sendCommand('dac', 'mute')"></Button>
          <div></div>
          <Button header="&nbsp" icon="fa-solid fa-minus" @click="sendCommand('dac', 'volumedown')"></Button>
        </div>
        <div style="height: 2px; margin-bottom: 1px; background-color: black"></div>
        <div style="height: 1px; background-color: black"></div>
      </div>
      <div style="text-align: center">
        <div style="display: flex; flex-direction: column;">
          <span style="font-size: 26px; font-weight: bolder; font-family: 'Times New Roman'">
            TEAC
          </span>
          <span style="font-size: 10px; font-weight: bold;">
            UD-701N
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
  height: 850px;
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