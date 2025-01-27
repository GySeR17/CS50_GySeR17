"""
Listas y su posible metodo de copiado y su espacio (id) en memoria.
"""
a = [2,5,6,7,9]
print(a) #Verificamos que es una lista
print(a) #Verificamos el id de la lista a
b = a #"copiamos" la lista "a" a la lista "b"
print(type(b)) #Verificamos que es una lista
print(id(a))
print(id(b)) #Verificamos el id de la lista a es exactamente igual a la lista b, 
             #lo que quiere decir que todos los cambios que sufra la lista a se
             #veran reflejados en la lista b(indeseable en ciertos casos)
a.append(10)
print(a)
print(b)
c = a[:] #Hacemos un slicing de la lista a desde el 1er numero hasta el ultimo con ":"
print(c) #Verificamos la copia de la lista a incluso con el numero añadido "10", por el orden de la accion
a.append(20)
print(f"Lista a añadiendo 20={a}")
print(f"Lista c con slicing sin el 20={c}")
print(f"Lista a={id(a)}")
print(f"Lista c={id(c)}")
"""
Sintaxis básica:

La sintaxis general para crear un slice en Python es la siguiente:
secuencia[inicio:fin:paso]

inicio: Índice donde comienza el slice (incluido).
fin: Índice donde termina el slice (excluido).
paso: Tamaño del incremento entre elementos del slice (opcional).
Ejemplos de uso:Supongamos que tenemos una lista de números:
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Copia completa de la lista:resultado = 
numeros[:] # Resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Obtener los primeros tres elementos:
primeros_tres = numeros[:3] # Resultado: [0, 1, 2]

Obtener todos los elementos desde el tercer elemento en adelante:
desde_tercero = numeros[2:] # Resultado: [2, 3, 4, 5, 6, 7, 8, 9]

Obtener todos los elementos con un paso de 2:
con_paso_dos = numeros[::2] # Resultado: [0, 2, 4, 6, 8]

Índices negativos: Podemos usar índices negativos para referirnos a elementos desde el final de la secuencia:
ultimos_tres = numeros[-3:] # Resultado: [7, 8, 9]

primeros_salvo_tres = numeros[:-3] # Resultado: [0, 1, 2, 3, 4, 5, 6]

Modificar valores con Slices: También podemos usar Slices para modificar valores en una secuencia:
frutas = ["manzana", "banana", "cereza", "dátil", "uva"] 
frutas[1:3] = ["pera", "naranja"] # Reemplaza "banana" y "cereza" por "pera" y "naranja"
"""