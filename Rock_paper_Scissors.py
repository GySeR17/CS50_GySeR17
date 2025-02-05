print("Bienvenido a piedra papel o tijera, por favor indica el nombre de los jugadores")
print("Cual es el nombre del 1er jugador?")
nom_jug_1 = input("")
print("Cual es el nombre del 2do jugador?")
nom_jug_2 = input("")

print("Que elije el jugador 1, piedra, papel o tijera?")
mov_jug_1 = input("").lower()
print("Que elije el jugador 2, piedra, papel o tijera?")
mov_jug_2 = input("").lower()

mov_validos = ["piedra", "papel", "tijera"]

if mov_jug_1 in mov_validos and mov_jug_2 in mov_validos:
    if mov_jug_1 == mov_jug_2:
        print("Empate!")
    elif (mov_jug_1 == "piedra" and mov_jug_2 == "papel") or\
          (mov_jug_1 == "papel" and mov_jug_2 == "tijera") or\
          (mov_jug_1 == "tijera" and mov_jug_2 == "piedra"):
        print(f"Gana {nom_jug_2}!")
    else:
        print(f"Gana {nom_jug_1}!")
else:
    print("ingrese una palabra valida entre: piedra, papel o tijera")

"""
Cuando queremos establecer un condicional que realice una acción sencilla, podemos usar el "operador ternario" que consiste 
en compactar un if-else en una sola línea. Su sintaxis es:


condition_if_true if condition else condition_if_false
Por ejemplo


edad = 21
print("mayor de edad") if edad > 18 else print("menor de edad") 
"""