# -*- coding: utf-8 -*-

#FUNCIONES SIN PARAMETROS
def saludar():
    print "Hola"
saludar() #sin parametro dentro


#FUNCIONES CON PARAMETROS
def saludarA(nombre):
    print "Hola " + nombre #concatenación
saludarA("Ian") #con parametro dentro


#FUNCIONES CON VALOR DE RETORNO
def componerNombre(nombre, apellido):
    return nombre.capitalize() + " " + apellido.capitalize()    #return no va a mostrar nada, sólo hace el calculo
nombreCompleto = componerNombre("iAn", "lOpEz")
print(nombreCompleto)


#DETECCION DE PALINDROMO
def es_palindromo(palabra):
    #True si la palabra es una PALINDROMO
    #False si la palabra no es un palíndromo

 #-------------------------------------------#
    # palabra = palabra.replace(" ", "")
    # palabra = palabra.replace("á", "a")
    # palabra = palabra.replace("é", "e")
    # palabra = palabra.replace("í", "i")
    # palabra = palabra.replace("ó", "o")
    # palabra = palabra.replace("ú", "u")
    palabra = palabra.lower()

#REMPLAZO A LOS REMPLAZOS DE ESPACIOS Y ACENTOS

    reemplazos = {
        " ": "",
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
    }
    for viejo, nuevo in reemplazos.iteritems():
        palabra = palabra.replace(viejo, nuevo)
    return palabra == palabra[::-1]


print "PALINDROMO"
print(es_palindromo("Aníta láVa la tiNa"))
#quitar espacios
