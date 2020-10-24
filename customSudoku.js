function limpiarTablero(tablero) {
    // Leer HTML del tablero
    filasE = tablero.children;
    // Iterar por cada fila
    for (let f=0; f < filasE.length; f++) {
        const columnas = filasE[f].children;
        // iterar por cada columna
        for (let c=0; c < columnas.length; c++) {
            const celdas = columnas[c].children;
            const tipoCelda = celdas[0].tagName;
            // Convertir todas las casillas del sudoku a input
            if (tipoCelda === 'DIV') {
                columnas[c].innerHTML = `
                <input type='text' class="celda" id="fila${f+1}columna${c+1}">
                `;
            }
        }
    }
}

function fijarNuevoTablero(tablero) {
    // Leer HTML del tablero
    filasE = tablero.children;
    // Iterar por cada fila
    for (let f=0; f < filasE.length; f++) {
        const columnas = filasE[f].children;
        // iterar por cada columna
        for (let c=0; c < columnas.length; c++) {
            const celdas = columnas[c].children;
            // Convertir todas las casillas del sudoku a input
            if (celdas[0].value != '') {
                columnas[c].innerHTML = `
                <div class="celda" id="fila${f+1}columna${c+1}">${celdas[0].value}</div>
                `;
            }
        }
    }
}

// Crear variable con el boton crear un tablero de sudoku propio
let botonSudokuPropio = document.getElementById('crearSudoku');

// Limpiar tablero para que el usuario cree su sudoku
botonSudokuPropio.addEventListener('click', (e)=>{
    const divFijar = document.getElementById('fijarTablero');
    tablero = document.getElementById('tableroSudoku');
    limpiarTablero(tablero);
    // Crear boton para fijar tablero
    const botonFijar = document.createElement('button');
    botonFijar.className = 'playButtons';
    botonFijar.id = 'botonFijar';
    botonFijar.innerHTML = 'Fijar nuevo tablero de sudoku'
    // Agregar evento para cuando se haga click en el boton
    botonFijar.addEventListener('click', (e) => {
        fijarNuevoTablero(tablero);
        e.target.remove();
    });
    // Agregar botón a div
    divFijar.appendChild(botonFijar);
});

