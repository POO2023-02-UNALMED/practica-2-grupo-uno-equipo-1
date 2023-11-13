import random
from datetime import date

class Mesa:
    numeroMesas = []

    def __init__(self, capacidad, numeroMesa):
        self.capacidad = capacidad
        if Mesa.verificarNumero(numeroMesa):
            self.numeroMesa = Mesa.generarNumeroMesa()
        else:
            self.numeroMesa = numeroMesa
        self.ocupada = False
        self.reservas = []
        Mesa.numeroMesas.append(self.numeroMesa)

    # Metodos getters
    def getCapacidad(self):
        return self.capacidad

    def getReservas(self):
        return self.reservas

    def isOcupada(self):
        return self.ocupada

    def getNumeroMesa(self):
        return self.numeroMesa

    # Metodos setters
    def setCapacidad(self, nuevaCapacidad):
        self.capacidad = nuevaCapacidad

    def setReservas(self, reservas):
        self.reservas = reservas

    def setOcupada(self, ocupacion):
        self.ocupada = ocupacion

    def setNumeroMesa(self, numeroMesa):
        if not Mesa.verificarNumero(numeroMesa):
            self.numeroMesa = numeroMesa

    # Metoddos estaticos
    @staticmethod
    def generarNumeroMesa():
        while True:
            numeroAleatorio = random.randint(1, 1000)
            if not Mesa.verificarNumero(numeroAleatorio):
                return numeroAleatorio

    @staticmethod
    def verificarNumero(numero):
        return numero in Mesa.numeroMesas

    # Metodos de clase
    @classmethod
    def getNumeroMesas(cls):
        return cls.numeroMesas

    # Metodos para funcionalidad
    def anadirNumero(self, a):
        self.getNumeroMesas().append(a)

    def suficienteCapacidad(self, reserva):
        if self.capacidad >= reserva.getNumeroAsistentes():
            return True
        else:
            return False

    def reservarMesa(self, reserva):
        self.reservas.append(reserva)
        reserva.setMesa(self)

    def mesaCompatible(self, reserva):
        for reserva1 in self.reservas:
            if reserva1.getDiaReserva() == reserva.getDiaReserva():
                return False
        return True

    def borrarReservasViejas(self):
        fechaActual = date.today()
        self.reservas = [reserva for reserva in self.reservas if not reserva.getDiaReserva() < fechaActual]

    def resumenMesa(self):
        return f"Capacidad de la mesa: {self.capacidad}\nNúmero de la mesa: {self.numeroMesa}"

    #ToString de la clase
    def __str__(self):
        return f"mesa numero: {self.numeroMesa} con capacidad: {self.capacidad}"
