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
		self.pagosEmpleados = 0
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

		return self.gastosMateriales

	def GastoMaterialEspecifico(self, nombre_material):
		total_gasto_material = 0
		for pedido in self.restaurante.getPedidos():
			for plato in pedido.getPlatos():
				for material, cantidad_utilizada in plato.getIngredientes().items():
					if material.getNombre() == nombre_material:
						total_gasto_material += material.getPrecioUnitario() * cantidad_utilizada
						
		return total_gasto_material

    #Calcula el pago de un solo empleado


    # Calcula el Pago total de todos los Empleados
	
	def pagosEmpleados(self):
		totalPagos = 0
		for empleado in self.restaurante.getEmpleados():
			totalPagos += self.pagoEmpleado(empleado)
		self.pagosEmpleados = totalPagos  # Actualiza el atributo pagosEmpleados
		return totalPagos
	
	def pagoEmpleado(self, empleado):
		totalPago = 0
		for turno in empleado.getTurnos():
			totalPago += turno.getSalario()
		return totalPago


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