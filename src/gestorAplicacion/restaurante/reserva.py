from datetime import datetime
from src.gestorAplicacion.Personas.cliente import Cliente

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
        if self.mesa is None:
            return f"Dueño de la reserva: {self.duenoReserva.getNombre()}\nCédula del reservista: {self.duenoReserva.getCedula()}\nNúmero de asistentes: {self.numAsistentes}\nMesa número: Sin mesa asignada\nFecha reservada: {self.diaReserva.strftime('%d-%m-%Y')}"
        else:
            return f"Dueño de la reserva: {self.duenoReserva.getNombre()}\nCédula del reservista: {self.duenoReserva.getCedula()}\nNúmero de asistentes: {self.numAsistentes}\nMesa número: {self.mesa.getNumeroMesa()}\nFecha reservada: {self.diaReserva.strftime('%d-%m-%Y')}"

    def resumenReservaPedido(self):
        return f"Dueño de la reserva: {self.duenoReserva.getNombre()} Mesa número: {self.mesa.getNumeroMesa()}"

    @staticmethod
    def deStringAFecha(fechaString):
        formato = "%d-%m-%Y"
        fecha = datetime.strptime(fechaString, formato).date()
        return fecha

    @staticmethod
    def revisarFecha(fecha):
        f1 = Reserva.deStringAFecha(fecha)
        fechaActual = datetime.now().date()
        return f1 > fechaActual
