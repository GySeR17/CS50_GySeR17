def main():

    x = int(input("Enter a number: "))
    if is_even(x)==True: #la expresion "== True" puede ser eliminada ya que python sobreentiende que si es verdad el retorno definido debajo esta es redundante
        print("The number is even") #El número es par
    else:
        print ("The number is odd") #El número es impar

def is_even(n):
    return n % 2 == 0

main()
#Codificacion mas comprimida posible


#En cuanto a la verificacion del numero par o impar, una codificacion mas detallada/larga seria:

#def main(): #Funcion principal para poder llamar valores de retorno de la verificacion

    #x = int(input("Enter a number: ")) #Ingreso del numero
    #if is_even(x)==True: #Verificación con la funcion "is_even" que el numero sea par o impar (Verdadero o falso)
        #print("The number is even") #El número es par
    #else:
        #print ("The number is odd") #El número es impar

#def is_even(n): #Verificacion del residuo("%") del número dividido por 2 y definición de la función "is_even"
    #if n % 2 == 0:
        #return True
    #else:
        #False

#main()

#Otra manera de hacerlo con 1 línea de código pero con la misma lógica:
#def is_even(n): #Verificacion del residuo("%") del número dividido por 2 y definición de la función "is_even"
#return True if n % 2 == 0 else False

#Simplificando la pregunta (Verdadero o falso) lo máximo posible:
#def is_even(n): #Verificacion del residuo("%") del número dividido por 2 y definición de la función "is_even"
#return n % 2 == 0 #Si es verdadero el valor de retorno (Return value) sera "True", mientras que si el falso ("False), en la funcion main() se vera reflejado dicho valor Booleano.