Integrantes:
-Tomás Núñez Montagna integrante 1 (NRC: 8062)
-Bastián Ibañez Martínez integrante 2 (NRC: 8062)

Nombre del Juego: Sudoku
Link: https://sudoku.com/es/experto/

Heuristica Iplementada
Codigo:
def heuristica(self):
        return np.sum(self.tablero == 0)

def esMeta(self):
        return self.heuristica() == 0 and self.aplicaReglas()

Explicacion:
La funcion Heuristica toma cada casilla de la matriz y devuelve "False"(0) si hay un numero distinto a cero
y devuelve "True"(1) si el numero es cero, con la funcion np.sum suma todos los True que hay, asi contando todas las casillas por rellenar.
La funcion esMeta utiliza La funcion heuristica para corroborar que no hayan casillas vacias y aplica las reglas del sudoku
1. No pueden haber numeros repetidos en las filas.
2. No pueden haber numeros repetidos en las columnas.
3. No pueden haber numeros repetidos en los 3x3.

Estado_base1
    [5, 3, 0, 0, 7, 0, 0, 0, 0]
    [6, 0, 0, 1, 9, 5, 0, 0, 0]
    [0, 9, 8, 0, 0, 0, 0, 6, 0]
    [8, 0, 0, 0, 6, 0, 0, 0, 3]
    [4, 0, 0, 8, 0, 3, 0, 0, 1]
    [7, 0, 0, 0, 2, 0, 0, 0, 6]
    [0, 6, 0, 0, 0, 0, 2, 8, 0]
    [0, 0, 0, 4, 1, 9, 0, 0, 5]
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
N° nodos revisados A*: 2.866 nodos
N° nodos revisados BFS: 4.632 Nodos

Estado_base2
    [0, 0, 0, 2, 6, 0, 7, 0, 1]
    [6, 8, 0, 0, 7, 0, 0, 9, 0]
    [1, 9, 0, 0, 0, 4, 5, 0, 0]
    [8, 2, 0, 1, 0, 0, 0, 4, 0]
    [0, 0, 4, 6, 0, 2, 9, 0, 0]
    [0, 5, 0, 0, 0, 3, 0, 2, 8]
    [0, 0, 9, 3, 0, 0, 0, 7, 4]
    [0, 4, 0, 0, 5, 0, 0, 3, 6]
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
N° nodos revisados A*: 69 nodos
N° nodos revisados BFS: 69 nodos

Estado_base3
    [9, 0, 0, 0, 3, 5, 0, 0, 0]
    [0, 0, 0, 0, 0, 0, 0, 4, 9]
    [0, 3, 0, 0, 8, 1, 0, 5, 0]
    [6, 0, 0, 0, 0, 9, 0, 0, 0]
    [0, 4, 0, 6, 0, 2, 5, 0, 0]
    [0, 0, 0, 0, 5, 0, 0, 0, 0]
    [5, 0, 0, 1, 0, 3, 4, 0, 0]
    [0, 0, 4, 0, 6, 7, 9, 0, 5]
    [1, 7, 0, 0, 0, 0, 6, 8, 3]
N° nodos revisados A*: 6.481 nodos
N° nodos revisados BFS: 24.388 nodos

Estado_base4
    [0, 0, 7, 0, 0, 0, 3, 0, 2]
    [2, 0, 0, 0, 0, 5, 0, 1, 0]
    [0, 0, 0, 8, 0, 1, 4, 0, 0]
    [0, 1, 0, 0, 9, 6, 0, 0, 8]
    [7, 6, 0, 0, 0, 0, 0, 4, 9]
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    [0, 0, 0, 1, 0, 3, 0, 0, 0]
    [8, 0, 1, 0, 6, 0, 0, 0, 0]
    [0, 0, 0, 7, 0, 0, 0, 6, 3]
N° nodos revisados A*: 8.932 nodos
N° nodos revisados BFS: 18.264 nodos

Estado_base5
    [0, 4, 0, 0, 0, 0, 0, 1, 5]
    [8, 0, 0, 3, 0, 0, 0, 2, 0]
    [7, 0, 1, 0, 0, 0, 6, 0, 0]
    [5, 0, 6, 0, 0, 0, 0, 3, 0]
    [0, 0, 7, 2, 0, 0, 0, 9, 0]
    [0, 0, 0, 0, 0, 5, 7, 0, 0]
    [6, 0, 9, 0, 4, 3, 8, 0, 0]
    [0, 0, 0, 6, 2, 0, 0, 0, 0]
    [3, 0, 0, 0, 0, 8, 2, 0, 6]
N° nodos revisados A*: 316 nodos
N° nodos revisados BFS: 4.767 nodos