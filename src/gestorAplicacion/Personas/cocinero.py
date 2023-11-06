from datetime import datetime
from gestorAplicacion.Cosas.restaurante import Restaurante
from gestorAplicacion.Cosas.turno import Turno

class Cocinero (Empleado):

    def __init__(self, nombre="", cedula=000000, puesto=None, restaurante=None, turno=None):
        super.__init__(nombre, cedula, puesto, restaurante, turno)
        self.turnos = []
        self.turnos.append(turno); 
        self.setFechaContratacion(datetime.date.today().day())

    def puntuacion(self):
        return "La puntacion del Cocinero es: "+ self.getPuntuacion()

    def trabajo(self):
        return "Cocinero, es quien cocina y prepara alimentos en el restaurante."