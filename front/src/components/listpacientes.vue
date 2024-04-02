<template >
    <html lang="en">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Sharp" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <body>
    
        <div class="container">
            <!-- Sidebar Section -->
            <aside ref="sideMenu">
                <div class="toggle">
                    
                    <div @click="closeSideMenu"  class="close" id="close-btn">
                        <span class="material-icons-sharp">
                            close
                        </span>
                    </div>
                </div>
    
                <div class="sidebar">
                    <a href="#">
                        <span class="material-icons-sharp">
                            dashboard
                        </span>
                        <h3>Dashboard</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            person_outline
                        </span>
                        <h3>Users</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            receipt_long
                        </span>
                        <h3>History</h3>
                    </a>
                    <a href="#" class="active">
                        <span class="material-icons-sharp">
                            insights
                        </span>
                        <h3>Analytics</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            inventory
                        </span>
                        <h3>Sale List</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            report_gmailerrorred
                        </span>
                        <h3>Reports</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            settings
                        </span>
                        <h3>Settings</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            add
                        </span>
                        <h3>Agregar Paciente</h3>
                    </a>
                    <a href="#">
                        <span class="material-icons-sharp">
                            logout
                        </span>
                        <h3>Logout</h3>
                    </a>
                </div>
            </aside>
            <main>
                <h1>Pacientes</h1>
                <div class="search-main">
                    <h2>Buscador </h2>
                    <div class="new-search">
                            <form class="buscador" id="buscador" href="buscador">
                              <i class="fa-solid fa-magnifying-glass" style="color: #7d8da1;margin-right: 10PX;"></i>
                                <input type="text" v-model="searchTerm" name="search" placeholder="Buscar" href="search" class="search" id="search" autocomplete="off">
                                
                            </form>
                            <ul id="box-search" v-show="showSearchResults" ref="searchResultsList" >
                                <li v-for="result in searchResults" :key="result.token" class="li1"  @click="showSelectedOrder(result)">
                                    <a href="#uploadForm"><span class="sp2"><i class="fa-solid fa-magnifying-glass" style="color: #7d8da1;"></i>Token: {{ result.token }}</span> <br class="responsive-br">Nombre: {{ result.nombre }}</a>
                                </li>
                            </ul>
                            <p id="mensajeNoResultados" style="display: none;">No hay resultados</p>
                    </div>
                </div>
                <div class="new-users">
                    <h2>Resultados</h2>
                    <div class="user-list">
                        <form class="both" action="/upload" method="post" enctype="multipart/form-data" id="uploadForm">
                            <label for="files" class="custom-upload-button">
                              <img class="add" src="@/assets/agregar.png" alt="Subir archivos">
                            </label>
                                <input type="file" name="files[]" id="files" multiple accept="image/*, video/*" style="display: none;">
                                <div class="right" v-if="selectedOrder">
                                        <h2>Nombre: {{ selectedOrder.nombre }}</h2>
                                        <h2>Token: {{ selectedOrder.token }}</h2>
                                        <h2>Fecha: {{ selectedOrder.fecha }}</h2>
                                </div>
                                <div class="right" v-else>
                                        <h2>Nombre: </h2>
                                        <h2>Token: </h2>
                                        <p>Fecha: </p>
                                </div>
                            <div class="both-ultra">
                                <label for="ultrasonido" class="ultra"><h2>Tipo de ultrasonido</h2></label>
                            <input type="text" name="ultrasonido" id="ultrasonido" placeholder="Escribe aqui">
                            </div>
                            <input class="bt-add" type="submit" value="Subir">
                        </form>
                    </div>
                </div>
    
                <div class="recent-orders">
                    <h2>Añadidos recientemente</h2>
                    <table>
                        <thead>
                            <tr>
                            <th>Nombre</th>
                            <th>Token</th>
                            <th>fecha</th>
                            <th>foto</th>
                            <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="order in Orders" :key="order.id">
                            <td>{{ order.nombre }}</td>
                            <td>{{ order.token }}</td>
                            <td>{{ order.fecha }}</td>
                            <td>{{ order.foto }}</td>
                            <td class="primary">mas</td>
                            </tr>
                        </tbody>
                    </table>
                    <a href="#">mostrar todos</a>
                </div>
            </main>
            <div class="right-section">
                <div class="nav">
                    <button id="menu-btn" @click="toggleSideMenu">
                        <span class="material-icons-sharp">
                            menu
                        </span>
                    </button>
    
                </div>
                <div class="user-profile">
                    <div class="logo">
                        <img src="@/assets/SALUD.svg" alt="Imagen SVG de Salud">
                        <h2>Salud Digna</h2>
                        <p>Datos</p>
                    </div>
                </div>
    
                <div class="reminders">
                    <div class="header">
                        <h2>usuario</h2>
                        <span class="material-icons-sharp">
                            notifications_none
                        </span>
                    </div>
                </div>
                <div class="user-profile">
                    <div class="logo">
                        <img src="@/assets/SALUD.svg" alt="Imagen SVG de Salud">
                        <p>Datos</p>
                    </div>
                </div>
            </div>     
        </div>
       
    </body>
    
    </html>
    
  </template>
 <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
    :root{
        --color-primary: #6C9BCF;
        --color-white: #fff;
        --color-info-dark: #7d8da1;
        --color-dark: #363949;
        --color-light: rgba(132, 139, 200, 0.18);
        --color-dark-variant: #677483;
        --color-background: #f6f6f9;
    
        --card-border-radius: 2rem;
        --border-radius-1: 0.4rem;
        --border-radius-2: 1.2rem;
    
        --card-padding: 1.8rem;
        --padding-1: 1.2rem;
    
        --box-shadow: 0 2rem 3rem var(--color-light);
    }
    
    *{
        margin: 0;
        padding: 0;
        outline: 0;
        appearance: 0;
        border: 0;
        text-decoration: none;
        box-sizing: border-box;
    }
    
    .sp2{
       font-family: 'Poppins', sans-serif;
        margin-right:20%;
        color: #777777;
       
    }
    html{
        font-size: 14px;
    }
    
    body{
        width: 100vw;
        height: 100vh;
        font-family: 'Poppins', sans-serif;
        font-size: 0.88rem;
        user-select: none;
        overflow-x: hidden;
        color: var(--color-dark);
        background-color: var(--color-background);
    }
    
    a{
        color: var(--color-dark);
    }
    h1{
        font-weight: 800;
        font-size: 1.8rem;
    }
    
    h2{
        font-weight: 600;
        font-size: 1.4rem;
    }
    
    h3{
        font-weight: 500;
        font-size: 0.87rem;
    }
    S
    small{
        font-size: 0.76rem;
    }
  
    .buscador .search:focus{
    outline: 1px solid #7d8da1;
  }
    #box-search{
        width: 100%;
        background: #fff;
        z-index: 8;
        overflow: hidden;
        display: none;
    }
    
    #box-search li a{
        display: block;
        
        color: #777777;
        padding: 12px 20px;
    }
    
    #box-search li a:hover{
        background: #f3f3f3;
    }
    
    #box-search li a i{
        margin-right: 10px;
        color: #777777;
    }
    .add {
        max-width: 150px; 
        height: auto;
    }
    
    #cover-ctn-search{
        width: 100%;
        height: 100%;
        position: fixed;
        left: 0;
        background: rgba(0,0,0,0.5);
        z-index: 7;
        display: none;
    }
    .right{
        
        display: flex;
        justify-content:baseline;
        width: 100%;
        display: flex;
        flex-direction:column;
         /* user h2 y p */
  
    }
    .right h2{
        font-size: 100%;
    }
    .ultra h2{
        margin-bottom: 10px;
        font-size: 100%;
        
    }
    .both-ultra{
        width: 40%;
        margin-right: 25px;
        
    }
    #ultrasonido:focus{
    outline: 1px solid #7d8da1;
  }
     #ultrasonido{
        background-color: #F2F3F7;
        border-radius: 20px;
        width: 100%;
        height: 30px;
    }
    #ultrasonido::placeholder {
    padding-left: 10px;
  }
    .buscador {
        display: flex;
        align-items: center;
      }
      .buscador input {
        padding-left: 30px; 
        flex: 1;
      }
      .input-icon {
        margin-right: 10px;
      }
    .container{
        display: grid;
        width: 96%;
        margin: 0 auto;
        gap: 1.8rem;
        grid-template-columns: 12rem auto 23rem;
    }
    
    aside{
        height: 100vh;
        
    }
    
    aside .toggle{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-top: 1.4rem;
    }
    aside .toggle .logo{
        display: flex;
        gap: 0.5rem;
    }
    aside .toggle .logo{
        width: 2rem;
        height: 2rem;
    }
    
    aside .toggle .close{
        padding-right: 1rem;
        display: none;
    }
    
    aside .sidebar{
        display: flex;
        flex-direction: column;
        background-color: var(--color-white);
        box-shadow: var(--box-shadow);
        border-radius: 15px;
        height: 88vh;
        position: relative;
        top: 1.5rem;
        transition: all 0.3s ease;
    }
    
    aside .sidebar:hover{
        box-shadow: none;
    }
    
    aside .sidebar a{
        display: flex;
        align-items: center;
        color: var(--color-info-dark);
        height: 3.7rem;
        gap: 1rem;
        position: relative;
        margin-left: 2rem;
        transition: all 0.3s ease;
    }
    
    aside .sidebar a span{
        font-size: 1.6rem;
        transition: all 0.3s ease;
    }
    
    aside .sidebar a:last-child{
        position: absolute;
        bottom: 2rem;
        width: 100%;
    }
    
    aside .sidebar a.active{
        width: 100%;
        color: var(--color-primary);
        background-color: var(--color-light);
        margin-left: 0;
    }
    
    aside .sidebar a.active::before{
        content: '';
        width: 6px;
        height: 18px;
        background-color: var(--color-primary);
    }
    
    aside .sidebar a.active span{
        color: var(--color-primary);
        margin-left: calc(1rem - 3px);
    }
    
    aside .sidebar a:hover{
        color: var(--color-primary);
    }
    
    aside .sidebar a:hover span{
        margin-left: 0.6rem;
    }
    
    aside .sidebar .message-count{
        background-color: var(--color-danger);
        padding: 2px 6px;
        color: var(--color-white);
        font-size: 11px;
        border-radius: var(--border-radius-1);
    }
    
    main{
        margin-top: 1.4rem;
    }
    .buscador {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    .buscador input::placeholder {
        color:#7D8DA1;
    }
    
    
    .buscador input {
        width: 50%;
        padding: 10px 5px;
        
        border-radius: 20px;
        outline: none;
        background-color: #F2F3F7;
    }
    
    .buscador button {
        margin-left: 10px;
        padding: 10px 20px;
        background-color: #7D8DA1;
        color:#F2F3F7;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        font-size: 1rem;
    }
    
    main .new-users, .search-main{
        margin-top: 1.3rem;
    }
    
    main .new-users .user-list, .search-main .new-search{
        background-color: var(--color-white);
        padding: var(--card-padding);
        border-radius: var(--card-border-radius);
        margin-top: 1rem;
        box-shadow: var(--box-shadow);
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 1.4rem;
        cursor: pointer;
        transition: all 0.3s ease;
        align-items: left;
        justify-content: left;
    }
    
    .bt-add{
        margin-left: 10px;
        padding: 10px 20px;
        background-color: #7D8DA1;
        color:#F2F3F7;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        font-size: 1rem;
        width: 30%;
        
    }
    .both{
        display: flex;
        width: 100% !important;
        align-items: center;
    }
   
    main .new-users .user-list:hover{
        box-shadow: none;
    }
    main .search-main .new-search:hover{
        box-shadow: none;
    }
    
    main .new-users .user-list .user{
        display: flex;
        flex-direction: column;
        align-items: left;
        justify-content: left;
        padding-left: 15px;
        margin-right: 40%S;
    }
    main .search-main .new-search .buscador{
        align-items: left;
        justify-content: left;
    }
    .both img{
        width: 95%;
        height: auto;
    }
    main .recent-orders{
        margin-top: 1.3rem;
    }
    main .recent-orders h2{
        margin-bottom: 0.8rem;
    }
    main .recent-orders table{
        background-color: var(--color-white);
        width: 100%;
        padding: var(--card-padding);
        text-align: center;
        box-shadow: var(--box-shadow);
        border-radius: var(--card-border-radius);
        transition: all 0.3s ease;
    }
    main .recent-orders table:hover{
        box-shadow: none;
    }
    main table tbody td{
        height: 2.8rem;
        border-bottom: 1px solid var(--color-light);
        color: var(--color-dark-variant);
    }
    main table tbody tr:last-child td{
        border: none;
    }
    main .recent-orders a{
        text-align: center;
        display: block;
        margin: 1rem auto;
        color: var(--color-primary);
    }
    .right-section{
        margin-top: 1.4rem;
    }
    .right-section .nav{
        display: flex;
        justify-content: end;
        gap: 2rem;
    }
    .right-section .nav button{
        display: none;
    }
    .right-section .nav .profile{
        display: flex;
        gap: 2rem;
        text-align: right;
    }
    .right-section .nav .profile .profile-photo{
        width: 2.8rem;
        height: 2.8rem;
        overflow: hidden;
    }
    .right-section .user-profile{
        display: flex;
        justify-content: center;
        text-align: center;
        margin-top: 1rem;
        background-color: var(--color-white);
        padding: var(--card-padding);
        box-shadow: var(--box-shadow);
        cursor: pointer;
        transition: all 0.3s ease;
        border-radius: 25px;
    }
    .right-section .user-profile:hover{
        box-shadow: none;
    }
    .right-section .user-profile img{
        width: 11rem;
        height: auto;
        margin-bottom: 0.8rem;
    }
    .right-section .user-profile h2{
        margin-bottom: 0.2rem;
    }
    .right-section .reminders{
        margin-top: 2rem;
    }
    .right-section .reminders .header{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 0.8rem;
    }
    .right-section .reminders .header span{
        padding: 10px;
        box-shadow: var(--box-shadow);
        background-color: var(--color-white);
        border-radius: 50%;
    }
    .right-section .reminders .notification{
        background-color: var(--color-white);
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 0.7rem;
        padding: 1.4rem var(--card-padding);
        border-radius: var(--border-radius-2);
        box-shadow: var(--box-shadow);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .right-section .reminders .notification:hover{
        box-shadow: none;
    }
    .right-section .reminders .notification .content{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0;
        width: 100%;
    }
    .right-section .reminders .notification .icon{
        padding: 0.6rem;
        color: var(--color-white);
        background-color: var(--color-success);
        border-radius: 20%;
        display: flex;
    }
    .right-section .reminders .notification.deactive .icon{
        background-color: var(--color-danger);
    }
    .right-section .reminders .add-reminder{
        background-color: var(--color-white);
        border: 2px dashed var(--color-primary);
        color: var(--color-primary);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }
    
    .right-section .reminders .add-reminder:hover{
        background-color: var(--color-primary);
        color: white;
    }
    
    .right-section .reminders .add-reminder div{
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    
    @media screen and (max-width: 1200px) {
        .container{
            width: 95%;
            grid-template-columns: 7rem auto 23rem;
        }
    
        aside .logo h2{
            display: none;
        }
    
        aside .sidebar h3{
            display: none;
        }
    
        aside .sidebar a{
            width: 5.6rem;
        }
    
        aside .sidebar a:last-child{
            position: relative;
            margin-top: 1.8rem;
        }
    
        main .analyse{
            grid-template-columns: 1fr;
            gap: 0;
        }
    
        main .new-users .user-list .user{
            flex-basis: 40%;
        }
    
        
    
        main .recent-orders table{
            width: 100%;
        }
    
        main table thead tr th:last-child,
        main table thead tr th:first-child{
            display: none;
        }
    
        main table tbody tr td:last-child,
        main table tbody tr td:first-child{
            display: none;
        }
        .bt-add{
            width: 30%;
            height: 30px;
            font-size: 98%;
            margin: 0;
        }
        .add{
            max-width: 70px;
            height: auto;
        }
        .both{
            display: flex;
            flex-direction: column;
        }
        .both-ultra{
        margin-right: 0;
        width: 100%;
       
        margin-top: 5PX;
        margin-bottom: 5PX;
        display: flex;
        justify-content: space-around;
        align-items: left;
        justify-items: left;
        }
        .bt-add{
            width: 50%;
            height: 40px;
        }
        .responsive-br {
            display: block;
  }
    }
    
    @media screen and (max-width: 768px) {
        .container{
            width: 100%;
            grid-template-columns: 1fr;
            padding: 0 var(--padding-1);
        }
    
        aside{
            position: fixed;
            background-color: var(--color-white);
            width: 15rem;
            z-index: 3;
            box-shadow: 1rem 3rem 4rem var(--color-light);
            height: 100vh;
            left: -100%;
            display: none;
            animation: showMenu 0.4s ease forwards;
        }
    
        @keyframes showMenu {
           to{
            left: 0;
           } 
        }
    
        aside .logo{
            margin-left: 1rem;
        }
    
        aside .logo h2{
            display: inline;
        }
    
        aside .sidebar h3{
            display: inline;
        }
    
        aside .sidebar a{
            width: 100%;
            height: 3.4rem;
        }
    
        aside .sidebar a:last-child{
            position: absolute;
            bottom: 5rem;
        }
    
        aside .toggle .close{
            display: inline-block;
            cursor: pointer;
        }
    
        main{
            margin-top: 8rem;
            padding: 0 1rem;
        }
    
        main .new-users .user-list .user{
            flex-basis: 35%;
        }
    
        main .recent-orders{
            position: relative;
            margin: 3rem 0 0 0;
            width: 100%;
        }
    
        main .recent-orders table{
            width: 100%;
            margin: 0;
        }
    
        .right-section{
            width: 94%;
            margin: 0 auto 4rem;
        }
    
        .right-section .nav{
            position: fixed;
            top: 0;
            left: 0;
            align-items: center;
            background-color: var(--color-white);
            padding: 0 var(--padding-1);
            height: 4.6rem;
            width: 100%;
            z-index: 2;
            box-shadow: 0 1rem 1rem var(--color-light);
            margin: 0;
        }
    
        .right-section .nav .dark-mode{
            width: 4.4rem;
            position: absolute;
            left: 66%;
        }
    
        .right-section .profile .info{
            display: none;
        }
    
        .right-section .nav button{
            display: inline-block;
            background-color: transparent;
            cursor: pointer;
            color: var(--color-dark);
            position: absolute;
            left: 1rem;
        }
    
        .right-section .nav button span{
            font-size: 2rem;
        }
        .bt-add{
            max-height: 30px;
            max-width: 100px;
            font-size: 12px;
            align-items: center;
            justify-items: center;
            padding: 5px 4px;
        }
        .user h2{
            font-size: 12px;
        }
        .user p{
            font-size: 8px;
        }
        .add{
            max-width: 70px;
            height: auto;
        }
        .both{
            display: flex;
            flex-direction: column;
        }
        .both-ultra{
        margin-right: 0;
        width: 100%;
       
        margin-top: 5PX;
        margin-bottom: 5PX;
        display: flex;
        justify-content: space-around;
        align-items: left;
        justify-items: left;
        }
        .bt-add{
            width: 100%;
            height: 40px;
        }
        .responsive-br {
    display: block;
  }
    }
</style>
<script>
  export default {
  data() {
    return {
        
      Orders: [
        // Datos de los pacientes
        {
          nombre: 'Emmanuel Arturo Torres Santana',
          token: 'at85743',
          fecha: 'fecha',
          foto: 'foto'
        },
        {
          nombre: 'JoShua Aviles',
          token: 'kkd2332',
          fecha: 'fecha',
          foto: 'foto'
        },
        {
          nombre: 'Manuel Balan',
          token: 'j342426',
          fecha: 'fecha',
          foto: 'foto'
        }
      ],
      selectedOrder: null,
      searchTerm: '', // Término de búsqueda
      searchResults: [], // Resultados de búsqueda
      showSearchResults: false // Flag para mostrar/ocultar resultados de búsqueda
    };
  },
  mounted() {
    // Acceder al campo de búsqueda y agregar un listener de evento input
    const searchInput = document.getElementById("search");
    searchInput.addEventListener("input", this.filtrarResultados);
  },
  methods: {
    toggleSideMenu() {
      //abir menu
      const sideMenu = this.$refs.sideMenu;
      if (sideMenu) {
        sideMenu.style.display = 'block';
      }
    },
    closeSideMenu() {
    //cerar menu
      const sideMenu = this.$refs.sideMenu;
      if (sideMenu) {
        sideMenu.style.display = 'none';
      }
    },
    filtrarResultados() {
    const box_search = document.getElementById("box-search");
    const mensajeNoResultados = document.getElementById("mensajeNoResultados");
    // Filtrar los resultados basados en el término de búsqueda
    const searchTerm = event.target.value;
    this.searchResults = this.Orders.filter(order => {
        return order.nombre.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
               order.token.toLowerCase().includes(this.searchTerm.toLowerCase());
    });
    if (searchTerm === "") {
        box_search.style.display = "none";
        mensajeNoResultados.style.display = "none";
    } else if (this.searchResults.length > 0) {
        box_search.style.display = "block";
        mensajeNoResultados.style.display = "block"; // Oculta el mensaje de no resultados
    } else {
        box_search.style.display = "none";
        mensajeNoResultados.style.display = "block !important";
        console.log(mensajeNoResultados);
    }
  },
    showSelectedOrder(result)
    {
        const box_search = document.getElementById("box-search");
        this.selectedOrder = result;
        box_search.style.display = "none";
        this.searchTerm = '';
        }
    }
  };
  </script>