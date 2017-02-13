#-*- coding: utf-8 -*-

lista = range(11)

def cubo(n):
    return n*n*n

print(map(cubo, lista))    #<--primero funcion sin llamar, o sea sin el () , luego la lista
