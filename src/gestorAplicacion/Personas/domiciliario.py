from datetime import datetime
from Personas.empleado import Empleado
from Restaurante.turno import Turno
from Restaurante.restaurante import Restaurante

class Domiciliario(Empleado):

    #Constructor de la clase Domiciliario que hereda de Empleado

    def __init__(self,nombre="",cedula=000000,puesto=None,restaurante=None,turno=None):
        super().__init__(nombre,cedula,puesto,restaurante,turno)
        self.tunros=[]
        self.turnos.append(turno)
        self.setFechaContratacion(datetime.date.today().day())

    #Sobreescritura de metodos
    def puntuacion(self):
        return "La puntuación del Domiciliario es: "+ self.getPuntuacion()

    def trabajo(self):
        return "Domiciliario, es la persona encargada de entregar los pedidos a domicilio."