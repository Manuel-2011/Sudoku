// Crear variable con el tablero para agregrar eventos
let tablero = document.getElementById('tableroSudoku');
// Crear variable global con los valores del tablero
let valoresTablero = {};

// Cuando se haga click en el tablero llamar función de leer el tablero
tablero.addEventListener('click', (e)=>{
    tablero = document.getElementById('tableroSudoku');
    readSudoku(tablero);
});

// funcion de leer los valores del tablero
function readSudoku(tablero) {
    // Reiniciar objeto con los valores del tablero
    valoresTablero = {};

    filasE = tablero.children;
    // Iterar por cada fila
    for (let f=0; f < filasE.length; f++) {
        const columnas = filasE[f].children;
        // iterar por cada columna
        for (let c=0; c < columnas.length; c++) {
            const celdas = columnas[c].children;
            const tipoCelda = celdas[0].tagName;
            // Guardar el valor de la casilla junto con la fila y su columna
            valoresTablero[`(${f},${c})`] = {};
            if (tipoCelda === 'DIV') {
                valoresTablero[`(${f},${c})`]['valor'] = celdas[0].innerHTML;
            } else {
                valoresTablero[`(${f},${c})`]['valor'] = celdas[0].value;
            }
            valoresTablero[`(${f},${c})`]['fila'] = f;
            valoresTablero[`(${f},${c})`]['columna'] = c;
        }
    }
    console.log(valoresTablero);
    evaluateSudoku(valoresTablero);
}