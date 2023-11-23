#!/usr/bin/python3
from typing import Tuple, Union

def multi_tupla(tupla: Tuple[Union[int, float]]) -> Union[int, float]:
    if len(tupla) == 0:
        return 1
    return tupla[0] * multi_tupla(tupla[1:])

tupla =(1,2,3)
multu = multi_tupla(tupla)
print(multu)
