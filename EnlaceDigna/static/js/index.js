document.addEventListener("DOMContentLoaded", function() {
    // Asumiendo que tienes varios formularios para subir archivos, escuchamos a todos ellos
    document.querySelectorAll('.both').forEach(form => {
        form.addEventListener("submit", function(e) {
            e.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

            // Crea una instancia de FormData para capturar los datos del formulario
            const formData = new FormData(form);
            
            // Asegúrate de que el nombre 'archivo' coincida con el nombre esperado por tu API
            // y 'files[]' es el nombre del input de archivo en tu formulario
            const filesInput = form.querySelector('input[type="file"]');
            if (filesInput.files.length > 0) {
                // Verifica si el archivo ya se ha enviado antes
                if (!formData.has('archivo')) {
                    formData.append('archivo', filesInput.files[0]); // Añade el primer archivo seleccionado
                }
            }

            // Opcional: Añade cualquier otro dato que tu API requiera
            // formData.append('tipo_ultrasonido', 'El tipo aquí');
            // formData.append('fecha', 'La fecha aquí');
     
            const id = formData.get('cliente_id');
            
            fetch(`../enviar_whats/${id}/`, { // Utiliza comillas inversas (`) para la cadena de plantilla
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json(); // Procesamos la respuesta JSON
            })
            .then(data => {
                console.log(data); // Hacemos algo con la respuesta del servidor
            })
            .catch(error => {
                console.error('There was a problem with your fetch operation:', error);
            });

            // Realiza la solicitud para cargar el archivo
            fetch('../upload/', { // Reemplaza con la URL real de tu API
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                // Aquí puedes manejar la respuesta de tu API, como actualizar la interfaz con el archivo subido
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });
});
