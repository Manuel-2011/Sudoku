// Crear variable con el tablero para agregrar eventos
const tablero = document.getElementById('tableroSudoku');
// Crear variable global con los valores del tablero
let valoresTablero = {};

// Cuando se haga click en el tablero llamar función de leer el tablero
tablero.addEventListener('click', (e)=>{
    readSudoku(tablero);
});

// funcion de leer los valores del tablero
function readSudoku(tablero) {
    filas = tablero.children;
    // Iterar por cada fila
    for (let f=0; f < filas.length; f++) {
        const columnas = filas[f].children;
        // iterar por cada columna
        for (let c=0; c < columnas.length; c++) {
            const celdas = columnas[c].children;
            // Guardar el valor de la casilla junto con la fila y su columna
            valoresTablero[`(${f},${c})`] = {};
            valoresTablero[`(${f},${c})`]['valor'] = celdas[0].innerHTML;
            valoresTablero[`(${f},${c})`]['fila'] = f;
            valoresTablero[`(${f},${c})`]['columna'] = c;
        }
    }
    evaluateSudoku(valoresTablero);
}