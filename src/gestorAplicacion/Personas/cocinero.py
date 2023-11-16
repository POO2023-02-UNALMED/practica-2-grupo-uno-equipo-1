from datetime import datetime
from Personas.empleado import Empleado
from Restaurante.turno import Turno
from Restaurante.restaurante import Restaurante


class Cocinero(Empleado):

    #Constructor de la clase Cocinero que hereda de Empleado

    def __init__(self,nombre="",cedula=000000,puesto=None,restaurante=None,turno=None):
        super().__init__(nombre,cedula,puesto,restaurante,turno)
        self.turnos=[]
        self.turnos.append(turno)
        self.setFechaContratacion(datetime.date.today().day())

    #Sobreescritura de metodos

    def puntuacion(self):
        return "La puntuación del Cocinero es: "+self.getPuntuacion()

    def trabajo(self):
        return "Cocinero, es quien cocina y prepara alimentos en el restaurante."