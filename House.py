name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
#El codigo en su estado inicial con la solucion lo mas simple y burda posible

name = input("What's your name? ")

if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
#El codigo un poco mas simplificado PERO con el condicional "if"

name = input("What's your name? ")
match name:
    case "Harry" | "Hermoine" | "Ron": #El caracter "|" es para separar los valores en la funcion match/case
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: #El guion "_" en case significa "cualquier caracter que se introduzca"para casos no especificados
        print("Who?")