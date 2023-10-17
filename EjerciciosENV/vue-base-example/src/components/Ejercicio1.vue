<template>
    <div>
    <h1> Hola!!!</h1>
      <input v-model="nombre"/>
    <h2>Mi nombre es {{nombre}}</h2>
    </div>
</template>
<script>
/* eslint-disable */
  export default {
    name: 'ExampleComponent',
    data: function () {
      return {
        nombre: 'Ori'
      }
    }
  }
</script>
  
<style>
body {
    font-family: Arial, sans-serif;
    background-color: hsl(0, 0%, 100%);
    margin: 0;
    padding: 0;
}

</style>