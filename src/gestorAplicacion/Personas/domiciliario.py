from datetime import datetime
from personas.empleado import Empleado
from restaurante.turno import Turno
from restaurante.restaurante import Restaurante

class Domiciliario(Empleado):
    def __init__(self,nombre="",cedula=000000,puesto=None,restaurante=None,turno=None):
        super().__init__(nombre,cedula,puesto,restaurante,turno)
        self.tunros=[]
        self.turnos.append(turno)
        self.setFechaContratacion(datetime.date.today().day())
    def puntuacion(self):
        return "La puntuación del Domiciliario es: "+ self.getPuntuacion()
    def trabajo(self):
        return "Domiciliario, es la persona encargada de entregar los pedidos a domicilio."