<script>
import { sendCommand } from '../utils/utils.ts'
export default {
  data() {
    return {
      text: this.updateRoonInfo()
    }
  },
  mounted() {
    setInterval(async () => {
      await this.updateRoonInfo()
    }, 2000)
  },
  methods: {
    async updateRoonInfo() {
      this.$refs.roonInfo.innerText = await sendCommand('roon', 'getinfo');
    }
  }
}
</script>

<template>
  <div style="white-space: pre-wrap;">
    <text ref="roonInfo">{{ text }}</text>
  </div>
</template>
