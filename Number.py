#try:
#    x = int(input("What's x? "))
#    print(f"x is {x}")
#except ValueError:
#    print("Please enter a integer number.")
#El programa termina independientemente del mensaje de error avisando que x no es un numero

#try:
 #   x = int(input("What's x? "))
#except ValueError:
 #   print("Please enter a integer number.")

#print(f"x is {x}")
#El programa funcionara bien SIEMPRE Y CUANDO x sea numero, de otra forma debido a la funcion int la variable x no puede ser definida, causando un error "NameError"

#Para que el programa se siga ejecutando de manera continua, independiente de si el valor  de x es un integer o no y este pida el input al usuario:
#while True: #Mientras sea verdadera alguna opcion dentro del loop while
    #try: #Intenta:...
    #    x = int(input("What's x? ")) #Pedir un numero
   # except ValueError: #En caso de que el valor de x no sea un numero (se introduzca un string)
  #      print("Please enter a integer number.")
  #  else: #Sino:...
 #       break #El loop al detectar que x es un valor integer valido, el loop se rompe y salimos para seguir con el programa
#print(f"x is {x}") #Se ejecuta en este caso la funcion print, que puede ser en realidad cualquier funcion deseada.

#Un poco mas condensado
#while True:
    #try:
    #    x = int(input("What's x? ")) #Pedir un numero
   #     break
  #  except ValueError:
 #       print("Please enter a integer number.")
#print(f"x is {x}")

#Para generar una funcion para ser utilizada en algun momento en el futuro y que este sea escalable y replicable.
#def main():
  #  x = get_int() #Generar una variable con la cual poder mostrar o asignar el valor necesario para usarlo de alguna manera //(2)Notar que la funcion get_int() esta siendo llamada aqui arriba de modo que esta se cierra
 #   print(f"x is {x}")

#def get_int(): #Definir funcion //(1)
    #while True:
      #  try:
     #       x = int(input("What's x? "))  # Pedir un numero
    #        break
   #     except ValueError:
  #          print("Please enter a integer number.")
 #   return x #Una vez creada la funcion el proposito de la misma no solo debe ser "imprimir" el valor, sino esta debe entregar un valor de retorno para que sea realmente util
#main()

#Mio tratando de condensar el codigo:
def main():
    x = get_int() #Generar una variable con la cual poder mostrar o asignar el valor necesario para usarlo de alguna manera //(2)Notar que la funcion get_int() esta siendo llamada aqui arriba de modo que esta se cierra
    print(f"x is {x}")

def get_int(): #Definir funcion //(1)
    while True:
        try:
            x = int(input("What's x? "))  # Pedir un numero
            return x
        except ValueError:
            print("Please enter a integer number.")

main()

#Cs50 David: Indicando que si la variable x en try es solo usada una vez, directamente se podria usar el return para terminar el loop y ademas retornar el valor ingresado Min 4:43:00
#def main():
  #  x = get_int()
 #   print(f"x is {x}")

#def get_int():
    #while True:
   #     try:
  #          return int(input("What's x? "))
 #       except ValueError:
#            print("Please enter a integer number.")
#main()
#CS50 David con pass
def main2():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
main2()
#Codigo con un valor agregado de reusabilidad de la pregunta
def main2():
    x = get_int("What's x? ") #Hace la pregunta en base al parametro que tomara la funcion ("What's x?" )
    print(f"x is {x}")

def get_int(prompt): #Definimos el parametro con una variable que podamos reutilizar
    while True:
        try:
            return int(input(prompt)) #Usamos el parametro para que tome el valor en la funcion arriba
        except ValueError:
            pass
main2()