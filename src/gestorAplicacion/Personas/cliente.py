from gestorAplicacion.Personas.persona import Persona

class Cliente(Persona):

    #Constructor de la clase Cliente que hereda de Persona

    def __init__(self,nombre="",cedula=000000):
        from gestorAplicacion.Restaurante.reserva import Reserva
        from gestorAplicacion.Restaurante.pedido import Pedido
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
    def Puntuacion(self):
        return "El cliente "+self.getNombre()+" no tiene puntuación"
    
    def __str__(self):
        return f"Cliente: {self.getNombre()}"