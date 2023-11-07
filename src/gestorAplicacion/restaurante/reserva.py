from datetime import datetime
from gestorAplicacion.personas.cliente import Cliente

class Reserva:
    def __init__(self, duenoReserva, numAsistentes, diaReserva):
        self.duenoReserva = duenoReserva
        self.mesa = None
        self.numAsistentes = numAsistentes
        self.diaReserva = diaReserva

    # Metodos getters
    def getDuenoReserva(self):
        return self.duenoReserva
    
    def getMesa(self):
        return self.mesa
    
    def getDiaReserva(self):
        return self.diaReserva
    
    def getNumeroAsistentes(self):
        return self.numAsistentes

    def setDuenoReserva(self, duenoReserva):
        self.duenoReserva = duenoReserva
    
    def setMesa(self, mesa):
        self.mesa = mesa
    
    def setDiaReserva(self, diaReserva):
        self.diaReserva = diaReserva

    def resumenReserva(self):
        formatoPersonalizado = "%d-%m-%Y"
        if self.mesa is None:
            return f"Dueño de la reserva: {self.duenoReserva.getNombre()}\nCédula del reservista: {self.duenoReserva.getCedula()}\nNúmero de asistentes: {self.numAsistentes}\nMesa número: Sin mesa asignada\nFecha reservada: {self.diaReserva.strftime(formatoPersonalizado)}"
        else:
            return f"Dueño de la reserva: {self.duenoReserva.getNombre()}\nCédula del reservista: {self.duenoReserva.getCedula()}\nNúmero de asistentes: {self.numAsistentes}\nMesa número: {self.mesa.getNumeroMesa()}\nFecha reservada: {self.diaReserva.strftime(formatoPersonalizado)}"
    
    def resumenReservaPedido(self):
        return f"Dueño de la reserva: {self.duenoReserva.getNombre()} Mesa número: {self.mesa.getNumeroMesa()}"
    
    @staticmethod
    def deStringAFecha(fechaString):
        formato = "%d-%m-%Y"
        fecha = datetime.strptime(fechaString, formato).date()
        return fecha
    
    @classmethod
    def revisarFecha(cls, fecha):
        f1 = cls.deStringAFecha(fecha)
        fechaActual = datetime.now().date()
        return f1 > fechaActual
