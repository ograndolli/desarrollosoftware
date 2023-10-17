import axios from 'axios'

methods: {
    cargarDatos (){
        axios.get('http://localhost:8000/items/')
        .then(response => {
            this.items = response.data
            console.log(response.data)
        })
        .catch(error => {
            console.log(error)
        })
    },