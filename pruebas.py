#-*- coding: utf-8 -*-


from productos import ProductoFisico



class Checkout:

    def obtenerTotal(self, listaProductos):
        total = 0
        for producto in listaProductos:
            total += producto.precio
        print "El total es " + str(total)



    def imprimirLista(self, listaProductos):
        productosEnLista = [""]
        for producto in listaProductos:
            productosEnLista += producto.nombre
        print producto.nombre + " : " + str(producto.precio)

checkout = Checkout()
listaProductos = [
    ProductoFisico("tele", "2131241", 100 ),
    ProductoFisico("radio", "443121", 200 ),
    ProductoFisico("computadora", "0987541", 300 )
]

(checkout.imprimirLista(listaProductos))
print(checkout.obtenerTotal(listaProductos))
