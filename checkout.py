# -*- coding: utf-8 -*-

# __init__.py   (--> para importar algo de otro archivo, en tu carpeta debes tener un archivo llamado __init__.py para que jale)

from productos import ProductoFisico



class Checkout:

    def obtenerTotal(self, listaProductos):
        total = 0
        for producto in listaProductos:
            total += producto.precio
        return "Total = " + str(total)    #return termina el bucle

    def imprimirLista(self, listaProductos):
        for producto in listaProductos:
            print producto.nombre + " = " + str(producto.precio)



checkout = Checkout()
listaProductos = [
    ProductoFisico("tele", "2131241", 100 ),
    ProductoFisico("radio", "443121", 200 ),
    ProductoFisico("computadora", "0987541", 300 ),
    ProductoFisico("impresora", "0972348", 250 )
]

(checkout.imprimirLista(listaProductos))
print("_________________")
print(checkout.obtenerTotal(listaProductos))
