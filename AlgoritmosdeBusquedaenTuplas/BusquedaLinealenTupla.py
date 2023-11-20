#!/usr/bin/python3

from typing import Tuple, Union

def busqueda_lineal(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:

    for index in range(len(tupla)):
        if tupla[index] == objetivo:
            return index
    return -1


datos: Tuple[int] = (5, 1, 8, 3, 2)
indice: int = busqueda_lineal(datos, 3)
print(f"El valor 3 se encontró en el índice {indice}.")
