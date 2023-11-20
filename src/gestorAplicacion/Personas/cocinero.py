from datetime import datetime
from gestorAplicacion.Personas.empleado import Empleado, datetime, Material, Turno, Restaurante, Pedido

class Cocinero(Empleado):

    #Constructor de la clase Cocinero que hereda de Empleado
    def __init__(self,nombre="",cedula=000000,puesto=None,restaurante=None,turno=None):
        super().__init__(nombre,cedula,puesto,restaurante,turno)
        self.turnos=[]
        self.turnos.append(turno)
        self.setFechaContratacion(datetime.now().day)

    #Sobreescritura de metodos

    def Puntuacion(self):
        return "La puntuación del Cocinero es: "+self.getPuntuacion()

    def trabajo(self):
        return "Cocinero, es quien cocina y prepara alimentos en el restaurante."
    
    def __str__(self):
        return f"Cocinero: {self.getNombre()}"