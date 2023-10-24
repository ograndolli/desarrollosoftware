<template>
  <div id="app">
    <Autores class= "primero"/>
    <Libros class="segundo"/>
  </div>
</template>

<script>
/* eslint-disable */

import Libros from './components/Libros'
import Autores from './components/Autores'

export default {
  name: 'App',
  components: {
    Autores,
    Libros
  }
}
</script>

<style>
.primero{
  background-color:#DCC3FF;
  padding: 2%;
  margin: 2%;
}

.segundo{
  background-color: #DCC3FF;
  padding: 2%;
  margin: 2%;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
