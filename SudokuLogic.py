# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:31:13 2020

@author: manum
"""
tablero1 = {
    (0, 0): 1, (0, 1): 2, (0, 2): 3,    (0, 3): 4, (0, 4): 5, (0, 5): 6,    (0, 6): 7, (0, 7): 8, (0, 8): 9, 
    (1, 0): 4, (1, 1): 5, (1, 2): 6,    (1, 3): 7, (1, 4): 8, (1, 5): 9,    (1, 6): 1, (1, 7): 2, (1, 8): 3, 
    (2, 0): 7, (2, 1): 8, (2, 2): 9,    (2, 3): 1, (2, 4): 2, (2, 5): 3,    (2, 6): 4, (2, 7): 5, (2, 8): 6,

    (3, 0): 3, (3, 1): 1, (3, 2): 2,    (3, 3): 6, (3, 4): 4, (3, 5): 5,    (3, 6): 9, (3, 7): 7, (3, 8): 8, 
    (4, 0): 6, (4, 1): 4, (4, 2): 5,    (4, 3): 9, (4, 4): 7, (4, 5): 8,    (4, 6): 3, (4, 7): 1, (4, 8): 2, 
    (5, 0): 9, (5, 1): 7, (5, 2): 8,    (5, 3): 3, (5, 4): 1, (5, 5): 2,    (5, 6): 6, (5, 7): 4, (5, 8): 5, 

    (6, 0): 2, (6, 1): 3, (6, 2): 1,    (6, 3): 5, (6, 4): 6, (6, 5): 4,    (6, 6): 8, (6, 7): 9, (6, 8): 7, 
    (7, 0): 5, (7, 1): 6, (7, 2): 4,    (7, 3): 8, (7, 4): 9, (7, 5): 7,    (7, 6): 2, (7, 7): 3, (7, 8): 1, 
    (8, 0): 8, (8, 1): 9, (8, 2): 7,    (8, 3): 2, (8, 4): 3, (8, 5): 1,    (8, 6): 5, (8, 7): 6, (8, 8): 4,
    }

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

#tablero = makeSudoku()
#print(tablero)

def crearCuadrantesFilasColumnas(tablero):
    cuadrantes = dict()
    filas = dict()
    columnas = dict()

    ########################################
    # Crear cudrantes
    ########################################


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
        cuadrantes[cuadrante].append(tablero[fila, columna])

    ########################################
    # Crear filas
    ######################################## 

        # Revisar si la fila ya esta creada y si no crear la la lista para la fila
        filas[fila] = filas.get(fila, list())
        filas[fila].append(tablero[fila, columna])

    ########################################
    # Crear columnas
    ######################################## 

        # Revisar si la columna ya esta creada y si no crear la la lista para la columna
        columnas[columna] = columnas.get(columna, list())
        columnas[columna].append(tablero[fila, columna])       

    return cuadrantes, filas, columnas

print(crearCuadrantesFilasColumnas(tablero1))



def validarNumeros(dict1):
    '''Validar si filas, columnas o cuadrantes están completas y correctas'''
    for k, v in dict1.items():
        listaSuma = sum(v)
        if listaSuma != 45:
            return False
    return True

#Resolver tablero de sudoku automáticamente
cuadrantes, filas, columnas = crearCuadrantesFilasColumnas(tablero1)
if validarNumeros(cuadrantes) and validarNumeros(filas) and validarNumeros(columnas):
    print('El Sudoku está correcto')
else:
    print('El Sudoku está incorrecto o incompleto')
