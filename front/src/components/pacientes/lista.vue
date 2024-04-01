<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de pacientes</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="usuarios" :fields="fields">
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>
<style lang="css">
/* Importa los estilos de Bootstrap solo en este componente */
@import 'bootstrap/dist/css/bootstrap.css';
@import 'bootstrap-vue/dist/bootstrap-vue.css';

h2{
    margin-top: 10px;
}
/* Estilos específicos de este componente */
/* Agrega tus estilos aquí */
</style>

<script>

import axios from 'axios'

export default {
    data() {
        return {
            fields: [
                { key: 'Nombre', label: 'Nombre' },
                { key: 'Apellido_Paterno', label: 'Apellido Paterno' },
                { key: 'Apellido_Materno', label: 'Apellido Materno' },
                { key: 'NumeroCelular', label: 'Teléfono' },
                { key: 'Correo', label: 'correo' },
                { key: 'Rol', label: 'Rol' },
            ],
            usuarios: []
        }
    },
    methods: {
        getusuaios() {
            const path = 'http://127.0.0.1:8000/EnlaceDigna/clientes/'
            axios.get(path)
                .then((response) => {
                    this.usuarios = response.data
                })
                .catch((error) => {
                    console.log(error)
                })
        }
    },
    created() {
        this.getusuaios()
    }
}
</script>
