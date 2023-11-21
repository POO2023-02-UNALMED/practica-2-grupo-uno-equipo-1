from datetime import datetime
from gestorAplicacion.Restaurante.reserva import Reserva
from gestorAplicacion.Restaurante.pedido import Pedido
from gestorAplicacion.Restaurante.material import Material
from gestorAplicacion.Restaurante.material import Tipo
from gestorAplicacion.Restaurante.mesa import Mesa
from gestorAplicacion.Personas.cliente import Cliente

class Restaurante():

	#Cuenta el tamaño de una lista
	def contadorListado (self, listado):
		contador = 0
		for elemento in listado:
			if (elemento != None):
				contador += 1
		return contador

	def __init__(self, listadoMesas=None, listadoEmpleados=None, listadoClientes=None, inventario=None, listadoAspEmpleados=None, restaurante = None):
		self.NOMBRE = "Le Quasó"
		self.empleadoDelMes = None
		self.numMesas = 0
		self.numEmpleados = 0
		self.numClientes = 0
		self.pedidos = []
		self.menu = listadoMesas if listadoMesas is not None else []
		self.listadoMesas = listadoMesas if listadoMesas is not None else []
		self.listadoEmpleados = listadoEmpleados if listadoEmpleados is not None else []
		self.listadoClientes = listadoClientes if listadoClientes is not None else []
		self.inventario = inventario if inventario is not None else {}
		self.listadoAspEmpleados = listadoAspEmpleados if listadoAspEmpleados is not None else []
		self.numMesas += self.contadorListado(self.listadoMesas)
		self.numEmpleados += self.contadorListado(self.listadoEmpleados)
		self.numClientes += self.contadorListado(self.listadoEmpleados)

    #Metodos getter
	def getNombre (self):
		return self.NOMBRE

	def getEmpleadoDelMes (self):
		return self.empleadoDelMes

	def getNumMesas (self):
		return self.numMesas

	def getNumEmpleados (self):
		return self.numEmpleados

	def getNumClientes (self):
		return self.numClientes

	def getEmpleados (self):
		return self.listadoEmpleados

	def getClientes (self):
		return self.listadoClientes

	def getMesas (self):
		return self.listadoMesas
	
	def getMenu(self):
		return self.menu
	
	def getCocineros (self):
		cocineros = []
		for empleado in self.listadoEmpleados:
			if empleado.getPuesto() == "cocinero":
				cocineros.append(empleado)
		return cocineros
	
	def getMeseros(self):
		meseros = []
		for empleado in self.listadoEmpleados:
			if empleado.getPuesto() == "mesero":
				meseros.append(empleado)
		return meseros	
	
	def getDomiciliarios(self):
		domiciliarios = []
		for empleado in self.listadoEmpleados:
			if empleado.getPuesto() == "mesero":
				domiciliarios.append(empleado)
		return domiciliarios	
	

	def getInventario (self):
		return self.inventario

	def getPedidos(self):
		return self.pedidos

	def getAspEmpleados (self):
		return self.listadoAspEmpleados

    #Metodos setter
	def setMesas(self,mesas):
		self.listadoMesas=mesas
	
	def setMenu(self, menu):
		self.menu=menu

	def setEmpleadoDelMes (self, empleadoDelMes):
		if (empleadoDelMes == None):
			puntuacionMaxima = 0
			for empleado in self.listadoEmpleados:
				if (empleado.getPuntuacion() > puntuacionMaxima):
					puntuacionMaxima = empleado.getPuntuacion()
					empleadoDelMes = empleado
		self.empleadoDelMes = empleadoDelMes

	def setEmpleados(self, empleados):
		self.listadoEmpleados=empleados

	def setClientes(self, clientes):
		self.listadoClientes=clientes

	def setInventario(self, inv):
		self.inventario=inv

	def setNumMesas(self, numMesas):
		self.numMesas = numMesas

	def setNumClientes(self, numClientes):
		self.numClientes = numClientes

	def setNumEmpleados(self, numEmpleados):
		self.numEmpleados = numEmpleados

	def setPedidos(self, pedidos):
		self.pedidos=pedidos


	#Metodos funcionalidad gestion de pedidos

	#Se agrega un pedido
	def agregarPedido(self, pedido):
		self.pedidos.append(pedido)


	#Se verifica el menu si es apto para ofrecerlo
	def verificarMenu(self, menu):
		menuVerificado = []
		for plato in menu:
			# Se verifica si cada plato cumple
			if (plato.verificarInsumos(plato)):
				menuVerificado.append(plato)
		return menuVerificado



	#Encontrar reserva, aqui se mira si segun los datos en el pedido hay una reserva
	def encontrarReserva(self, numMesa, nombre):
		mesa = self.encontrarMesa(numMesa)
		if mesa!=None:
			for reserva in mesa.getReservas():
				if ((reserva.getDuenoReserva().getNombre()) == nombre):
					return reserva
		return None

	#Clasificar empleados por su tipo
	def clasificarEmpleados(self, empleados, tipo):
		empleadosClasificados = []
		for empleado in empleados:
			if (empleado.getPuesto() == tipo):
				empleadosClasificados.append(empleado)
		return empleadosClasificados
	
	def encontrarEmpleado(self, nombreEmpleado):
		for empleado in self.getEmpleados():
			if empleado.getNombre() == nombreEmpleado:
				return empleado

	#Encontrar una mesa disponible en la fecha de el dia actual
	def buscarMesaDisponible(self):
		fechaActual = datetime.now()
		for mesa in self.listadoMesas:
			for reserva in mesa.getReservas():
				if not (reserva.getDiaReserva() == fechaActual):
					return mesa
		return None

	#Verificar los cocineros aptos para la cantidad de platos
	def verificarCocineros(self, empleados, platos):
		cocinerosVerificados = []

		cocineros = self.clasificarEmpleados(empleados, "cocinero")
		tiempoPreparacion = platos[0].getTiempoTotal(platos)

		for empleado in cocineros:
			if (empleado.verificarTiempoCocinero(empleado, tiempoPreparacion)):
				cocinerosVerificados.append(empleado)
		
		return cocinerosVerificados

	#Verificar los domiciliarios aptos para entregar el pedido
	def verificarDomiciliarios(self, empleados):
		domiciliarios = self.clasificarEmpleados(empleados, "domiciliario")
		domiciliariosVerificados = []
		for empleado in domiciliarios:
			if (empleado.verificarTiempoGeneral(empleado)):
				domiciliariosVerificados.append(empleado)
		return domiciliariosVerificados

	#Verificar los meseros aptos para entregar
	def verificarMeseros(self, empleados):
		meseros = self.clasificarEmpleados(empleados, "mesero")
		meserosVerificados = []
		for empleado in meseros:
			if (empleado.verificarTiempoGeneral(empleado)):
				meserosVerificados.append(empleado)
		return meserosVerificados

	#Filtrar los pedidos consumo domicilio
	def imprimirPedidosDomicilios(self):
		pedidosDomicilio = self.getPedidosDomicilio()
		domicilios = ""
		for i in range(len(pedidosDomicilio)):
			domicilios += str((i + 1)) + ". " + pedidosDomicilio[i]
			domicilios += "\n-------------------------------------------------------\n"
		return domicilios
	def getPedidosDomicilio(self):
		pedidosDomicilio = []
		for pedido in self.getPedidos():
			if (pedido.getDomiciliario()!=None):
				pedidosDomicilio.append(pedido)
		return pedidosDomicilio

	#Filtrar los pedidos consumo(restaurante)
	def getPedidosRestaurante(self):
		pedidosRestaurante = []
		for pedido in self.getPedidos():
			if (pedido.isVerificado() and pedido.getDomiciliario()==None and pedido.getMesero()!=None):
				pedidosRestaurante.append(pedido)
		return pedidosRestaurante

	#Imprimir pedidos restaurante
	def imprimirPedidosRestaurante(self):
		pedidosRestaurante = ""
		for i in range(self.getPedidosRestaurante()):
			pedidosRestaurante += str((i + 1)) + ". " + self.getPedidosRestaurante()[i]
			pedidosRestaurante+="\n-------------------------------------------------------\n"
			return pedidosRestaurante

	#Actualizar insumos despues de ya estar verificado el pedido
	def actualizarInsumos(self, pedido):
		for plato in pedido.getPlatos():
			for material, cantidadUtilizada in plato.getIngredientes().items():
				material.restarCantidad(cantidadUtilizada)


	#Gestion de Pedidos
	def actualizarTiempoEmpleados(self, pedido):
		#Este metodo es  para actualizar el tiempo
		fechaActual = datetime.now()
		dia = pedido.getCocinero().clasificarDia(fechaActual)
		for pedidoi in self.getPedidos():
			if (pedidoi == pedido):
				for turno in pedido.getCocinero().getTurnos():
					if (turno.getTipo().value == dia):
						if not (turno.isCompletado()):
							turno.actualizarTiempo(turno, pedido.getTiempoTotal())
		#Llama metodo para cobrar turno
		pedido.getCocinero().turnosCompletados(pedido.getCocinero())
		#Si el pedido es de consumo en restaurante se actualiza tiempo a mesero
		if (pedido.getMesero() != None):
			pedido.getMesero().turnosCompletados(pedido.getMesero())
			for turno in pedido.getMesero().getTurnos():
				if (turno.getTipo().value == dia):
					if not (turno.isCompletado()):
						turno.actualizarTiempo(turno, Pedido.TIEMPO_MESERO)
		#Llama metodo para cobrar turno
		
		#Si el pedido es de consumo en domicilio se actualiza tiempo a domiciliario
		if (pedido.getDomiciliario()!=None):
			pedido.getDomiciliario().turnosCompletados(pedido.getDomiciliario())
			for turno in pedido.getDomiciliario().getTurnos():
				if(turno.getTipo().value == dia):
					if not (turno.isCobrado()):
						turno.actualizarTiempo(turno,Pedido.TIEMPO_DOMICILIO)
		#Llama metodo para cobrar turno
		#Buscar un por su nombre y puesto

	def buscarEmpleado(self, nombre, puesto):
		for empleado in self.listadoEmpleados:
			if((empleado.getNombre()) == nombre and (empleado.getPuesto()) == puesto):
				return empleado
		return  None

	#añade un a la lista de empleados
	def contratarEmpleado(self, novato):
		self.listadoEmpleados.append(novato)
		a = self.getNumEmpleados()
		self.setNumEmpleados(a+1)

	#Añade el cliente a la lista de clientes
	def afiliarCliente (self, nuevoCliente):
		self.listadoClientes.append(nuevoCliente)
		a = self.getNumClientes()
		self.setNumClientes(a+1)

	#añade la mesa a la lista de mesas
	def comprarMesa (self, numMesa,capacidad):
		nuevaMesa=Mesa(capacidad,numMesa)
		self.listadoMesas.append(nuevaMesa)
		a = self.getNumMesas()
		self.setNumMesas(a+1)

	#elimina la mesa del listado de mesas en base al número
	def eliminarMesa(self, numeroMesa):
		for mesa in self.listadoMesas:
			if(mesa.getNumeroMesa() == numeroMesa):
				self.listadoMesas.remove(mesa)
				break

	#Metodos gestion de inventario


	#Añade la cantidad del material suministrado junto a su fecha de vencimiento, en caso de
	#que lo ultimo no coincida se crea una instancia diferente y si no existe la instancia se crea
	def comprarMaterial (self, tipo, cantidad, precio, fecha=None):
		#revisa si ya existe el material
		if tipo in self.inventario:
			materialComprado = self.inventario[tipo]
			materialComprado.cantidad+=cantidad
			materialComprado.precioUnitario=precio
		#no existe por lo que lo crea
		else:
			nuevoMaterial = Material(tipo,cantidad,precio,None)
			self.inventario[tipo]=nuevoMaterial
			nuevoMaterial.precioUnitario=precio

	#Se encarga de eliminar un material especifico
	def botarMaterial(self, tipo,cantidad):
		if tipo in self.inventario:
			materialEliminado = self.inventario[tipo]
			if (materialEliminado.getCantidad()>=cantidad):
				materialEliminado.cantidad-=cantidad
			else:
				raise TypeError("Operacion Invalida")
		else:
			raise TypeError("No existe el elemento en el inventario")

	#metodo para decir si una accion no puede ser ejecutada
	def operacionInvalida(self):
		return "Operacion Inválida"

	def calcularValorInventario(self):
		valorTotal=0
		for material in self.inventario.values():
			valorTotal += material.getCantidad() * material.getPrecioUnitario()
		return valorTotal

	#Gestion de Reservas
	def borrarReservasViejas(self):
		for mesa1 in self.getMesas():
			mesa1.borrarReservasViejas()

	#retorna las mesas que son válidas (capacidad y fecha disponible) para la reserva
	def listadoMesasValidasParaReserva(self, reserva):
		mesasFiltradas = []
		for mesa in self.listadoMesas:
			if (mesa.suficienteCapacidad(reserva) and mesa.mesaCompatible(reserva)):
				mesasFiltradas.append(mesa)
		return mesasFiltradas

	#encuentra una mesa por su numero
	def encontrarMesa(self, numMesa):
		if self.getMesas() != None:
			for mesa1 in self.getMesas():
				a = mesa1.getNumeroMesa()
				if (int(numMesa) == a):
					return mesa1
		return None

	#Imprime las reservas por confirmar (sin mesa asignada)
	def imprimirReservas(self):
		r = ""
		listado = []
		for cliente1 in self.getClientes():
			listado.append(cliente1.getReserva())
		for reserva1 in listado:
			if (reserva1 != None):
				r += "\n"+reserva1.resumenReserva()+"\n\n+++++++++++++++++++++++++\n"
		if (r == ""):
			r = "\nNo se han hecho reservas\n"
		return r

	#Imprime las reservas confirmadas (con mesa asignada)
	def imprimirReservas2(self):
		r = ""
		listado = []
		for mesa1 in self.getMesas():
			listado += mesa1.getReservas()
		for reserva1 in listado:
			if (reserva1 != None):
				r += "\n"+reserva1.resumenReserva()+"\n\n+++++++++++++++++++++++++\n"
		if (r == ""):
			r = "\nNo se han confirmado reservas\n"
		return r

	#dice si el cliente si está guardado en la lista de clientes
	def verificarCliente(self, cedula):
		for cliente1 in self.getClientes():
			if (cedula == cliente1.getCedula()):
				return False
		return True

	#devuelve el objeto cliente en base a su cédula
	def obtenerCliente(self, cedula):
		for cliente1 in self.getClientes():
			if (cedula == cliente1.getCedula()):
				return cliente1
		return None

	#obtiene el cliente en base a la cédula llamando al método obtenerCliente, y le asigna la reserva
	def asignarReservaCliente(self, cedula, nombre, numAsistentes, diaReserva):
		if (self.verificarCliente(cedula)):
			c1 = Cliente(nombre, cedula)
			self.afiliarCliente(c1)
		c1 = self.obtenerCliente(cedula)
		diaReserva2 = Reserva.deStringAFecha(diaReserva)
		c1.setReserva(Reserva(c1, numAsistentes, diaReserva2))

	#retorna el listado de mesas que cumplen para la reserva que tenga asignada ek cliente
	def mesasQueCumplen(self, cedulaDuenoReserva):
		t = ""
		c1 = self.obtenerCliente(cedulaDuenoReserva)
		r1 = c1.getReserva()
		listado = self.listadoMesasValidasParaReserva(r1)
		for mesa1 in listado:
				t += "\n"+mesa1.resumenMesa()+"\n\n+++++++++++++++++++++++++\n"
		if (t == ""):
			t = "\nNo hay mesas válidas para esa reserva\n"
		return t

	#Si la mesa seleccionada cumple, le asigna la reserva a la mesa
	def confirmarReserva(self, numMesa, cedula):
		numMesa=int(numMesa)
		cedula=int(cedula)
		c1 = self.obtenerCliente(cedula)
		r1 = c1.getReserva()
		if (Mesa.verificarNumero(Mesa,numMesa)):
			mesa1 = self.encontrarMesa(numMesa)
			if (mesa1.suficienteCapacidad(r1)):
				mesa1.reservarMesa(r1)
				c1.setReserva(None)
				return "Reserva asignada a la mesa #"+numMesa
			else:
				return "La mesa seleccionada no tiene la capacidad suficiente, vuelva a intentarlo"
		else:
			return "No existe una mesa con ese número, por favor vuelva a intentarlo"