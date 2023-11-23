#!/usr/bin/python3

from typing import Tuple, Union

def multi_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
    index = len(tupla)
    if index == 0:
        return 1
    return tupla[index-1] * multi_tupla(tupla[:-1])

tupla = 1,2,3
multupla = multi_tupla(tupla)
