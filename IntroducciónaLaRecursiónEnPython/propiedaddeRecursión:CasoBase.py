#!/usr/bin/python3

from typing import Tuple, Union

def suma_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
    index = len(tupla)
    if index == 0:
        return 0
    return tupla[index-1] +  suma_tupla(tupla[:-1])

tupla = 1,2,4
sumtu = suma_tupla(tupla)
