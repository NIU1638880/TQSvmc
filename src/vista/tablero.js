
    // Obtén una referencia a la tabla
var table = document.querySelector('table');

    // Número de filas y columnas en la matriz
    var numRows = 5;
    var numCols = 5;

    // Genera las filas y celdas utilizando un bucle
    for (var i = 1; i <= numRows; i++) {
        var row = document.createElement('tr');
        for (var j = 1; j <= numCols; j++) {
            var cell = document.createElement('td');
            cell.textContent = i + ',' + j; // Contenido de la celda
            cell.id = 'cell-' + i + '-' + j; // ID de la celda
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
