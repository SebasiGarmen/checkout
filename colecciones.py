# -*- coding: utf-8 -*-

batch_13 = ["Alejandro", "Frank", "Sebastian", "Nelly", "Cynthia"]

batch_14 = ["Pedro", "Juan", "Bruno", "Veronica"]

elementos = ["Aire", "Tierra", "Fuego", "Agua"]

#las listas son objetos iterables

for alumno in batch_13:
    print(alumno)

for alumno in batch_14:
    print(alumno)

#range [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, 10):
    print(i)

#range [1, 3, 5, 7, 9]
for e in range(1, 10, 2):
    print(e)

#range [1, 2, 3, 4... 19]
for w in range(0, 20):
    print(w)


for elemento in elementos:
    print(elemento)

persona = {
    "nombre": "Sebastian",
    "apellido": "Garcia",
    "edad": 20,
}

print("Diccionario =====")
for dato, valor in persona.iteritems():
    print(dato + "es" + str(valor))

#*for* elemento_individual *in* interable:
#   *le hago algo*
