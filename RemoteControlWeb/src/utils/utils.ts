import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { notify } from '@kyvg/vue3-notification'

export const sendCommand = (device: string, command: string) => {
  axios.get(`http://127.0.0.1:8000/${device}/${command}`).then((response: any) => {
    notify({
      title: `sending command to device: ${device}--${command}`,
      type: 'success'
    })
  })
  console.log(`sending command to device: ${device}--${command}`)
}
