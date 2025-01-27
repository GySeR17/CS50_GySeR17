#Tablero de damas hecho desde cero.
tablero_damas = [[0,"d",0,"d",0,"d",0,"d"],
                 ["d",0,"d",0,"d",0,"d",0],
                 [0,"d",0,"d",0,"d",0,"d"],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 ["d",0,"d",0,"d",0,"d",0],
                 [0,"d",0,"d",0,"d",0,"d"],
                 ["d",0,"d",0,"d",0,"d",0]]

for fila in tablero_damas:
    for dama in fila:
        print(dama, end= "")
    print()