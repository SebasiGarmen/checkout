# -*- coding: utf-8 -*-


#Parametros Nombrados
def precioFinal(precio=0, tasaIVA=0.16):  #aqui el parametro se mete como variable y se
    return precio * (1 + tasaIVA)           #agrega un DEFAULT por si no recibe
                                            # información en el parametro

p = 10000    #aqui le das un valor al parametro precio
t = 0.16     #aqui  le das un valor al parametro IVA

print(precioFinal(precio=p, tasaIVA=t))    #parametro=variable de arriba


#Argumentos
def imprimirListaDeProdcutos(*args):     #args es una lista de todos los parametros que recibe
    for producto in args:
        print(producto)

imprimirListaDeProdcutos("sillas", "mesa", "sillon")


#Kwargs
listaImpuestos=[]

def aplicarImpuestos(precio, **kwargs):
    totalImpuestos = 0    #al principio porque aun no hay impuestos
    for impuesto, tasa in kwargs.iteritems():
        impuestoActual = precio * tasa
        totalImpuestos = totalImpuestos + impuestoActual
        print(impuesto + "es " + str(impuestoActual))
        print(totalImpuestos)
    return precio + totalImpuestos

aplicarImpuestos(1000, iva=0.16, ipsss=0.04, isr=0.18)
