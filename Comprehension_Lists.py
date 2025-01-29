squares = [a ** 2 for a in range(1,11)] #Genera lista de cuadrados de cada numero desde el 1 al 10
cubes = [b ** 3 for b in range(1,11)]
#print(f"Los cuadrados son: {squares}")
#print(f"Los cuadrados son: {cubes}")

#Convertidor de temperaturas
celsius = [(c * 10) + 5 for c in range(1,7)] #Generando la lista de temperaturas
fahrenheit = [(temp * 9 / 5) + 32 for temp in celsius] #El "range" no es necesario al ser una lista
print(f"La temperatura en °C: {celsius} ==> °F: {fahrenheit}")

#Numeros pares e impares
even = [d for d in range(1,22) if d % 2 == 0]
odd = [e for e in range(1,22) if e % 2 != 0]
print(f"Los numeros pares son: {even}")
print(f"Los numeros impares son: {odd}")

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))] #Leyendo de derecha a izquierda (forma normal de escribir), para i en el rango de longitud y posicion 
# de la matriz original ==> para cada fila en matriz se debe generar un valor representado por "fila[i]"
"""Leyendo de izquierda a derecha: necesitamos el valor que tomara la matriz transpuesta "fila[i]" (importante denotar que este valor debe estar encerrado entre [] ya que tiene 
que tener varias filas(listas), para fila en matriz para i(el valor de transpuesta) en el rango de la matriz "len(matriz[0])" (pero de posicion y longitud de la original). """
print(matriz)
print(transpuesta)