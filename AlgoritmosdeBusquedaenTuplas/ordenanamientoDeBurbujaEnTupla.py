from typing import Tuple, Union

def ordenamiento_burbuja(tupla: Tuple[Union[str, int]]) -> Tuple[Union[str, int]]:
    print('tupla:',tupla)
    n = len(tupla)
    tupla_ordenada = tuple(tupla)

    for i in range(n):
        print(f'1er FOR iteracion i:{i}')
        for j in range(0, n-1-i):
            print(f"2do FOR iteracion{j} -> (j:{j},{n-i-1})")
            if tupla_ordenada[j] > tupla_ordenada[j+1]:
                print('j:',j)
                print('Primera',tupla_ordenada[:j])
                print('Segunda',tupla_ordenada[j+1], tupla_ordenada[j])
                print('Tercera',tupla_ordenada[j+2:])
                tupla_ordenada = tupla_ordenada[:j] + (tupla_ordenada[j+1], tupla_ordenada[j]) + tupla_ordenada[j+2:]
                print('tupla Ordenada', tupla_ordenada)
                
    return tupla_ordenada


datos: Tuple[int] = (1, 5, 8, 3, 2)
datos_ordenados: Tuple[int] = ordenamiento_burbuja(datos)

print(f"Tupla ordenada: {datos_ordenados}")
