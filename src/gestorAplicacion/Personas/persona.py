from abc import ABC, abstractmethod

class Persona(ABC):

    #Constructor de la clase Persona
    def __init__(self, nombre="", cedula=000000):
        self.nombre = nombre
        self.cedula = cedula

    #Getter
    def getNombre(self):
        return self.nombre

    def getCedula(self):
        return self.cedula

    #Setter
    def setNombre(self, nombre):
        self.nombre = nombre

    def setCedula(self, cedula):
        self.cedula = cedula

    @abstractmethod
    def puntuacion(self):
        pass