import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { notify } from '@kyvg/vue3-notification'

export const sendCommand = (device: string, command: string) => {
  console.log(`sending command to device: ${device}-${command}`)
  axios
    .get(`http://sfp.sys.ink:82/${device}/${command}`)
    .then(() => {
      notify({
        title: `${device}: ${command}`,
        type: 'success'
      })
    })
    .catch((exception) => {
      notify({
        title: `${device}: ${command}`,
        text: `${exception}`,
        type: 'error'
      })
    })
}
