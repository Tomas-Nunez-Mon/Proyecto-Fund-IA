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


# Clase Nodo Sudoku
class NodoSudoku:
    def __init__(self, tablero, padre=None, costo=0):
        self.tablero = deepcopy(tablero)
        self.padre = padre
        self.costo = costo
    
    #crea una lista ordenada segun su valor f
    def __lt__(self, otroNodo):
        return self.costo < otroNodo.costo
    
    #ordena cada fila en una lista de strings comvirtiendo los numeros a str y los 0 en "." para tener un efecto visual mas comodo para los ojos
    def __str__(self):
        return '\n'.join(' '.join(str(x) if x != 0 else '.' for x in fila)for fila in self.tablero)  

    #permite identificar los nodos que son iguales
    def __eq__(self, otroNodo):
        return np.array_equal(self.tablero, otroNodo.tablero)   

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

    # se tiene una copia de la meta para cada Estado Base
    def esMeta(self):
        if inicial == NodoSudoku(Estado_base1):
            meta = np.array([
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]
            ])
            return np.array_equal(self.tablero, meta)
        
        elif inicial == NodoSudoku(Estado_base2):
            meta = np.array([
                [4, 3, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 9, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 4, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 2, 6, 8, 7, 4],
                [2, 4, 8, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 8, 2, 5, 9]
                ])
            return np.array_equal(self.tablero, meta)
        
        elif inicial == NodoSudoku(Estado_base3):
            meta = np.array([
                [9, 6, 2, 4, 3, 5, 8, 7, 1],
                [8, 1, 5, 2, 7, 6, 3, 4, 9],
                [4, 3, 7, 9, 8, 1, 2, 5, 6],
                [6, 5, 8, 7, 4, 9, 1, 3, 2],
                [7, 4, 3, 6, 1, 2, 5, 9, 8],
                [2, 9, 1, 3, 5, 8, 7, 6, 4],
                [5, 8, 6, 1, 9, 3, 4, 2, 7],
                [3, 2, 4, 8, 6, 7, 9, 1, 5],
                [1, 7, 9, 5, 2, 4, 6, 8, 3]
                ])
            return np.array_equal(self.tablero, meta)
        
        elif inicial == NodoSudoku(Estado_base4):
            meta = np.array([
                [1, 5, 7, 6, 4, 9, 3, 8, 2],
                [2, 8, 4, 3, 7, 5, 9, 1, 6],
                [3, 9, 6, 8, 2, 1, 4, 7, 5],
                [4, 1, 5, 2, 9, 6, 7, 3, 8],
                [7, 6, 3, 5, 1, 8, 2, 4, 9],
                [9, 2, 8, 4, 3, 7, 6, 5, 1],
                [6, 7, 2, 1, 5, 3, 8, 9, 4],
                [8, 3, 1, 9, 6, 4, 5, 2, 7],
                [5, 4, 9, 7, 8, 2, 1, 6, 3]
                ])
            return np.array_equal(self.tablero, meta)
        
        elif inicial == NodoSudoku(Estado_base5):
            meta = np.array([
                [2, 4, 3, 7, 8, 6, 9, 1, 5],
                [8, 6, 5, 3, 1, 9, 4, 2, 7],
                [7, 9, 1, 4, 5, 2, 6, 8, 3],
                [5, 8, 6, 9, 7, 4, 1, 3, 2],
                [4, 3, 7, 2, 6, 1, 5, 9, 8],
                [9, 1, 2, 8, 3, 5, 7, 6, 4],
                [6, 2, 9, 5, 4, 3, 8, 7, 1],
                [1, 5, 8, 6, 2, 7, 3, 4, 9],
                [3, 7, 4, 1, 9, 8, 2, 5, 6]
                ])
            return np.array_equal(self.tablero, meta)

#funciones copiadas del busqueda_no_informada_(puzzle_8).py
def ingresaLista(lista, nodo, esquema):
    if esquema == "BFS":
        lista.append(nodo)   
    if esquema == "DFS":
        lista.insert(0, nodo)    
    if esquema == "UCS":
        heappush(lista, nodo)
    return lista

def Solucion(nodo, inicial):
    solucion = []
    while nodo is not inicial:
        solucion = [str(nodo)] + solucion
        nodo = nodo.padre
    return [str(inicial)] + solucion

def busquedaNoInformada(nodoInicial, esquema):
    ABIERTOS = [nodoInicial]
    CERRADOS = []
    exito = False
    fracaso = False
    cont = 0
    while not exito and not fracaso:
        cont += 1

        if esquema == "UCS":
            nodoActual = heappop(ABIERTOS)
        else:
            nodoActual = ABIERTOS.pop(0)


        CERRADOS.append(nodoActual)
        if nodoActual.esMeta():
            exito = True
        else:
            listaSucesores = nodoActual.sucesores(ABIERTOS, CERRADOS)
            for nodo in listaSucesores:
                ABIERTOS = ingresaLista(ABIERTOS, nodo, esquema)
            if ABIERTOS == []:
                fracaso = True
    if exito:
        return Solucion(nodoActual, inicial), len(CERRADOS)
    else:
        return None
    
# bloque principal copiado del busqueda_no_informada_(puzzle_8).py
inicial = NodoSudoku(Estado_base5) #Estado_base1, Estado_base2, Estado_base3, Estado_base4, Estado_base5

esquema = "BFS"
respuesta, nodosRevisados = busquedaNoInformada(inicial, esquema)
if respuesta is None:
    print("No se encontró solución")
else:
    print(f"Cantidad de nodos revisados: {nodosRevisados} nodos")
    print(f"\nSolución encontrada por {esquema}: ")
    for nodo in respuesta:
        print(f"\n{nodo}")
    