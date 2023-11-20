from enum import Enum

class TipoTurno(Enum):
    SEMANA = "SEMANA"
    SABADO = "SABADO"
    DOMINGO = "DOMINGO"

class Turno:

    #Constructor de la clase Turno

    def __init__(self, tipo, horas, salario):
        self.tipo = tipo
        self.horas = horas
        self.salario = salario
        self.completado = False
        self.cobrado = False
    # Métodos getter

    def getTipo(self):
        return self.tipo

    def getHoras(self):
        return self.horas

    def getSalario(self):
        return self.salario

    def isCompletado(self):
        return self.completado

    def isCobrado(self):
        return self.cobrado

    def getEstado(self):
        return self.completado

    # Métodos setter

    def setSalario(self, salario):
        self.salario = salario

    def setCompletado(self, completado):
        self.completado = completado

    def setCobrado(self, cobrado):
        self.cobrado = cobrado

    def setHoras(self, horas):
        self.horas = horas

    # Metodo para actualizar tiempo

    def actualizarTiempo(self, turno, tiempo):
        if(self.horas*60)-tiempo>=20:
            self.horas = (self.horas*60-tiempo)/60
            if turno.getHoras*60-tiempo<=20:
                turno.setCompletado(True)

    # Metodo para calcualr las horas extra

    def HorasExtras(self):
        horasRegulares = 8
        if self.horas > horasRegulares:
            return self.horas - horasRegulares
        else:
            return 0

    # Tostring de la clase
    def toString(self):
        return (f"Tipo: {self.getTipo()} Salario: {self.getSalario()} Estado completado: {self.isCompletado()} Estado cobrado: {self.isCobrado()}")