from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre="", cedula=000000):
        self.nombre = nombre
        self.cedula = cedula

    def getNombre(self):
        return self.nombre

    def getCedula(self):
        return self.cedula

    def setNombre(self, nombre):
        self.nombre = nombre

    def setCedula(self, cedula):
        self.cedula = cedula

    @abstractmethod
    def puntuacion(self):
        pass