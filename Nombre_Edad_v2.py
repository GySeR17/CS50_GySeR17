#Pedir al usuario su nombre y comprobar que sea un string
while True:
        nombre = input("Ingresa tu nombre: ")
        if isinstance(nombre, str) and nombre.strip():
            nombre = nombre.title()
            break
        else:
            print("El nombre debe ser una palabra, intentalo de nuevo")

#Pedir la edad y comprobar si la edad es un numero
while True:
    try:
        edad = round(float(input("Ingresa tu edad: ")),0)
        edad = int(edad)
        break #Si la edad es un numero, salimos del bucle
    except ValueError:
        print("El valor ingresado no es un numero")

#Imprimimos el nombre y la edad
print(f"Tu nombre es {nombre} y tu edad es de {edad} años")