#!/usr/bin/python3

from typing import Tuple, Union

def multi_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
		index = len(tupla)-1
    if index == 0:
        return tupla[0]
    return tupla[index] * multi_tupla(tupla[:-1])

tupla = 1,2,4,67,1,2,4
sumtu = suma_tupla(tupla)
