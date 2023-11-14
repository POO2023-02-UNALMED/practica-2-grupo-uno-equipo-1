from datetime import datetime
from enum import Enum

class Tipo(Enum):
    TOMATES,CEBOLLAS,PAPAS,ACEITES,VINOS = "TOMATES", "CEBOLLAS", "PAPAS", "ACEITES", "VINOS"
    QUESOS,CHAMPINONES,RES,PESCADOS,CERDOS = "QUESOS", "CHAMPINONES", "RES", "PESCADOS", "CERDOS"
    POLLOS,PANES,AJOS,ESPECIAS,HUEVOS = "POLLOS", "PANES", "AJOS", "ESPECIAS", "HUEVOS"
    ATUN,CUCHARAS,TENEDORES,PLATOS,VASOS = "ATUN", "CUCHARAS", "TENEDORES", "PLATOS", "VASOS"

class Material:
    def __init__(self, tipo, cantidad=0, precioUnitario=0, fechavencimiento=None):
        if tipo in Tipo:
            self.tipo = tipo
        else:
            self.tipo = None
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        self.fechavencimiento = fechavencimiento

    # Métodos getters
    def getTipo(self):
        return self.tipo

    def getCantidad(self):
        return self.cantidad

    def getPrecioUnitario(self):
        return self.precioUnitario

    def getFechaVencimiento(self):
        return self.fechavencimiento

    # Métodos setters
    def setTipo(self, tipo):
        self.tipo = tipo

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def setPrecioUnitario(self, precioUnitario):
        self.precioUnitario = precioUnitario

    def setFechaVencimiento(self, fechavencimiento):
        self.fechavencimiento = fechavencimiento

    # Métodos de funcionalidad
    def actualizarPrecio(self, precioUnitario):
        self.setPrecioUnitario(precioUnitario)

    def actualizarCantidad(self, cantidad):
        self.setCantidad(cantidad)

    def actualizarFechaVencimiento(self, fechavencimiento):
        self.setFechaVencimiento(fechavencimiento)

    # Metodos para modificar cantidades
    def comprarMaterial(self, cantidad):
        self.cantidad += cantidad

    def botarMaterial(self, cantidad):
        self.cantidad -= cantidad

    def cambiarPrecioUnitario(self, precio):
        self.precioUnitario = precio

    def fechaMaterial(self, fecha):
        self.fechavencimiento = fecha

    def restarCantidad(self, cantidad):
        self.cantidad -= cantidad

    def fecha_material(self):
        if self.fechavencimiento is None:
            return "Este material no tiene fecha de vencimiento"
        else:
            return self.fechavencimiento.strftime("%d-%m-%Y")
