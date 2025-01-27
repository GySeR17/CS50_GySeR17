"""
Para las matrices se utilizan listas dentro de listas, para generar filas y columnas.
"""
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matriz)
fila = int(input("Ingrese la fila a verificar: "))
col = int(input("Ingrese la columna a verificar: "))
print(f"{matriz[fila][col]}\n\n")

matriz2 = [[[1,2],[3,4]],
           [[5,6],[7,8]]]
print(matriz2)
fila2 = int(input("Ingrese la fila a verificar: "))
col2 = int(input("Ingrese la columna a verificar: "))
num2 = int(input("Ingrese 0 o 1 para verificar el valor: "))
print(matriz2[fila2][col2][num2])

#tuplas
numeros = (7,8,9,10,[11,12]) #Tupla originalmente inmutable, sin embargo si existe una lista dentro de la tupla, esta lista puede ser modificada.
print(numeros) #Verificamos los datos de la tupla.
print(type(numeros)) #Verificamos el tipo de la tupla.
print(numeros[4]) #Verifica solamente la lista.
print(type(numeros[4])) #Verifica el tipo de la lista.
numeros[4][1] = 15 #Reemplazando el valor [1] de la lista [4]
print(numeros) #Verifica los nuevos valores de la tupla

"""
'We can include list inside tuples'
numbers2 = (7,8,9,10,[11,12])
print(numbers2)
print(numbers2[4])
print(type(numbers2[4]))  # list
# numbers2[4] = [20,40] -----> Gives error since they are inmutable
numbers2[4][1] = 2
print(numbers2)
'''No podemos cambiar la tupla pero si podemos modificar las variables que se 
 encuentran dentro de la lista que a su vez esta incluida en la tupla'''
"""

#Imprimiendo un tablero de ajedrez donde las fichas son las letras:
#Fichas blancas con mayusculas y las negras con minusculas.
chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
for fila in chess_board: #Para cada fila en el tablero de ajedrez.
    for pieza in fila: #Para cada pieza en la fila del tablero.
        print(pieza, end= "") #imprimir la pieza, sin salto de pagina "end="" ".
    print() #Imprimir un salto de fila cuando se acabe de imprimir las piezas.

"""Si queremos mover alguna ficha del tablero, debemos tener en cuenta las configuraciones y posibilidades de cada ficha
Por ejemplo moveremos la ficha de caballo de la posicion (7,6) y debemos verificar los posibles movimientos que puede realizar el caballo (N)
Tomando en cuenta las posibles posiciones finales del caballo pueden ser: (5,7), (5,5) y (6,5), sin embargo esta ultima posicion esta ocupada 
con una ficha, de modo que no puedde ser ubicado el caballo en esa posicion.
"""
chess_board[7][6] = 0
chess_board[5][7] = "N" #Moveremos el caballo (N) a laa posicion (5,7).
print() #Solo para diferenciar el tablero inicial del final.
for fila in chess_board:
    for pieza in fila:
        print(pieza, end= "")
    print()
