# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:31:13 2020

@author: manum
"""

def makeSudoku():
    tablero = dict()
    adelantar = 0
    for fila in range(9):
        n = adelantar + 1
        for columna in range(9):
            tablero[fila, columna] = n
            if n == 9:
                n = 1
            else:
                n += 1
            
        adelantar = (adelantar + 3)%9
    return tablero

tablero = makeSudoku()
print(tablero)

def crearCuadrantesFilasColumnas(tablero):
    cuadrantes = dict()
    filas = dict()
    columnas = dict()

    # cuadrantes del sudoku:
    #   1, 2, 3
    #   4, 5, 6
    #   7, 8, 9
    # cuadranteF: Fila en la que se hace un cambio de cuadrante
    # cuadranteC: Columna en la que se hace un cambio de cuadrante
    cuadranteF = 0
    cuadranteC = 1


    # loop por cada  celda del tablero
    for fila, columna in tablero:

        # Revisar si la fila pasó las 3 filas correspondientes a un cuadrante
        if fila%3 == 0 and fila>0:
            # Sumar 3 cada vez se pasen 3 filas para designar el numero del cuadrante
            cuadranteF = fila//3*3

        # Revisar si la columna pasó las 3 columnas correspondientes a un cuadrante
        if columna%3 == 0:
            cuadranteC = columna//3 + 1
        
        # Determinar numero del cuadrante 
        cuadrante = cuadranteF + cuadranteC
        # Agregar la posicion de la celda al cuadrante correspondiente
        cuadrantes[cuadrante] = cuadrantes.get(cuadrante, list())
        cuadrantes[cuadrante].append((fila, columna))        

    return cuadrantes

print(crearCuadrantesFilasColumnas(tablero))