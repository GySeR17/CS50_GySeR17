to_do = ["Ir al hotel",
         "Ir a almorzar",
         "Visitar el museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(numbers)
mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix),type(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Tercero elemento", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Tercero elemento", string[-1])
print(mix[2:])
print(mix)
mix.append(False)
print(mix)
mix.insert(2, ["a", "b"])
mix.append("c")
print(mix)