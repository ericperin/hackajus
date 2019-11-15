<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <label for="">QR Code</label>
    <p class="decode-result">Last result: <b>{{ result }}</b></p>

    <qrcode-stream :camera="camera" @decode="onDecode" @init="onInit">
      <div v-if="validationSuccess" class="validation-success">
        Código válido
      </div>

      <div v-if="validationFailure" class="validation-failure">
        Código inválido
      </div>

      <div v-if="validationPending" class="validation-pending">
        Carregando...
      </div>
    </qrcode-stream>
  </div>
</template>

<script>
import { QrcodeStream } from 'vue-qrcode-reader'
export default {
  name: "HelloWorld",
  data () {
    return {
      isValid: undefined,
      camera: 'auto',
      result: null,
    }
  },
  props: {
    msg: String
  },
  components: {
    QrcodeStream
  },
  computed: {
    validationPending () {
      return this.isValid === undefined
        && this.camera === 'off'
    },

    validationSuccess () {
      return this.isValid === true
    },

    validationFailure () {
      return this.isValid === false
    }
  },
  methods: {
    // async onInit (promise) {
    //   try {
    //     await promise
    //   } catch (error) {
    //     if (error.name === 'NotAllowedError') {
    //       this.error = "ERROR: you need to grant camera access permisson"
    //     } else if (error.name === 'NotFoundError') {
    //       this.error = "ERROR: no camera on this device"
    //     } else if (error.name === 'NotSupportedError') {
    //       this.error = "ERROR: secure context required (HTTPS, localhost)"
    //     } else if (error.name === 'NotReadableError') {
    //       this.error = "ERROR: is the camera already in use?"
    //     } else if (error.name === 'OverconstrainedError') {
    //       this.error = "ERROR: installed cameras are not suitable"
    //     } else if (error.name === 'StreamApiNotSupportedError') {
    //       this.error = "ERROR: Stream API is not supported in this browser"
    //     }
    //   }
    // }

    onInit (promise) {
      promise
        // .catch(console.error)
        .then(this.resetValidationState)
    },

    resetValidationState () {
      this.isValid = undefined
    },

    async onDecode (content) {
      this.result = content
      this.turnCameraOff()

      // pretend it's taking really long
      await this.timeout(500)
      this.isValid = content.startsWith('http')

      // some more delay, so users have time to read the message
      await this.timeout(2000)

      this.turnCameraOn()
    },

    turnCameraOn () {
      this.camera = 'auto'
    },

    turnCameraOff () {
      this.camera = 'off'
    },

    timeout (ms) {
      return new Promise(resolve => {
        window.setTimeout(resolve, ms)
      })
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.validation-success,
.validation-failure,
.validation-pending {
  position: absolute;
  width: 100%;
  height: 100%;

  background-color: rgba(255, 255, 255, .8);
  text-align: center;
  font-weight: bold;
  font-size: 1.4rem;
  padding: 10px;

  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
}
.validation-success {
  color: green;
}
.validation-failure {
  color: red;
}
</style>
