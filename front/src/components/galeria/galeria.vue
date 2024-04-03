<template lang="html">
    <body>
      <header id="header">
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
        <!-- <div class="overlay">
          <div class="slideshow">
            <span class="btn-cerrar">&times;</span>
            <div class="botones adelante">
              <i class="fa-solid fa-circle-arrow-right"></i>
            </div>
            <div class="botones atras">
              <i class="fa-solid fa-circle-arrow-left"></i>
            </div>
            <img src="" alt="" id="img-siledeshow">
          </div> -->
        <!-- </div> -->
        <div class="recent-orders">
          <div class="container" >
            <div class="box-date">
            <h2>Ultrasonido: Nombre</h2>
            <p>Fecha: 1/04/2023</p>
            <div class="options">
              <button id="btnShow" @click="Showhide">
                <p>ver mas</p><i class="fa-solid fa-caret-down" style="color:#33a451;"></i>
              </button>
            </div>
          </div>
            <div href="grid1" class="grid-container" id="grid-container" >
              <img class="grid-item" src="https://picsum.photos/230/155.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/152.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/154.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/150.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/158.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/150.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/152.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/154.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/150.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/158.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/155.jpg" width="230" height="155"/>
            </div>
            <div class="enviar">
              <button class="boton">
              <!-- <button id="btnenviarw" @click="whatsapp"> -->
                <i class="fa-brands fa-whatsapp imagen" style="color: #fff;"></i>
                <p class="texto">Enviar</p>
              </button>
            <button class="boton1">
              <!-- <button id="btnenviarw" @click="whatsapp"> -->
                <i class="fa-regular fa-envelope imagen1" style="color: #fff;"></i>
                <p class="texto1">Enviar</p>
            </button>
          </div> 
          </div>
          <div class="container" >
            <div class="box-date">
            <h2>Ultrasonido: Nombre1</h2>
            <p>Fecha: 3/04/2023</p>
            <div class="options">
              <button id="btnShow" @click="Showhide">
                <p>ver mas</p><i class="fa-solid fa-caret-down" style="color:#33a451;"></i>
              </button>
            </div>
          </div>
            <div href="grid1" class="grid-container" id="grid-container" style="display:none;">
              <img class="grid-item" src="https://picsum.photos/230/155.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/152.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/154.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/150.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/158.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/150.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/152.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/154.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/150.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/158.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/153.jpg" width="230" height="155"/>
                            <img class="grid-item" src="https://picsum.photos/230/155.jpg" width="230" height="155"/>
            </div>
            
          </div> 
          
      <!-- <img class="grid-item" src="https://picsum.photos/230/300.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/410.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/250.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/180.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/340.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/120.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/215.jpg"  /> -->
      <!-- <img class="grid-item" src="https://picsum.photos/230/420.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/320.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/153.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/480.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/260.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/450.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/135.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/180.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/340.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/120.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/215.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/420.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/320.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/153.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/480.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/260.jpg" />
      <img class="grid-item" src="https://picsum.photos/230/450.jpg"  />
      <img class="grid-item" src="https://picsum.photos/230/135.jpg"  /> -->
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
import { watch } from 'vue';

export default {
  data() {
    return {
      items: ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
    };
  },
  mounted() {
    // Inicializa Masonry después de que el componente haya sido montado
    this.initializeMasonry();

    // Muestra u oculta el elemento this.$refs.grit
    this.Showhide();
  },
  methods: {
    initializeMasonry() {
      var elem = document.querySelector('.grid-container');
      var msnry = new Masonry(elem, {
        itemSelector: '.grid-item',
        columnWidth: 230,
        gutter: 20,
        isFitWidth: true
      });
    },
    Showhide() {

      const show = document.getElementById("grid-container");
      if (show) {
        if (show.style.display === "none") {
          show.style.display = "block";
        } else {
          show.style.display = "none";
        }
      }
    }
  }
};

</script>
