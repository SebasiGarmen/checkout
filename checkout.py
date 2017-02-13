# -*- coding: utf-8 -*-

# __init__.py   (--> para importar algo de otro archivo, en tu carpeta debes tener un archivo llamado __init__.py para que jale)

from productos import ProductoFisico
from metodos import Stripe, Bitcoin



class Checkout:

    def __init__(self, metodoDePago):
        #pass --> para dejar una def en blanco
        self.metodoDePago = metodoDePago


    def obtenerTotal(self, listaProductos):
        total = 0
        for producto in listaProductos:
            total += producto.precio
        return "Total = " + str(total)    #return termina el bucle

    def imprimirLista(self, listaProductos):
        for producto in listaProductos:
            # print producto.nombre + " = " + str(producto.precio)
            print("Nombre: %s, SKU: %s, Precio: %s" % (producto.nombre, producto.sku, producto.precio))

    def cobrar(self, listaProductos):
        total = self.obtenerTotal(listaProductos)
        self.metodoDePago.cobrar(total)
        print("He cobrado %s" % total)


tele = ProductoFisico("tele", "2131241", 100 )
radio = ProductoFisico("radio", "443121", 200 )
computadora = ProductoFisico("computadora", "0987541", 300 )
listaProductos = [tele, radio, computadora]


checkoutStripe = Checkout(Stripe)
checkoutStripe.cobrar(listaProductos)

help(Stripe)
