#!/usr/bin/python3

def euclides(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (MCD) de dos números enteros a y b utilizando el algoritmo de Euclides.

    Args:
        a (int): El primer número entero.
        b (int): El segundo número entero.

    Returns:
        int: El MCD de a y b.
    """
    pass
    if a%b == 0:
      return a
    return euclides(b, a%b)


# Caso de prueba 1: MCD de 48 y 18
num1: int = 48
num2: int = 18
mcd: int = euclides(num1, num2)
print(f"MCD de {num1} y {num2} es {mcd}")
# Salida esperada: "MCD de 48 y 18 es 6"
