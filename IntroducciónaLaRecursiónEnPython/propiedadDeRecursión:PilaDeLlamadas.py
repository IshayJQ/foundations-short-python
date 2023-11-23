#!/usr/bin/python3

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)

# Caso de prueba 3: Factorial de 5
numero: int = 5
resultado: int = factorial(numero)
print(f"Factorial de {numero} es {resultado}")
# Salida esperada: "Factorial de 5 es 120"
