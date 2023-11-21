from datetime import datetime

class Financia():
	
	def __init__(self, restaurante=None, presupuesto=1000000):
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
			self.gastosMateriales = 0
			self.gastoMaterialEspecifico = 0
			self.pagosEmpleados = 0
			self.gananciasBrutas = 0
			self.gananciasNetas = 0
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

	def gastosMateriales(self):
		total_gastos_materiales = 0
		for pedido in self.restaurante.getPedidos():
			for plato in pedido.getPlatos():
				for material, cantidad_utilizada in plato.getIngredientes().items():
					total_gastos_materiales += material.getPrecioUnitario() * cantidad_utilizada
		self.gastosMateriales = total_gastos_materiales
		return total_gastos_materiales

	def gastoMaterialEspecifico(self, material_seleccionado):
		total_gasto_material = 0
		for pedido in self.restaurante.getPedidos():
			for plato in pedido.getPlatos():
				for material, cantidad_utilizada in plato.getIngredientes().items():
					if material.getNombre() == material_seleccionado:
						total_gasto_material += cantidad_utilizada * material.getPrecioUnitario()
		self.gastoMaterialEspecifico = total_gasto_material
		return total_gasto_material

	def pagosEmpleados(self):
		totalPagos = 0
		for empleado in self.restaurante.getEmpleados():
			totalPagos += self.calcularPagoEmpleado(empleado)
			self.pagosEmpleados = totalPagos
		return totalPagos


    #Calcula las ganancias Brutas del restaurante
	def gananciasBrutas(self):
		totalGananciasBrutas = 0
		for pedido in self.restaurante.getPedidos():
			totalGananciasBrutas += pedido.getPrecioTotal()
		self.gananciasBrutas = totalGananciasBrutas
		return self.gananciasBrutas

    #Calcula las ganancias netas del restaurante
	def gananciasNetas(self):
		totalGastos = self.gastosMateriales + self.pagosEmpleados  # Acceder a los valores directamente
		totalIngresos = self.GananciasBrutas()
		self.gananciasNetas = totalIngresos - totalGastos
		return self.gananciasNetas

    #Calcula el presupuesto considerando las ganancias del restaurante
	def presupuesto(self):
		totalGastos = self.GastosMateriales() + self.pagosEmpleados(self.restaurante)
		gananciasNetas = self.gananciasNetas()
		self.presupuesto = self.presupuesto - totalGastos + gananciasNetas
		return self.presupuesto