<script>
import { sendCommand } from '../utils/utils.ts'
export default {
  data() {
    return {
      text: "Track: unknown\nArtist: unknown\nAlbum: unknown"
    }
  },
  mounted() {
    setTimeout(async () => {
      await this.updateRoonInfo()
    }, 0)
  },
  methods: {
    async updateRoonInfo() {
      while (true) {
        var res = await sendCommand('roon', 'getinfo')
        var info = /Track: \"(.*)\"Artist: \"(.*)\"Album: \"(.*)\"State/.exec(res.result.replace(/\n/g, "").replace(/\t/g, ""))
        this.$refs.roonInfo.innerText = `Track: ${info[1]}\nArtist: ${info[2]}\nAlbum: ${info[3]}`;
      }
    }
  }
}
</script>

<template>
  <div style="white-space: pre-wrap;">
    <text ref="roonInfo">{{ text }}</text>
  </div>
</template>
