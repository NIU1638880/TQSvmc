function coordenadasValidas(piece1, piece2, barcos, numRows, numCols) {
    let coordenadas1 = piece1.split(',').map(coordinate => parseInt(coordinate.trim()));
    let coordenadas2 = piece2.split(',').map(coordinate => parseInt(coordinate.trim()));

    // Comprobar que las dos piezas no sean iguales
    if(coordenadas1[0] === coordenadas2[0] && coordenadas1[1] === coordenadas2[1]){
        return false;
    }

    // Asegurarse de que las dos piezas sean adyacentes
    let deltaX = Math.abs(coordenadas1[0] - coordenadas2[0]);
    let deltaY = Math.abs(coordenadas1[1] - coordenadas2[1]);
    if (!(deltaX <= 1 && deltaY <= 1) || (deltaX === 1 && deltaY === 1)) {
        return false; // Esto excluye diagonales
    }

    // Comprobar que las coordenadas estén dentro del tablero
    if (coordenadas1[0] < 0 || coordenadas1[0] > numRows || coordenadas1[1] < 0 || coordenadas1[1] > numCols ||
        coordenadas2[0] < 0 || coordenadas2[0] > numRows || coordenadas2[1] < 0 || coordenadas2[1] > numCols) {
        return false;
    }

    // Comprobar que no haya otro barco en las mismas coordenadas
    for (let barco of barcos) {
        if ((coordenadas1[0] === parseInt(barco[1][0]) && coordenadas1[1] === parseInt(barco[1][1])) ||
            (coordenadas2[0] === parseInt(barco[2][0]) && coordenadas2[1] === parseInt(barco[2][1]))) {
            return false;
        }
    }

    return true;
}
