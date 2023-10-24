<template>
    <div id="app">
        <h1> Autores de Libros </h1>
        <div>
            <h2> Cargar Autor </h2>
            <input v-model="nuevoAutor" @input="resetMessage" />
            <button @click="agregarAutor"> Agregar autor</button>
            <p class="message"> {{ message }}</p>
        </div>
        <div>
            <h2> Autores </h2>
            <ul>
                <li v-for="autor in autores" :key="autor.id">
                {{ autor.nombre }}
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
            autores: [],
            nuevoAutor: "",
            message: "",
            autorId: 1, 
        } 
    },
    mounted(){
        this.cargarAutores();
    },
    methods: {
        agregarAutor(){
            if(this.nuevoAutor.trim() === ""){
                this.message = "Por favor, ingresa el nombre del autor"
                return;
            }  
            
            axios.post("https://localhost:8000/api/views.py/autores/")
            axios.then((response) => {
                this.autores.push({
                    id: response.data.id,
                    nombre: this.nuevoAutor,
                });
                this.nuevoAutor= "";
            })

            .catch((error)=> {
                console.error("Error al agregar autor: " + error);
            });
        },
        resetMessage(){
            this.message = "";
        },
        cargarAutores(){
            axios.get("https://localhost:8000/api/views.py/autores/")
            axios.then((response) => {
                this.autores = response.data;
            })
            .catch((error) => {
                console.error("Error al cargar autores: " + error)
            });
        },

    },

}

</script>


<style>

ul{
    list-style: none;
    padding: 0;
}
li{
    margin-bottom: 5px;
}

</style>
