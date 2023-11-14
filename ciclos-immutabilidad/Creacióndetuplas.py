#!/usr/bin/python3

from typing import Tuple

tupla1:Tuple[int] = (1, 2, 3)
tupla2:Tuple[str] = 'a', 'b', 'c'
tupla_vacia:Tuple[str] = ()
tupla_vacia = ('m','pera','carro')
tupla_instancia:Tuple[float] = tuple()
tupla_instancia = 6.8, 9.12, 3.14
tupla_de_un_elemento:Tuple[str] = ('z',)  # Importante agregar una coma para crear una tupla de un elemento

number:int
newTuple:Tuple[int] = tuple(number for number in range(5))
print(newTuple)
