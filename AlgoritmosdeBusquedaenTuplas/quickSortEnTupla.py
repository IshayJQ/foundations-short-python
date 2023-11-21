#!/usr/bin/python3

from typing import Tuple, Union

def quick_sort(tupla: Tuple[Union[int, str]]) -> Tuple[Union[int, str]]:


# Ejemplo de uso 1: Ordenamiento de una tupla de enteros
datos: Tuple[int] = (5, 1, 8, 3, 2)
datos_ordenados: Tuple[int] = quick_sort(datos)
print(f"Tupla ordenada: {datos_ordenados}")
# Salida esperada: "Tupla ordenada: (1, 2, 3, 5, 8)"
