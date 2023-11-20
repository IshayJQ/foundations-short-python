#!/usr/bin/python3

def recorrerTupla(tupla):
    length = len(tupla)
    for elemento in tupla:
        print(elemento, end="")
    print()
    for index in range(length):
        print(tupla[index], end="")
    print()
    i = length-1
    while i >= 0:
        print(tupla[i], end="")
        i -= 1
    print()



mi_tupla = (1, 2, 3)

recorrerTupla(mi_tupla)
