from datetime import datetime
from Personas.empleado import Empleado
from gestorAplicacion.Cosas.restaurante import Restaurante
from gestorAplicacion.Cosas.turno import Turno

class Mesero (Empleado):
  
    def __init__(self, nombre="", cedula=000000, puesto=None, restaurante=None, turno=None):
        super().__init__(nombre, cedula, puesto, restaurante, turno)
        self.turnos = []
        self.turnos.append(turno)
        self.setFechaContratacion(datetime.date.today().day())

    def puntuacion(self):
        return "La puntacion del Mesero es: "+ self.getPuntuacion()

    def trabajo(self):
        return "Mesero, es quien se encarga de atender y servir a la clientela."