const csvtojson = require("csvtojson");

// Función para leer un archivo CSV y convertirlo en un objeto JSON
function parseCSV(filename) {
    return csvtojson.parse(filename);
}
// Lee el archivo CSV
const data = parseCSV("../model/datos.csv");

// Imprime los datos del CSV
console.log(data);
