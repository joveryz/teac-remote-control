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
      var res = await sendCommand('roon', 'getinfo')
      this.$refs.roonInfo.innerText = res.result;
    }
  }
}
</script>

<template>
  <div style="white-space: pre-wrap;">
    <text ref="roonInfo">{{ text }}</text>
  </div>
</template>
