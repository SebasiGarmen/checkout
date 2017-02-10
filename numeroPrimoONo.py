# -*- coding: utf-8 -*-

def esPrimo(n):
    #saber si es divisible entre algun numero que no sea 1 o si mismo
    listaNumerosMenores = range(2, n) #n = 5   -->  2, 3, 4
    for numero in listaNumerosMenores:
        if n % numero == 0:
            return False
        return True

print(esPrimo(10))
print(esPrimo(11))
print(esPrimo(37))
