#!/usr/bin/python3

def suma_naturales(N: int) -> int:
	if N == 1:  # Caso base: Cuando N es 1, la suma es 1
        return 1
    else:
        return N + suma_naturales(N - 1)  # Llamada recursiva reduciendo N

# Ejemplo de uso
resultado: int = suma_naturales(5)
print(f"La suma de los primeros 5 números naturales es: {resultado}")
# Salida esperada: "La suma de los primeros 5 números naturales es: 15"
