# -*- coding: utf-8 -*-

class MetodoDePago:
    def cobrar(self, cantidad):
        pass

class Stripe(MetodoDePago):
    """
        Esta clase es la encargada de cobrar con Stripe.
        implementa la Interfaz de Metodo de pago
    """
    token = "asdfgh"
    mail = "sebasti.garmen@gmail.com"

    @classmethod
    def cobrar(cls, cantidad):     #<-- cuando tengas un @classmethod, en el def en lugar de poner SELF se pone CLS.
        """
            Esta es la función que cobra
        """
        print("Cobré con Stripe %s" % cantidad)

    @staticmethod
    def unMetodoStatico():
        pass

class Efectivo(MetodoDePago):
    def cobrar(self, cantidad):
        print("Envié correo al cliente para que prepare el dinero")

class Bitcoin(MetodoDePago):
    def cobrar(self, cantidad):
        print("Cobré %s bitcoins" % cantidad)
