<template>
  <div class="hello">
    <!-- <h1>{{ msg }}</h1> -->
    <h1>Recebimento via QR Code</h1>

    <!-- <button type="button" class="btn btn-default btn-block">
      <i class="fas fa-qrcode fa-9x"></i>
    </button> -->

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

    <h2>ou</h2>
    <div class="row">
      <div class="input-group input-group-lg flex-nowrap">
        <div class="input-group-prepend">
          <span class="input-group-text" id="addon-wrapping"
            ><i class="fas fa-barcode"></i
          ></span>
        </div>
        <input
          type="text"
          class="form-control"
          name="code"
          placeholder="Código de barras"
        />
      </div>
      <div class="form-group col-md-12"></div>
    </div>
    <p>
      <b>{{ result }}</b>
    </p>
  </div>
</template>

<script>
import { QrcodeStream } from "vue-qrcode-reader";
export default {
  name: "HelloWorld",
  data() {
    return {
      isValid: undefined,
      camera: "auto",
      result: null
    };
  },
  props: {
    msg: String
  },
  components: {
    QrcodeStream
  },
  computed: {
    validationPending() {
      window.$('.swal2-input').mask('000.000.000-00');
      return this.isValid === undefined && this.camera === "off";
    },

    validationSuccess() {
      return this.isValid === true;
    },

    validationFailure() {
      return this.isValid === false;
    }
  },
  methods: {
    showAlert() {
      this.$swal
        .mixin({
          input: "text",
          confirmButtonText: "Próximo",
          showCancelButton: false,
          progressSteps: ["1", "2"]
        })
        .queue([
          {
            title: "Informações do usuário",
            text: "Digite o CPF"
          },
          {
            title: "Informações da Nota Fiscal",
            text: "Digite ou leia o qr code da NF"
          }
        ])
        .then(result => {
          if (result.value) {
            const answers = JSON.stringify(result.value);
            this.$swal.fire(
              "Informações enviadas com sucesso!",
              `${answers}`,
              "success"
            );
          }
        });
    },

    onInit(promise) {
      promise.then(this.resetValidationState).catch(function(error) {
        if (error.name === "NotAllowedError") {
          this.error = "ERROR: you need to grant camera access permisson";
        } else if (error.name === "NotFoundError") {
          this.error = "ERROR: no camera on this device";
        } else if (error.name === "NotSupportedError") {
          this.error = "ERROR: secure context required (HTTPS, localhost)";
        } else if (error.name === "NotReadableError") {
          this.error = "ERROR: is the camera already in use?";
        } else if (error.name === "OverconstrainedError") {
          this.error = "ERROR: installed cameras are not suitable";
        } else if (error.name === "StreamApiNotSupportedError") {
          this.error = "ERROR: Stream API is not supported in this browser";
        }
      });
    },

    resetValidationState() {
      this.isValid = undefined;
    },

    async onDecode(content) {
      this.result = content;
      this.turnCameraOff();

      // pretend it's taking really long
      await this.timeout(500);
      // this.isValid = content.startsWith("R4");
      if (content.startsWith("R4")) {
        this.showAlert();
      }

      // some more delay, so users have time to read the message
      await this.timeout(2000);

      this.turnCameraOn();
    },

    turnCameraOn() {
      this.camera = "auto";
    },

    turnCameraOff() {
      this.camera = "off";
    },

    timeout(ms) {
      return new Promise(resolve => {
        window.setTimeout(resolve, ms);
      });
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

  background-color: rgba(255, 255, 255, 0.8);
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
