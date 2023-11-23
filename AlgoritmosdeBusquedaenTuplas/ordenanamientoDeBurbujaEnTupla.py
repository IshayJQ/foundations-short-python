#!/usr/bin/python3

rom typing import Tuple, Union

def ordenamiento_burbuja(tupla: Tuple[Union[str, int]]) -> Tuple[Union[str, int]]:
    n = len(tupla)
    tupla_ordenada = tuple(tupla)

    for i in range(n):
        for j in range(0, n-i-1):
            if tupla_ordenada[j] > tupla_ordenada[j+1]:
                print('Primera',tupla_ordenada[:j])
                tupla_ordenada = tupla_ordenada[:j] + (tupla_ordenada[j+1], tupla_ordenada[j]) + tupla_ordenada[j+2:]

    return tupla_ordenada


datos: Tuple[int] = (5, 1, 8, 3, 2)
datos_ordenados: Tuple[int] = ordenamiento_burbuja(datos)

print(f"Tupla ordenada: {datos_ordenados}")
# Salida esperada: "Tupla ordenada: (1, 2, 3, 5, 8)"

"""
def ordenamiento_burbuja(tupla: Tuple[Union[str, int]]) -> Tuple[Union[str, int]]:
    length = len(tupla)
    mayor = tupla[0]
    sortTuple = tupla
    for index1 in range(length):
        for index2 in range(index1,length):
            if sortTuple[index2] < tupla[index2+1]:
"""
