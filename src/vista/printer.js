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
    let form = document.getElementById(formId);

    let piece1 = convertirCoordenadas(form.elements["piece1"].value);
    let piece2 = convertirCoordenadas(form.elements["piece2"].value);

    let barco = {
        numeroBarco,
        piece1,
        piece2
    };

    if (coordenadasValidas(barco, barcos, numRows, numCols)) {
        // Lógica para guardar en el array de barcos
        barcos.push(barco);

        // Ejemplo de cómo pintar las celdas individualmente
        pintarCelda(piece1.x, piece1.y);
        pintarCelda(piece2.x, piece2.y);

        // Comprobación de que se guardan los barcos
        console.log(barcos);
    } else {
        console.log('Coordenadas inválidas o ya ocupadas.');
    }
}

function convertirCoordenadas(coordenadaStr) {
    let partes = coordenadaStr.split(',');
    return {
        x: parseInt(partes[0], 10),
        y: parseInt(partes[1], 10)
    };
}
