<template>
  <div id="app">
    <ReccomenderWindow />
  </div>
</template>

<script>
import ReccomenderWindow from './components/ReccomenderWindow.vue'

export default {
  name: 'App',
  components: {
    ReccomenderWindow
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
