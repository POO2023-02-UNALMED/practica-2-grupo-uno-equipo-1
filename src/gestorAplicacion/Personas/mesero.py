from datetime import datetime
from gestorAplicacion.Personas.empleado import *

class Mesero (Empleado):

    #Constructor de la clase Mesero que hereda de Empleado

    def __init__(self, nombre="", cedula=000000, puesto=None, restaurante=None, turno=None):
        super().__init__(nombre, cedula, puesto, restaurante, turno)
        self.turnos = []
        self.turnos.append(turno)
        self.setFechaContratacion(datetime.now().day)

    #Sobreescritura de metodos

    def puntuacion(self):
        return "La puntacion del Mesero es: "+ self.getPuntuacion()

    def trabajo(self):
        return "Mesero, es quien se encarga de atender y servir a la clientela."
    
    def __str__(self):
        return f"Mesero: {self.getNombre()}"