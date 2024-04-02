<template lang="html">
  <body>
    <header id="header">
        <img src="@/assets/Recurso1.svg" class="logo">
      <input type="checkbox" id="menu">
      <label for="menu">
        <i class="fa-solid fa-bars menu_icono"></i>
      </label>
      <ul class="menu">
        <li class="item" id="item">Ajustes</li>
        <li class="item" id="item">Usuario</li>
        <li class="btn"  id="item">Salir</li>
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
        </div>
      </div> -->
      <div class="recent-orders">
        <div class="box-date">
          <h2>Ultrasonido: Nombre</h2>
          <p>Fecha: 1/04/2023</p>
        </div>
        <div class="container" >
          <div href="grid" class="grid-container">
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
        <div class="box-date">
          <h2>Ultrasonido: Nombre1</h2>
          <p>Fecha: 1/04/2023</p>
        </div>
        <div class="container" >
          <div href="grid" class="grid-container">
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
      </div>
      
    </div>
    </main>
</body>
</template>
<style scoped>
  @import url('./styles.css');
</style>
<script>

import Masonry from 'masonry-layout';
import imagesLoaded from 'imagesloaded';

export default {
data() {
  return {
    items: ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
  };
},
mounted() {
  const header = document.getElementById("header");
  const item = document.getElementById("item");
  window.addEventListener('scroll', () => {
    var scroll = window.scrollY;
    if (scroll > 10) {
      header.style.backgroundColor = '#000';
      item.style.color = '#fff';
    } else {
      header.style.backgroundColor = 'transparent';
    }
  });
  // Elemento que quieres convertir en un diseño de mampostería
  var elem = document.querySelector('.grid-container');
  // imagesLoaded(elem,()=>{
    var msnry = new Masonry( elem, {
// option
      itemSelector: '.grid-item',
      columnWidth: 230,
      gutter: 20,
      isFitWidth: true
});
  // });
}
};
</script>