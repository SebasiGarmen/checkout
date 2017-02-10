# -*- coding: utf-8 -*-


class Persona:
    nombre = ""
    apellido = ""
    edad = 0
    nacionalidad = ""
    sexo = ""

    def __init__(self, nombre="NA", apellido="NA", edad="NA", nacionalidad="mexicano", sexo=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo



class Empleado(Persona):
    salario= 0
    antiguedad= 0
    area= 0.0


class Directivo(Empleado):             #aqui en lugar de persona pudiera ser (empleado) para aprovechar lo que se puso atras
     numeroDeEstacionamiento= 0
     numeroDeOficina= 0
     semanasDeVacaciones= 0
     diasEnCasaClub= 0


empleado1 = Empleado("Jorge", "Lopez", 38, "Mexicano", "M" )
print(empleado1.nombre)
print(empleado1.apellido)
print(empleado1.edad)
print(empleado1.nacionalidad)
print(empleado1.sexo)
print(empleado1.diasDeVacaciones)
print(empleado1.salarioSemanal)
print(empleado1.numeroDeCubiculo)
