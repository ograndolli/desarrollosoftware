<template>
    <div id="app">
        <title> Pagina de Libros </title>
        <div>
            <h2>Libros</h2>
            <ul>
                <li v-for="libro in libros" :key="libro.id">
                <h3>{{libro.titulo}}</h3>
                <p>Autor: {{ libro.autor}}</p>
                <img :src="libro.imagen" alt="Portada del libro" />
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'

export default {
    data: function (){
        return{
            libros: [],
        } 
    },
    mounted(){
        this.cargarLibros();
    },
    methods: {
        cargarLibros(){
            axios.get("http://localhost:8000/libros/")
            .then((response) => {
                this.libros = response.data;
            })
            .catch((error) => {
                console.error("Error al cargar libros: " + error); 
            });
        },
    },
}
</script>

<style>
ul{
    list-style:none;
    padding:0;
}

li{
    margin-bottom:20px;
    border: 1px solid #ccc;
    padding: 10px;
}

img{
    max-width:20px;
    height: auto;
}
</style>