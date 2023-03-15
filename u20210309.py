# Tarea clase abstracta
# Asignatura: Programación orientada a objetos I.
# Estudiante: Jordi Haziel Amaya Martínez.

#1.Debe de realizar un ejercicio en el cual cree una clase padre (Super clase) que sea abstracta aplicando el
#  término clase abstracta.
#2.Crear 3 clases hijas que deben de estar heredadas de la Super clase y aplique al ejercicio el polimorfismo.
#3.Debe tomar en cuenta que debe de realizar todo en un solo archivo con el nombre de su código estudiantil.py.
#4.La super Clase debe de ser aplicada a su persona, sus atributos y métodos.
#5.Recuerde que debe de utilizar polimorfismo para sus comportamientos.
#6.La entrega debe de realizarse con el enlace de un repositorio en GitHub.

from abc import ABC, abstractmethod
class Jordi(ABC):
    def __init__(self, nombreEstudiante, carreraEstudiante, universidadEstudiante):
        self.nombreEstudiante=nombreEstudiante
        self.carreraEstudiante=carreraEstudiante
        self.universidadEstudiante=universidadEstudiante
    @abstractmethod
    def verDatos(self):
        pass

class Nombre(Jordi):
    def verDatos(self):
        return "El nombre del estudiante es {}.".format(self.nombreEstudiante)
nombre1=Nombre("Jordi Amaya", "lic. en computación", "UNIVO")
print(nombre1.verDatos())

class Carrera(Jordi):
    def verDatos(self):
        return "La carrera del estudiante es {}.".format(self.carreraEstudiante)
carrera1=Carrera("Jordi Amaya", "lic. en computación", "UNIVO")
print(carrera1.verDatos())

class Universidad(Jordi):
    def verDatos(self):
        return "La universidad a la que asiste el estudiante es {}.".format(self.universidadEstudiante)
universidad1=Universidad("Jordi Amaya", "lic. en computación", "UNIVO")
print(universidad1.verDatos())