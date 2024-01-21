import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { notify } from '@kyvg/vue3-notification'

export const sendCommand = async (
  device: string,
  command: string,
  enableNotify: boolean = true
) => {
  console.log(`sending command to device: ${device}-${command}`)
  return await axios
    .get(`http://sfp.sys.ink:82/${device}/${command}`)
    .then((response: any) => {
      if (enableNotify) {
        notify({
          title: `${device}: ${command}`,
          type: 'success'
        })
      }
      return response.data
    })
    .catch((exception) => {
      notify({
        title: `${device}: ${command}`,
        text: `${exception}`,
        type: 'error'
      })
    })
}
