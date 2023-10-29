

function coordenadasValidas(piece1, piece2, barcos, numRows, numCols) {
    let coordenadas1 = piece1.split(',');
    let coordenadas2 = piece2.split(',');

    // Comprobar que las coordenadas estén dentro del tablero
    if (coordenadas1[0] > numRows || coordenadas1[1] > numCols || coordenadas2[0] > numRows || coordenadas2[1] > numCols) {
        return false;
    }

    // Comprobar que no haya otro barco en las mismas coordenadas
    for (let barco of barcos) {
        if (barco.piece1 === piece1 || barco.piece2 === piece1 || barco.piece1 === piece2 || barco.piece2 === piece2) {
            return false;
        }
    }

    return true;
}

// Puedes añadir más funciones relacionadas con la lógica del juego aquí.
