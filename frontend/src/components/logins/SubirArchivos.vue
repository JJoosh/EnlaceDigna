<template>
  <form class="both" action="/upload" method="post" enctype="multipart/form-data" id="uploadForm">
    <label for="files" class="custom-upload-button">
      <i class="fa-solid fa-image"></i> Subir archivos
    </label>
    <input type="file" name="files[]" id="files" multiple accept="image/*, video/*" style="display: none;">
  </form>
</template>

<style>
/* *{
  background-color: #e6efe7;
  width: 100vh;
}
.both{
  background-color: #fff;
        width: 100%;
        padding: 1.8rem;
        text-align: center;
        box-shadow:  0 2rem 3rem rgba(132, 139, 200, 0.18);
        border-radius: 20px;
        transition: all 0.3s ease;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 1.4rem;
        cursor: pointer;
        align-items: left;
        justify-content: left;
        margin: 30px 10%
}

.custom-upload-button {
  display: inline-block;
  cursor: pointer;
  padding: 10px 20px;
  background-color: #9ca0a3;
  color: #fff;
  border-radius: 5px;
}

.custom-upload-button:hover {
  background-color: #9ca0a3;
} */
</style>
