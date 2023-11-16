from Personas.persona import Persona
from Restaurante.reserva import Reserva
from Restaurante.pedido import Pedido


class Cliente(Persona):

    #Constructor de la clase Cliente que hereda de Persona

    def __init__(self,nombre="",cedula=000000):
        super().__init__(nombre,cedula)
        self.reserva=None
        self.pedido=None

    #Getter
    def getReserva(self):
        return self.reserva

    def getPedido(self):
        return self.pedido

    #Setter

    def setReserva(self,reserva):
        self.reserva=reserva

    def pedirComida(self,pedido):
        self.pedido=pedido

    #Metodo abstracto definido
    def puntuacion(self):
        return "El cliente "+self.getNombre()+" no tiene puntuación"