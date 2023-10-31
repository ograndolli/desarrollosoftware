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
            
            axios.post("http://localhost:8000/autores/",{
                nombre: this.nuevoAutor, 
                biografia: 'Ejemplo de biografia',
                fecha_nacimiento: '2018-10-20',
                fecha_defuncion: '2018-10-20',
            })
            .then((response) => {
                this.cargarAutores()
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
            axios.get("http://localhost:8000/autores/")
            .then((response) => {
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
