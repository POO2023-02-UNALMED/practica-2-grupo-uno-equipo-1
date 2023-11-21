from datetime import datetime

class Financia():
	def __init__(self, restaurante=None, presupuesto=1000000, gastosMateriales=0, gastoMaterialEspecifico=0, pagosEmpleados=0, gananciasBrutas=0, gananciasNetas=0):
		from gestorAplicacion.Restaurante.restaurante import Restaurante
		from gestorAplicacion.Restaurante.material import Material
		from gestorAplicacion.Restaurante.pedido import Pedido
		from gestorAplicacion.Restaurante.reserva import Reserva
		from gestorAplicacion.Restaurante.mesa import Mesa
		from gestorAplicacion.Restaurante.turno import Turno
		from gestorAplicacion.Restaurante.plato import Plato
		from gestorAplicacion.Personas.empleado import Empleado
		from gestorAplicacion.Personas.persona import Persona
		self.presupuesto = presupuesto
		self.gastosMateriales = gastosMateriales
		self.gastoMaterialEspecifico = gastoMaterialEspecifico
		self.pagosEmpleados = pagosEmpleados
		self.gananciasBrutas = gananciasBrutas
		self.gananciasNetas = gananciasNetas
		self.restaurante = restaurante


	def getPresupuesto(self):
		return self.presupuesto

	def getGastosMateriales(self):
		return self.gastosMateriales

	def getGastoMaterialEspecifico(self):
		return self.gastoMaterialEspecifico

	def getPagosEmpleados(self):
		return self.pagosEmpleados

	def getGananciasBrutas(self):
		return self.gananciasBrutas

	def getGananciasNetas(self):
		return self.gananciasNetas

	def GastosMateriales(self):
		total_gastos_materiales = 0
		# Recorre cada pedido del restaurante
		for pedido in self.restaurante.getPedidos():
			# Recorre cada plato de los pedidos
			for plato in pedido.getPlatos():
				# Recorre los ingredientes de cada plato con su cantidad usada y luego multiplica el precio unitario de material por su cantidad
				for material, cantidad_utilizada in plato.getIngredientes().items():
					total_gastos_materiales += material.getPrecioUnitario() * cantidad_utilizada
		self.gastosMateriales = total_gastos_materiales

	def GastoMaterialEspecifico(self, nombre_material):
		total_gasto_material = 0
		for pedido in self.restaurante.getPedidos():
			for plato in pedido.getPlatos():
				for material, cantidad_utilizada in plato.getIngredientes().items():
					if material.getNombre() == nombre_material:
						total_gasto_material += material.getPrecioUnitario() * cantidad_utilizada
						
		return total_gasto_material

    #Calcula el pago de un solo empleado
	def pagoEmpleado(self, empleado):
		totalPago = 0
		for turno in empleado.getTurnos(self):
			pago = turno.getSalario(self)
			horasExtras = turno.HorasExtras(self)
			if (horasExtras > 0):
				pagoHoraExtra = 1.5 # Supongamos que las horas extras se pagan a 1.5 veces el salario regular por hora
				pago += horasExtras * (empleado.getSalario() / turno.getHoras()) * pagoHoraExtra
			totalPago += pago
		return totalPago

    #Calcula el Pago total de todos los Empleados
	def PagosEmpleados(self,restaurante):
		totalPago = 0
		for empleado in restaurante.getEmpleados():
			totalPago += empleado.getSalario()
			totalPago += self.liquidacionEmpleado(empleado.getNombre()) # Sumar la liquidación del empleado
			for turno in empleado.getTurnos():
				if (turno.isCompletado() and not turno.isCobrado(self)):
					horasExtras = turno.HorasExtras()
					if (horasExtras > 0):
						pagoHoraExtra = 1.5 # Supongamos que las horas extras se pagan a 1.5 veces el salario regular por hora
						totalPago += horasExtras * (empleado.getSalario() / turno.getHoras()) * pagoHoraExtra
		self.pagosEmpleados = totalPago
		return self.pagosEmpleados

    #Calcula las ganancias Brutas del restaurante
	def GananciasBrutas(self):
		totalGananciasBrutas = 0
		for pedido in self.restaurante.getPedidos():
			totalGananciasBrutas += pedido.getPrecioTotal()
		self.gananciasBrutas = totalGananciasBrutas
		return self.gananciasBrutas

    #Calcula las ganancias netas del restaurante
	def GananciasNetas(self):
		totalGastos = self.gastosMateriales + self.pagosEmpleados  # Acceder a los valores directamente
		totalIngresos = self.GananciasBrutas()
		self.gananciasNetas = totalIngresos - totalGastos
		return self.gananciasNetas

    #Calcula el presupuesto considerando las ganancias del restaurante
	def Presupuesto(self):
		totalGastos = self.GastosMateriales() + self.pagosEmpleados(self.restaurante)
		gananciasNetas = self.gananciasNetas()
		self.presupuesto = self.presupuesto - totalGastos + gananciasNetas
		return self.presupuesto