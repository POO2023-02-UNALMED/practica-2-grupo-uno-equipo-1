from Personas.persona import Persona
from Restaurante.reserva import Reserva
from Restaurante.pedido import Pedido

class Cliente (Persona):

    def __init__(self, nombre="", cedula=000000):
        super().__init__(nombre, cedula)
        self.reserva = None
        self.pedido = None

    def getReserva(self):
        return self.reserva

    def setReserva(self, reserva):
        self.reserva = reserva

    def getPedido(self):
        return self.pedido

    def pedirComida(self, pedido):
        self.pedido = pedido

    def puntuacion(self):
        return "El cliente "+self.getNombre() +" no tiene puntuacion"