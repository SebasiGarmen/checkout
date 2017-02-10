# -*- coding: utf-8 -*-

    #funciones --> def
def imprimirGrupo(grupo):
        for alumno in grupo:
            for dato, valor in alumno.iteritems():
                print(" su " + dato + " es " + str(valor))


batch13 = [
    {"nombre": "Antonio", "edad": 41},
    {"nombre": "Ximena", "edad": 24}
]

imprimirGrupo(batch13)


#iteriterms --> convierte diccionarios en listas en tuplas.

#{"nombre": "Antonio", "Edad": 20}
#[("nombre", "Antonio", "Edad", 20)]
