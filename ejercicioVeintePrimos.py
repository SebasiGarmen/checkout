# -*- coding: utf-8 -*-


def numerosPrimos(x, y):
    z = 0                                            # Z es el contador de números primas que van
    listaNumerosPrimos = []                          #lista de numeros primos esta en 5
    while z < x:                                     #Mientras que z sea menor que x (número deseado):
        for numero in range(2, y):                          #por cada numero en el rango de 2 a y()
            if y % numero == 0:
                y = y+1
                break

        else:
            print y
            listaNumerosPrimos.append(y)
            y = y+1
            z = z+1

    return listaNumerosPrimos

print(numerosPrimos(10, 2))
