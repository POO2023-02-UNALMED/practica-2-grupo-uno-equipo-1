from datetime import datetime
#from baseDatos.serializador import Serializador
# En uiMain/administrador.py
from gestorAplicacion.restaurante.financia import Financia
from restaurante.material import Material, Tipo
from restaurante.mesa import Mesa
from restaurante.pedido import Pedido
from restaurante.plato import Plato
from restaurante.reserva import Reserva
from restaurante.restaurante import Restaurante
from restaurante.turno import Turno, TipoTurno
from personas.cliente import Cliente
from personas.cocinero import Cocinero
from personas.domiciliario import Domiciliario
from personas.empleado import Empleado
from personas.mesero import Mesero
from personas.persona import Persona

class Administrador ():
	if __name__ == "__main__":
		restaurante = Restaurante()

#Crear un objeto Financia
		financia = Financia(restaurante)
		res = Material(Tipo.RES.value, 100, 100)
		especias = Material(Tipo.ESPECIAS.value, 100, 50)
		aceites = Material(Tipo.ACEITES.value, 100, 100)
		pollos = Material(Tipo.POLLOS.value, 100, 200)
		vinos = Material(Tipo.VINOS.value, 100, 300)
		cebollas = Material(Tipo.CEBOLLAS.value, 100, 50)
		champinones = Material(Tipo.CHAMPINONES.value, 500, 100)
		ajos = Material(Tipo.AJOS.value, 100, 30)
		tomates = Material(Tipo.TOMATES.value, 400, 200)
		quesos = Material(Tipo.QUESOS.value, 300, 150)
		cerdos = Material(Tipo.CERDOS.value, 100, 200)
		atun = Material(Tipo.ATUN.value, 100, 250)
		panes = Material(Tipo.PANES.value, 200, 50)
		pescados = Material(Tipo.PESCADOS.value ,200 ,300 )
		papas = Material(Tipo.PAPAS.value ,200 ,100 )
		huevos = Material(Tipo.PAPAS.value ,200 ,100 )

		#Crear turnos
		turno1 = Turno(TipoTurno.SEMANA.value, 2.0, 50000)
		turno2 = Turno(TipoTurno.SEMANA.value, 8.0, 60000)
		turno3 = Turno(TipoTurno.SEMANA.value, 2.0, 70000)
		turno4 = Turno(TipoTurno.DOMINGO.value, 8.0, 55000)
		turno5 = Turno(TipoTurno.SEMANA.value, 2.0, 65000)
		turno6 = Turno(TipoTurno.SEMANA.value, 8.0, 75000)
		turno7 = Turno(TipoTurno.SEMANA.value, 2.0, 60000)
		turno8 = Turno(TipoTurno.SEMANA.value, 8.0, 70000)
		turno9 = Turno(TipoTurno.SEMANA.value, 2.0, 80000)
		turno10 = Turno(TipoTurno.SEMANA.value, 8.0, 65000)
		turno11 = Turno(TipoTurno.SEMANA.value, 3.0, 80000)
		turno12 = Turno(TipoTurno.SABADO.value, 7.0, 50000)
		turno13 = Turno(TipoTurno.SABADO.value, 3.0, 60000)
		turno14 = Turno(TipoTurno.SEMANA.value, 7.0, 70000)
		turno15 = Turno(TipoTurno.SEMANA.value, 2.0, 55000)
		turno16 = Turno(TipoTurno.DOMINGO.value, 3.0, 55000)
		turno17 = Turno(TipoTurno.SABADO.value, 2.0, 55000)
		#Crear empleados
		empleado1 = Mesero("Juan", 123456789, "mesero", restaurante, turno1)
		empleado1.agregarTurno(turno2)
		empleado2 = Cocinero("Fernando", 234567891, "cocinero", restaurante, turno2)
		empleado2.agregarTurno(turno3)
		empleado3 = Domiciliario("Santiago", 345678912, "domiciliario", restaurante, turno4)
		empleado1.agregarTurno(turno5)
		empleado4 = Mesero("Jhon", 123456789, "mesero", restaurante, turno6)
		empleado1.agregarTurno(turno7)
		empleado5 = Cocinero("Moises", 234567891, "cocinero", restaurante, turno8)
		empleado2.agregarTurno(turno9)
		empleado6 = Domiciliario("Rigo", 345678912, "domiciliario", restaurante, turno10)
		empleado1.agregarTurno(turno11)
		empleado7 = Mesero("Brayan", 123456789, "mesero", restaurante, turno12)
		empleado1.agregarTurno(turno13)
		empleado8 = Cocinero("Felipe", 234567891, "cocinero", restaurante, turno14)
		empleado2.agregarTurno(turno15)
		empleado9 = Domiciliario("Martin", 345678912, "domiciliario", restaurante, turno16)
		empleado1.agregarTurno(turno17)
		pedido = Pedido()
		plato = Plato()
		for mesa1 in restaurante.getMesas():
			mesa1.anadirNumero(mesa1.getNumeroMesa())
		restaurante.borrarReservasViejas()