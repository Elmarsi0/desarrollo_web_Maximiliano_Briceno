document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form-comentario");
    const errorDiv = document.getElementById("mensaje-error");
    const listaComentarios = document.getElementById("lista-comentarios");
    const actividadId = parseInt(document.getElementById("actividad-id").value);

    const cargarComentarios = () => {
        fetch(`/api/comentarios/${actividadId}`)
            .then(res => res.json())
            .then(data => {
                listaComentarios.innerHTML = "";
                data.forEach(com => {
                    const item = document.createElement("li");
                    item.textContent = `${com.fecha} - ${com.nombre}: ${com.texto}`;
                    listaComentarios.appendChild(item);
                });
            });
        };
    cargarComentarios();

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        console.log("Submit interceptado por JS");
        errorDiv.textContent = "";

        const nombre = document.getElementById("nombre").value.trim();
        const texto = document.getElementById("texto").value.trim();

        if (nombre.length < 3 || nombre.length > 80 || texto.length < 5) {
            errorDiv.textContent = "Revisa los campos: el nombre debe tener entre 3 y 80 caracteres y el comentario al menos 5.";
            return;
        }

        // Crear nuevo forms
        const formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            body: formData
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            } else {
                return response.text().then(text => {
                    errorDiv.textContent = "Error al enviar el comentario.";
                    console.error("Respuesta inesperada:", text);
                });
            }
        })
        .catch(error => {
            errorDiv.textContent = "Error de conexión al enviar comentario.";
            console.error("Error en fetch:", error);
        });
    });
});