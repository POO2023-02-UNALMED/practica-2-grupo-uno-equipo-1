from uiMain import Menu
from gestorAplicacion.personas.empleado import Empleado
class Pedido(Menu):
    tiempoDomicilio = 45
    tiempoMesero = 30

    def __init__(self, mesa=None, tipoPedido='', cocinero=None, mesero=None, platos=None, restaurante=None, reserva=None, domiciliario=None):
        self.mesa = mesa
        self.tipoPedido = tipoPedido
        self.cocinero = cocinero
        self.mesero = mesero
        self.platos = platos if platos is not None else []
        self.restaurante = restaurante
        self.reserva = reserva
        self.domiciliario = domiciliario
        self.verificado = False

    # Metodos setter
    def setMesa(self, mesa):
        self.mesa = mesa

    def removerPlato(self, plato):
        self.platos.remove(plato)

    def agregarPlato(self, plato):
        self.platos.append(plato)
    
    def setVerificado(self, verificado):
        self.verificado = verificado
    
    # Metodos getter
    def isVerificado(self):
        return self.verificado

    def getTiempoTotal(self):
        tiempoTotal = 0
        for plato in self.platos:
            tiempoTotal += plato.getTiempoPreparacion()
        return tiempoTotal

    def getPlatos(self):
        return self.platos

    def getCocinero(self):
        return self.cocinero

    def getMesero(self):
        return self.mesero

    def getDomiciliario(self):
        return self.domiciliario

    def getPrecioTotal(self):
        precioTotal = 0
        for plato in self.platos:
            precioTotal += plato.getPrecio()
        return precioTotal
    
    # Metodos de funcionalidad
    def verificarPedido(self, restaurante, pedido):
        mesa = restaurante.buscarMesaDisponible()
        pedido.setMesa(mesa)
        pedido.setVerificado(True)
        self.actualizarInventario(restaurante, pedido)
        return mesa

    def actualizarInventario(self, restaurante, pedido):
        restaurante.actualizarTiempoEmpleados(pedido)
        restaurante.actualizarInsumos(pedido)

    def imprimirPlatos(self):
        stringPlatos = ""
        for i, plato in enumerate(self.platos, 1):
            stringPlatos += f"\n   Plato número {i}: {plato.detallesPlato()}\n"
        return stringPlatos
    
    # ToString de la clase
    def __str__(self):
        mesaStr = str(self.mesa) if self.mesa is not None else "N/A"
        meseroStr = self.mesero.getNombre() if self.mesero is not None else "N/A"
        domiciliarioStr = self.domiciliario.getNombre() if self.domiciliario is not None else "N/A"
        resumen = self.reserva.resumenReservaPedido() if self.reserva is not None else "no tiene reserva asociada"

        return f"mesa: {mesaStr}" \
               f"\n   cocinero: {self.cocinero}" \
               f"\n   mesero: {meseroStr}" \
               f"\n   domiciliario: {domiciliarioStr}" \
               f"\n   número de platos: {len(self.platos)}" \
               f"\n   platos: {self.imprimirPlatos()}" \
               f"\n   Este pedido tiene esta reserva: {resumen}" \
               f"\n   tipoPedido: {self.tipoPedido}"