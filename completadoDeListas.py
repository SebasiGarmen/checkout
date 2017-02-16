# -*- coding: utf-8 -*-

#LIST COMPREHESION = AYUDA A ITERAR LISTAS

lista = range(11)       #<-- lista del 0 a 10
x = [n for n in lista if n % 2 == 0]     #<-- x es una variable que pide: por cada numero en la lista, si el
print(x)                                         #residuo del n es 0, agregalo a la variable


grupo = ["hector", "ivan", "patricio"]
y = [n.upper() for n in grupo]
print(y)
