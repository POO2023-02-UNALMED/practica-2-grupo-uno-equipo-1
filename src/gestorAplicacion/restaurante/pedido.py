
class Pedido():

    TIEMPO_DOMICILIO = 45
    TIEMPO_MESERO = 30

    def __init__(self, platos = [], mesa=None, tipoPedido='', cocinero=None, mesero=None, restaurante=None, reserva=None, domiciliario=None):
        # from gestorAplicacion.Personas.empleado import Empleado
        self.mesa = mesa
        self.tipoPedido = tipoPedido
        self.cocinero = cocinero
        self.mesero = mesero
        self.platos = platos 
        self.restaurante = restaurante
        self.reserva = reserva
        self.domiciliario = domiciliario
        self.verificado = False
        restaurante.pedidos.append(self)

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
        print("Actualizando inventario...")
        restaurante.actualizarTiempoEmpleados(pedido)
        restaurante.actualizarInsumos(pedido)

    def imprimirPlatos(self):
        stringPlatos = ""
        i=1
        for plato in self.platos:
            stringPlatos += f"\nPlato número {i}: {plato.detallesPlato()}\n"
            i+=1
        return stringPlatos


    def __str__(self):
        # Crear una lista para almacenar las partes de la cadena
        partes = []

        # Añadir la información de la mesa si está disponible
        if self.mesa is not None:
            partes.append(f"mesa: {self.mesa}")

        # Añadir la información del cocinero si está disponible
        if self.cocinero is not None:
            partes.append(f"{self.cocinero}")

        # Añadir la información del mesero si está disponible
        if self.mesero is not None:
            meseroStr = self.mesero.getNombre()
            if meseroStr != "N/A":
                partes.append(f"mesero: {meseroStr}")

        # Añadir la información del domiciliario si está disponible
        if self.domiciliario is not None:
            domiciliarioStr = self.domiciliario.getNombre()
            if domiciliarioStr != "N/A":
                partes.append(f"domiciliario: {domiciliarioStr}")

        # Añadir la información de los platos
        partes.append(f"número de platos: {len(self.platos)}")
        partes.append(f"{self.imprimirPlatos()}")

        # Añadir la información de la reserva si está disponible
        if self.reserva is not None:
            resumen = self.reserva.resumenReservaPedido()
            if resumen != "no tiene reserva asociada":
                partes.append(f"Este pedido tiene esta reserva: {resumen}")

        # Añadir la información del tipo de pedido
        partes.append(f"tipoPedido: {self.tipoPedido}")

        # Unir todas las partes en una sola cadena de texto
        return "\n   ".join(partes)
