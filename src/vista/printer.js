function pintarCelda(fila, columna) {
    var cell = document.getElementById('cell-' + fila + '-' + columna);
    if (cell) {
        cell.classList.add('pintada');
    }
}
