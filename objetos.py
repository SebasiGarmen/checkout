# -*- coding: utf-8 -*-


#programación en objetos


class Animal:                #se acostumbra a empezar la clase con mayuscula
    nPatas = 4
    color = "negro"
    sonido = ""
    def hacerSonido(self):  #el argumento de una funcion dentro de la clase siempre será self por lo menos uno, se pueden agregar mas.
        print(self.sonido)

    def correr(self):
        print("run run run")

perro = Animal()    #instansear un objeto a la clase
gato = Animal()
print(perro.nPatas)
perro.sonido= "guau guau"
perro.hacerSonido()
