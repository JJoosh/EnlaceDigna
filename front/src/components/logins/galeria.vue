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
        <div class="recent-orders">
          <div class="container">
            <div class="box-date">
              <h2>Ultrasonido: Nombre</h2>
              <p>Fecha: 1/04/2023</p>
              <div class="options">
                <button id="btnShow" @click="Showhide">
                  <p>ver mas</p><i class="fa-solid fa-caret-down" style="color:#33a451;"></i>
                </button>
              </div>
            </div>
            <div href="grid" class="grid-container" id="grid-container" style="display: none;">
              <img v-for="(imagen, index) in imagenes" :key="index" class="grid-item" :src="imagen.img" width="230" height="155" @click="openOverlay(imagen.img)" />
            </div>
            <div class="enviar" id="enviar">
              <button class="boton" @click="sendWithWhatsapp">
                <i class="fa-brands fa-whatsapp imagen" style="color: #fff;"></i>
                <p class="texto">Enviar</p>
              </button>
              <button class="boton1" @click="sendWithEmail">
                <i class="fa-regular fa-envelope imagen1" style="color: #fff;"></i>
                <p class="texto1">Enviar</p>
              </button>
            </div>
          </div>
          <!-- Repite la estructura para el segundo container -->
        </div>
      </div>
    </main>
  </body>
</template>

<style>
  @import url('./styles.css');
</style>

<script>
import Masonry from 'masonry-layout';
import imagesLoaded from 'imagesloaded';
import { ref } from 'vue';

export default {
  data() {
    return {
      overlayVisible: false,
      currentImage: '',
      imagenes: [
        { img: 'https://picsum.photos/230/155.jpg' },
        { img: 'https://picsum.photos/230/151.jpg' },
        { img: 'https://picsum.photos/230/150.jpg' },
        { img: 'https://picsum.photos/230/152.jpg' },
        { img: 'https://picsum.photos/230/154.jpg' },
        { img: 'https://picsum.photos/230/153.jpg' },
        { img: 'https://picsum.photos/230/155.jpg' },
        { img: 'https://picsum.photos/230/151.jpg' },
        { img: 'https://picsum.photos/230/150.jpg' },
        { img: 'https://picsum.photos/230/152.jpg' },
        { img: 'https://picsum.photos/230/154.jpg' },
        { img: 'https://picsum.photos/230/153.jpg' },
        { img: 'https://picsum.photos/230/155.jpg' },
        { img: 'https://picsum.photos/230/151.jpg' },
        { img: 'https://picsum.photos/230/150.jpg' },
        { img: 'https://picsum.photos/230/152.jpg' },
        { img: 'https://picsum.photos/230/154.jpg' },
        { img: 'https://picsum.photos/230/153.jpg' },
      ],
      contador: 0,
    };
  },
  setup() {
    const contenedor = ref(null);
    const imgSlideshows = ref(null);

    const initializeMasonry = () => {
      if (contenedor.value) {
        const msnry = new Masonry(contenedor.value, {
          itemSelector: '.grid-item',
          columnWidth: 230,
          gutter: 20,
          isFitWidth: true
        });
      }
    };

    const Showhide = () => {
      const show = document.getElementById("grid-container");
      const enviar = document.getElementById("enviar");
      if (show) {
        if (show.style.display === "none") {
          show.style.display = "block";
          enviar.style.display = "block";
        } else {
          show.style.display = "none";
          enviar.style.display = "none";
        }
      }
    };

    return {
      contenedor,
      imgSlideshows,
      initializeMasonry,
      Showhide,
    };
  },
  methods: {
    openOverlay(imageSrc) {
      this.overlayVisible = true;
      this.currentImage = imageSrc;
    },
    changeImage(direction) {
      if (direction === 'next') {
        if (this.contador < this.imagenes.length - 1) {
          this.contador++;
        } else {
          this.contador = 0;
        }
      } else if (direction === 'prev') {
        if (this.contador > 0) {
          this.contador--;
        } else {
          this.contador = this.imagenes.length - 1;
        }
      }
      this.currentImage = this.imagenes[this.contador].img;
    },
    closeOverlay() {
      this.overlayVisible = false;
    },
    sendWithWhatsapp() {
      // Lógica para enviar por WhatsApp
    },
    sendWithEmail() {
      // Lógica para enviar por correo electrónico
    },
  },
  mounted() {
    this.initializeMasonry();
  }
};
</script>