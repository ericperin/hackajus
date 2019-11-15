<template>
  <div id="app">
    <img alt="TJ-RO" src="./assets/tjro.png">
    <HelloWorld msg="HACKAJUS"/>
  </div>
</template>

<script>
import HelloWorld from './components/Qrcode.vue'

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
