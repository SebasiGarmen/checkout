# -*- coding: utf-8 -*-

#listaValores = [10, 100, 90.9, 100]
#sumaTotal / numeroEstudiantes


#promedio
def promedio(listaValores):
    promedio = sum(listaValores) / len(listaValores)
    return promedio


#moda -->
def moda(listaValores):
    valores = {}
    for valor in listaValores:
        if valores.get(valor):        #aqui se pregunta al diccionario
            valores[valor] += 1       #se agrega uno si ya existe o se crea si no existe
        else:
            valores[valor] = 1

    print(valores)

    vMax = 0
    moda = 0
    for valor, repeticiones in valores.iteritems():
        if repeticiones > vMax:
            vMax = repeticiones
            moda = valor

    return moda

#mediana
def mediana(listaValores):

    orden = sorted(listaValores)
    medio = len(listaValores)/2

    if len(listaValores) % 2 == 0:
        return (orden[medio-1] + orden[medio]) / 2.0
    else:
        return orden[medio]



listaValores = [0, 2, 3, 1, 4, 5, 6 ,7, 8, 9, 10]
print(mediana(listaValores))
