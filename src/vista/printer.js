
function pintarCelda(fila, columna) {
    var cell = document.getElementById('cell-' + fila + '-' + columna);
    if (cell) {
        cell.style.backgroundColor = "blue"; // Cambia el color a azul u otro color de tu elección
    } else {
        console.log('La celda no existe');
    }
}

let barcos = [];

function guardarBarco(numeroBarco) {
    let formId = "form" + numeroBarco;
    let form = document.getElementById('form' + numeroBarco);
    let piece1 = form.elements["piece1"].value;
    let piece2 = form.elements["piece2"].value;

    // Agregar lógica para validar las coordenadas
    if (!coordenadasValidas(piece1, piece2, barcos, numRows, numCols)) {
        alert('Las coordenadas no son válidas');
        return;
    }

    form.innerHTML = "El barco se ha colocado correctamente.";
    barcos.push([numeroBarco, piece1, piece2]);

    // Ejemplo de cómo pintar las celdas individualmente
    let coordenadas1 = piece1.split(',');
    let coordenadas2 = piece2.split(',');
    pintarCelda(coordenadas1[0], coordenadas1[1]);
    pintarCelda(coordenadas2[0], coordenadas2[1]);
}