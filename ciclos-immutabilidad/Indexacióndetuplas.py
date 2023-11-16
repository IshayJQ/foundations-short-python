#!/usr/bin/python3

mi_tupla = (1, 2, 3, 'a', 'b','c','d','e')
primer_elemento = mi_tupla[0]  # Acceder al primer elemento
ultimo_elemento = mi_tupla[-1]  # Acceder al último elemento

for i in range(len(mi_tupla)):
    if i == 0:
      print(mi_tupla[i])
    else:
      print(mi_tupla[i*-1], end="")
      #print(end="")
      print(mi_tupla[i], end="")
      #print(end="")
