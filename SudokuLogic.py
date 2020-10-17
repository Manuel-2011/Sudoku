# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:31:13 2020

@author: manum
"""

def makeSudoku():
    tablero = []
    adelantar = 0
    for fila in range(9):
        n = adelantar + 1
        tablero.append(list())
        for columna in range(9):
            tablero[fila].append(n)
            if n == 9:
                n = 1
            else:
                n += 1
            
        adelantar = (adelantar + 3)%9
    return tablero

tablero = makeSudoku()
print(tablero)

def evaluarCuadrantes(tablero):
    cuadrantes = dict()
    cuadranteF = 1
    cuadranteC = 0
    indiceF = 1
    for fila in tablero:
        
        indiceC = 1
        for celda in fila:
            cuadrante = cuadranteF + cuadranteC
            cuadrantes[cuadrante] = cuadrantes.get(cuadrante, list())
            cuadrantes[cuadrante].append(celda)
            if indiceC%3 == 0:
                cuadranteC +=1
            indiceC += 1
        
        if indiceF%3 == 0:
            cuadranteF += 3
            
        cuadranteC = 0
        indiceF += 1

print(evaluarCuadrantes(tablero))