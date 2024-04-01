<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de pacientes</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="pacientes" :fields="fields">
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
                { key: 'apellido_p', label: 'Apellido Paterno' },
                { key: 'apellido_m', label: 'Apellido Materno' },
                { key: 'telefono', label: 'Teléfono' },
                { key: 'email', label: 'Email' },
            ],
            pacientes: []
        }
    },
    methods: {
        getpacientes() {
            const path = 'http://127.0.0.1:8000/api/v1.0/pacientes/'
            axios.get(path)
                .then((response) => {
                    this.pacientes = response.data
                })
                .catch((error) => {
                    console.log(error)
                })
        }
    },
    created() {
        this.getpacientes()
    }
}
</script>
