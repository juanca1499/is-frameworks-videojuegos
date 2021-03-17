function muestraModal(url, caption){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = 
    `Está seguro que desea eliminar ${caption}?`;
}

// Aquí usamos JQuery (que es un Framework de JavaScript)
$('#id_estado').on('change', function () { 
    alert('Hola');
    alert(this.value)
});