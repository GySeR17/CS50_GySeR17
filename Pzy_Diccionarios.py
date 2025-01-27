palabras = ["manzana", "banana", "naranja", "manzana", "banana"] #Teniendo una lista con elementos incluso repetidos, crearemos un diccionario llamado contador.
contador = {} #Contador inicialmente no tendra ningun valor asignado o predefinido.
for palabra in palabras: #Para la variable palabra tomando en cuenta la lista "palabras"
    if palabra in contador: #si la variable palabra esta ya en contador
        contador[palabra] += 1 #Se suma en uno la palabra ya establecida.
    else:
        contador[palabra] = 1 #Se mantiene con uno
print("Contador de palabras:", contador)
print(contador['manzana'])
print(contador['banana'])

"""
# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}
print("Datos del libro:", libro)

# Datos en formato JSON
import json
json_data = json.dumps(libro)
print("Datos en JSON:", json_data)

Configuración de una Aplicación:
Se crea un diccionario para almacenar configuraciones de una aplicación.
Contador de Palabras:
Se utiliza un diccionario para contar la frecuencia de palabras en una lista.
Mapeo de Usuarios a Datos:
Se crea un diccionario para mapear identificadores de usuarios a sus datos personales.
Almacenamiento de Datos Estructurados:
Se almacena información de un libro en un diccionario
Formato JSON:
Se convierte un diccionario a una cadena JSON utilizando el módulo json.
"""