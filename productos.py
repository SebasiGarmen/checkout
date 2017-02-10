# -*- coding: utf-8 -*-

class Producto:           #esta es la clase de un producto en general
    precio = 0.0
    calidad = "buena"
    origen = ""
    sku = ""                #sku : codgo de barras.
    nombre = ""
    imagen = ""

    def __init__(self, nombre, sku, precio):   #esto es el constructor de la clase (siempre que veas __ es algo especial)
        self.nombre = nombre
        self.sku = sku
        self.precio = precio

    def establecerImagen(self, imagen):
        #ir por la imagen a internet
        #guardarla con un nombre relacionado al producto     <-- esto debería ser código
        self.imagen = imagen


class ProductoFisico(Producto):        #en un producto fisico puedes agregar caracteristicas exclusivas de los productos fisicos y aparte agregar la clase de los productos en general
    fechaDeCaducidad = ""

    def estaCaducado(self):
        return True



class ProductoVirtual(Producto):        #igualmente aquí como en el anterior
    tamanoMB = 0.0


# tele = ProductoFisico("TV Sony", "1908489909", 100.90)
# print(tele.nombre)
# print(tele.sku)
# print(tele.precio)
# print(tele.fechaDeCaducidad)
# # radio = ProductoFisico()
# # print(tele.calidad)
#
# cancion = ProductoVirtual("Stay", "1908489", 14.99)
# print(cancion.nombre)
# print(cancion.sku)
# print(cancion.precio)
