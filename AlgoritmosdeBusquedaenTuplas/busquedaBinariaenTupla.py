#!/usr/bin/python3

from typing import Tuple, Union

def busqueda_binaria(tupla: Tuple[Union[int, str]], objetivo: Union[int, str]) -> int:
    final = len(tupla)
    mitad = final/2
    mitad = int(mitad)
    while mitad <=final -1:
        if objetivo <= tupla[mitad]:
            if objetivo == tupla[mitad]:
                return mitad
            mitad = mitad/2
            mitad = int(mitad)
        else:
            temp = (final-mitad)/2
            temp = int(temp)
            mitad = mitad+temp
    return -1



# Ejemplo de uso
datos: Tuple[int] = (1, 2, 3, 5, 8)
indice: int = busqueda_binaria(datos, 2)
print(f"El valor 5 se encontró en el índice {indice}.")
