<template>
  <div class="container-fluid">
    <div class="row">
      <!-- Lado izquierdo con formulario de login -->

      <div class="col-md-6 bg-secondary p-4 d-flex align-items-center justify-content-center">
        <img src="@/assets/img.jpg" alt="Imagen de fondo" class="img-fluid">
      </div>


      <div class="col-md-6 bg-white p-4">
        <h2>Iniciar sesión</h2>
        <form @submit.prevent="handleSubmit">
          <div class="mb-3">
            <h2>Token</h2>
            <label for="token" class="form-label"></label>
            <input type="text" class="form-control" id="token" placeholder="token">
          </div>
          <div class="mb-3">
            <h2>Contraseña</h2>
            <label for="password" class="form-label" style="color: aqua;"></label>
            <input type="password" class="form-control" id="password" placeholder="contraseña">
          </div>
          <button type="submit" class="btn btn-primary">Iniciar sesión</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  methods: {
    handleSubmit() {
      // Navegar a otra ruta usando Vue Router
      this.$router.push('/galeria1');
    }
  }
  // Otros métodos y opciones del componente
}
</script>

<style>

@import url('./styles.css');
</style>