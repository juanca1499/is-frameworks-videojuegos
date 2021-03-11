function muestraModal(url, titulo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = 
    `¿Deseas eliminar el Videojuego ${titulo}?`;
}