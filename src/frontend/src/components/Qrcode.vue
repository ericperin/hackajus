<template>
  <div class="hello">
    <h1>Recebimento via QR Code</h1>

    <div class="row justify-content-center">
      <div class="form-group col-md-4">
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
    </div>

    <h2>ou</h2>

    <div class="row justify-content-center">
      <div class="form-group col-md-6">
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
      </div>
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
      result: null,
      error: ""
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
      window.$(".swal2-input").mask("000.000.000-00");
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
            text: "Digite o CPF",
            showLoaderOnConfirm: true,
            preConfirm: () => {
              return fetch("//api.ipify.org?format=json")
                .then(response => response.json())
                .then(data => {
                  this.$swal.insertQueueStep({
                    title: "Informações da Nota Fiscal",
                    text: `Digite ou leia o qr code da NF ${data.ip}`
                  });
                })
                .catch(() => {
                  this.$swal.insertQueueStep({
                    icon: "error",
                    title: "Ops! Aconteceu algo inesperado."
                  });
                });
            }
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
        let msg = "Ops!";
        if (error.name === "NotAllowedError") {
          msg = "Você precisar dar permissão de acesso a sua câmera";
        } else if (error.name === "NotFoundError") {
          msg = "Nenhuma cãmera encontrada";
        } else if (error.name === "NotSupportedError") {
          msg = "Segurança é obrigatória (HTTPS, localhost)";
        } else if (error.name === "NotReadableError") {
          msg = "A câmera já esta em uso?";
        } else if (error.name === "OverconstrainedError") {
          msg = "Câmera instala não esta adequada corretamente";
        } else if (error.name === "StreamApiNotSupportedError") {
          msg = "Stream API não tem suporte neste browser";
        }
        alert(msg);
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
