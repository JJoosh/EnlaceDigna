<template>
  <body>
    <header id="header" v-show="!overlayVisible">
      <img src="@/assets/Recurso1.svg" class="logo">
        <input type="checkbox" id="menu">
        <label for="menu">
          <i class="fa-solid fa-bars menu_icono"></i>
        </label>
        <!-- buscador -->
        <div class="search-main">
          <form class="buscador" id="buscador" href="buscador">
            <i class="fa-solid fa-magnifying-glass" style="color: #33a451;"></i>
            <input type="text"  name="search" placeholder="Buscar" href="search" class="search" id="search" autocomplete="off">
            <!-- v-model="searchTerm" -->
          </form>
          <ul id="box-search"  ref="searchResultsList" >
            <!-- v-show="showSearchResults" -->
            <li >
              <!-- <li v-for="result in searchResults" :key="result.token" class="li1"  @click="showSelectedOrder(result)"> -->
              <!-- <a href="#uploadForm"><span class="sp2"><i class="fa-solid fa-magnifying-glass" style="color: #7d8da1;"></i></span></a> -->
              <!-- Token: {{ result.token }}</span> <br class="responsive-br">Nombre: {{ result.nombre }} -->
            </li>
          </ul>
          <p id="mensajeNoResultados" style="display: none;">No hay resultados</p>
        </div>
        <!-- fin buscador -->
        <ul class="menu">
          <li class="item" id="item">Ajustes</li>
          <li class="item">Usuario</li>
          <li class="btn">Salir</li>
        </ul>
    </header>
    <main>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
      <div class="main-container">
        <div class="recent-orders" v-for="(dato, index) in datosConImagenes" :key="index">
          <div class="container">
            <div class="box-date">
              <h2>Ultrasonido: {{ dato.TipoDeUltrasonidos }}</h2>
              <p>Fecha: {{ dato.Fecha }}</p>
              <div class="options">
                <button id="btnShow" @click="Showhide(index)">
                  <p>ver mas</p><i class="fa-solid fa-caret-down" style="color:#33a451;"></i>
                </button>
              </div>
            </div>
            <div :href="'grid-' + index" class="grid-container" :id="'grid-container-' + index" style="display: none;">
              <img v-for="(imagen, imgIndex) in dato.imagenes" :key="imgIndex" class="grid-item" :src="imagen.img" width="230" height="155" @click="openOverlay(imagen.img, index)" />
            </div>
            <div class="enviar" :id="'enviar-' + index">
              
              <button class="boton" @click="sendWithWhatsapp(index)">
                <i class="fa-brands fa-whatsapp imagen" style="color: #fff;"></i>
                <p class="texto">Enviar</p>
              </button>
              <button class="boton1" @click="sendWithEmail(index)">
                <i class="fa-regular fa-envelope imagen1" style="color: #fff;"></i>
                <p class="texto1">Enviar</p>
              </button>
            </div>
          </div>
        </div>
        </div>

      <div class="overlay" v-if="overlayVisible">
        <div class="slideshow">
          <span class="btn-cerrar" @click="closeOverlay">&times;</span>
          <div class="botones adelante" @click="changeImage('next')">
            <i class="fa-solid fa-circle-arrow-right"></i>
          </div>
          <div class="botones atras" @click="changeImage('prev')">
            <i class="fa-solid fa-circle-arrow-left"></i>
          </div>
          <img :src="currentImage" alt="" id="img-slideshow">
        </div>
      </div>
    </main>
  </body>
</template>

<script>
import Masonry from 'masonry-layout';
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      fields: [
        { key: 'ruta_files', label: 'Ruta files' },
        { key: 'TipoDeUltrasonidos', label: 'Tipo de ultrasonidos' },
        { key: 'Fecha', label: 'Fecha' },
      ],
      datos: [],
      datosConImagenes: [],
      overlayVisible: false,
      currentImage: '',
      currentDataIndex: 0, // Nueva propiedad para almacenar el índice de los datos actuales
    };
  },
  setup() {
    const contenedor = ref(null);
    const imgSlideshows = ref(null);

    const initializeMasonry = () => {
      if (contenedor.value) {
        new Masonry(contenedor.value, {
          itemSelector: '.grid-item',
          columnWidth: 230,
          gutter: 20,
          isFitWidth: true
        });
      }
    };

    return {
      contenedor,
      imgSlideshows,
      initializeMasonry,
    };
  },
  methods: {
    filtrarResultados() {
      const box_search = this.$refs.searchResultsList;
      const mensajeNoResultados = this.$refs.mensajeNoResultados;

      // Filtrar los resultados basados en el término de búsqueda
      this.searchResults = this.datosConImagenes.filter(item => {
        return item.TipoDeUltrasonidos.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
               item.Fecha.toLowerCase().includes(this.searchTerm.toLowerCase());
      });

      if (this.searchTerm === "") {
        box_search.style.display = "none";
        mensajeNoResultados.style.display = "none";
      } else if (this.searchResults.length > 0) {
        box_search.style.display = "block";
        mensajeNoResultados.style.display = "none"; // Oculta el mensaje de no resultados
      } else {
        box_search.style.display = "none";
        mensajeNoResultados.style.display = "block";
      }
    },
    showSelectedOrder(result) {
      const box_search = this.$refs.searchResultsList;

      this.selectedOrder = result;
      box_search.style.display = "none";
      this.searchTerm = '';
    },
    getdatos() {
      const path = 'http://127.0.0.1:8000/get_galeria/3/';
      axios.get(path)
        .then((response) => {
          this.datos = response.data;
          this.procesarDatos();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    procesarDatos() {
      this.datosConImagenes = [];

      for (let i = 0; i < this.datos.length; i++) {
        const item = this.datos[i];
        const imagenes = [];

        const enlacesArray = JSON.parse(item.ruta_files);

        for (let j = 0; j < enlacesArray.length; j++) {
          const enlace = enlacesArray[j];
          const enlaceString = JSON.stringify(enlace).replace(/"/g, "");
          imagenes.push({ img: enlaceString });
        }

        this.datosConImagenes.push({
          ...item,
          imagenes,
        });
      }
    },
    Showhide(index) {
      const show = document.getElementById(`grid-container-${index}`);
      // const enviar = document.getElementById(`enviar-${index}`);
      if (show) {
        if (show.style.display === "none") {
          show.style.display = "block";
         
        } else {
          show.style.display = "none";
         
        }
      }
    },
    openOverlay(imageSrc, index) {
      this.overlayVisible = true;
      this.currentImage = imageSrc;
      this.currentDataIndex = index; // Asigna el índice de los datos actuales
    },
    changeImage(direction) {
      if (this.datosConImagenes.length > 0 && this.datosConImagenes[this.currentDataIndex] && this.datosConImagenes[this.currentDataIndex].imagenes) {
        const currentIndex = this.datosConImagenes[this.currentDataIndex].imagenes.findIndex(
          (imagen) => imagen.img === this.currentImage
        );

        if (direction === 'next') {
          if (currentIndex < this.datosConImagenes[this.currentDataIndex].imagenes.length - 1) {
            this.currentImage = this.datosConImagenes[this.currentDataIndex].imagenes[currentIndex + 1].img;
          } else {
            this.currentImage = this.datosConImagenes[this.currentDataIndex].imagenes[0].img;
          }
        } else if (direction === 'prev') {
          if (currentIndex > 0) {
            this.currentImage = this.datosConImagenes[this.currentDataIndex].imagenes[currentIndex - 1].img;
          } else {
            this.currentImage = this.datosConImagenes[this.currentDataIndex].imagenes[this.datosConImagenes[this.currentDataIndex].imagenes.length - 1].img;
          }
        }
      }
    },
    closeOverlay() {
      this.overlayVisible = false;
    },
    sendWithWhatsapp() {
      // Lógica para enviar por WhatsApp las imágenes correspondientes al índice
    },
    sendWithEmail() {
      // Lógica para enviar por correo electrónico las imágenes correspondientes al índice
    },
  },
  created() {
    this.getdatos();
  },
  mounted() {
    this.initializeMasonry();
  },
};
</script>
<style>
  @import url('./styles.css');
</style>
