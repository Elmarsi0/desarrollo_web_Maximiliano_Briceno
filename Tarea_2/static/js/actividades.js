function openModalWithImage(src) {
    document.getElementById("imgModal").src = src;
    document.getElementById("modal").style.display = "block";
}

// Cierra el modal
function closeModal() {
    document.getElementById("modal").style.display = "none";
}

// Asigna eventos a todas las imágenes con la clase 'imagenes'
document.addEventListener("DOMContentLoaded", () => {
    const zoom = document.querySelectorAll("img.imagenes");
    zoom.forEach(img => {
        img.addEventListener("click", () => {
            const fullSrc = img.getAttribute("data-full");
            openModalWithImage(fullSrc);
        });
    });
});