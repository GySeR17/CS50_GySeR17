#Pedir al usuario su nombre
nombre = input("Ingresa tu nombre: ")

#Pedir la edad y comprobar si la edad es un numero
while True:
    try:
        edad = round(float(input("Ingresa tu edad: ")),0)
        edad = int(edad)
        break #Si la edad es un numero, salimos del bucle
    except ValueError:
        print("El valor ingresado no es un numero")

#Validacion el nombre
if isinstance(nombre, str) and nombre.strip(): #El metodo ".strip" para verificar que no este vacio
    print(f"Tu nombre es {nombre.title()} y tu edad es de {edad} años")
else:
    print("El nombre debe ser una palabra, intentalo de nuevo")