import numpy as np
from copy import deepcopy
from heapq import heappush, heappop

#estados Bases
Estado_base1 = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
Estado_base2 = np.array([
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
])
Estado_base3 = np.array([
    [9, 0, 0, 0, 3, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 9],
    [0, 3, 0, 0, 8, 1, 0, 5, 0],
    [6, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 4, 0, 6, 0, 2, 5, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [5, 0, 0, 1, 0, 3, 4, 0, 0],
    [0, 0, 4, 0, 6, 7, 9, 0, 5],
    [1, 7, 0, 0, 0, 0, 6, 8, 3]
])
Estado_base4 = np.array([
    [0, 0, 7, 0, 0, 0, 3, 0, 2],
    [2, 0, 0, 0, 0, 5, 0, 1, 0],
    [0, 0, 0, 8, 0, 1, 4, 0, 0],
    [0, 1, 0, 0, 9, 6, 0, 0, 8],
    [7, 6, 0, 0, 0, 0, 0, 4, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 3, 0, 0, 0],
    [8, 0, 1, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 6, 3]
])
Estado_base5 = np.array([
    [0, 4, 0, 0, 0, 0, 0, 1, 5],
    [8, 0, 0, 3, 0, 0, 0, 2, 0],
    [7, 0, 1, 0, 0, 0, 6, 0, 0],
    [5, 0, 6, 0, 0, 0, 0, 3, 0],
    [0, 0, 7, 2, 0, 0, 0, 9, 0],
    [0, 0, 0, 0, 0, 5, 7, 0, 0],
    [6, 0, 9, 0, 4, 3, 8, 0, 0],
    [0, 0, 0, 6, 2, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 8, 2, 0, 6]
])

#Clase Nodo Sudoku
class NodoSudoku:
    def __init__(self, tablero, padre=None, costo=0):
        self.tablero = deepcopy(tablero)
        self.padre = padre
        self.costo = costo
        self.f = self.costo + self.heuristica()

    #crea una lista ordenada segun su valor f
    def __lt__(self, otroNodo):
        return self.f < otroNodo.f

    #ordena cada fila en una lista de strings comvirtiendo los numeros a str y los 0 en "." para tener un efecto visual mas comodo para los ojos
    def __str__(self):
        return '\n'.join(' '.join(str(x) if x != 0 else '.' for x in fila)for fila in self.tablero)
    
    #permite identificar los nodos que son iguales
    def __eq__(self, otroNodo):
        return np.array_equal(self.tablero, otroNodo.tablero)
    
    #cuenta la cantidad de de casillas vacias( vacias = 0)
    def heuristica(self):
        return np.sum(self.tablero == 0)
    
    # las reglas del sudoku y ademas valida los movimientos/ Nodos
    def aplicaReglas(self):
        for i in range(9):
            fila = [n for n in self.tablero[i, :] if n !=0]
            if len(fila) != len(set(fila)): return False
            columna = [n for n in self.tablero[:, i] if n != 0]
            if len(columna) != len(set(columna)): return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub = [n for n in self.tablero[i:i+3,j:j+3].flatten() if n != 0]
                if len(sub) != len(set(sub)): return False
        return True
    
    # se asegura que el tablero este completo pq sin la heuristica aca podrian tener ceros en el tablero final
    def esMeta(self):
        return self.heuristica() == 0 and self.aplicaReglas()
    
    def sucesores(self, ABIERTOS, CERRADOS):
        listaSucesores = []
        for i in range(9):
            for j in range(9):
                if self.tablero[i, j] == 0:
                    for num in range(1, 10):
                        nuevoTablero = deepcopy(self.tablero)
                        nuevoTablero[i, j] = num
                        nuevoNodo = NodoSudoku(nuevoTablero, self, self.costo + 1)
                        if nuevoNodo.aplicaReglas() and nuevoNodo not in ABIERTOS and nuevoNodo not in CERRADOS:
                            listaSucesores.append(nuevoNodo)
                    return listaSucesores
        return listaSucesores

#Funiciones A* copiadas del aestrella_(puzzle_8).py

def ingresaLista(lista, nodo):
    heappush(lista, nodo)
    return lista

def Solucion(nodo, inicial):
    solucion = []
    while nodo is not inicial:
        solucion = [str(nodo)] + solucion
        nodo = nodo.padre
    return [str(inicial)] + solucion

def Aestrella(nodoInicial):

    ABIERTOS = []
    heappush(ABIERTOS, nodoInicial)
    CERRADOS = []
    éxito = False
    fracaso = False
    cont = 0
    while not éxito and not fracaso and cont <= MAX:

        nodoActual = heappop(ABIERTOS)
        CERRADOS.append(nodoActual)

        if nodoActual.esMeta():
            éxito = True
        else:
            listaSucesores = nodoActual.sucesores(ABIERTOS, CERRADOS)
            for nodo in listaSucesores:
                heappush(ABIERTOS, nodo)
            if ABIERTOS == []:
                fracaso = True
        cont += 1
    if éxito:
        return Solucion(nodoActual, nodoInicial), cont
    else:
        return None, cont
    
# Bloque principal copiado del aestrella_(puzzle_8).py
inicial = NodoSudoku(Estado_base5) #Estado_base1, Estado_base2, Estado_base3, Estado_base4, Estado_base5

MAX = 30000

respuesta, nodosRevisados = Aestrella(inicial)
if respuesta is None:
    print(f"Cantidad de nodos revisados: {nodosRevisados} nodos")
    print("No se encontró solución")
else:
    print(f"Cantidad de nodos revisados: {nodosRevisados} nodos")
    for nodo in respuesta:
        print(f"\n{nodo}")
