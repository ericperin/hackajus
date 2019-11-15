<template>
  <div id="app">
    <img alt="Vue logo" src="https://www.tjro.jus.br/templates/tjro_portal_responsivo/images/presets/tjro/logo.png">
    <HelloWorld msg="HACKAJUS"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

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
