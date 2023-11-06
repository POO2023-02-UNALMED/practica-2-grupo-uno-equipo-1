from datetime import datetime
from gestorAplicacion.Personas.persona import Persona
from gestorAplicacion.Cosas.material import Material
from gestorAplicacion.Cosas.mesa import Mesa
from gestorAplicacion.Cosas.pedido import Pedido
from gestorAplicacion.Cosas.plato import Plato
from gestorAplicacion.Cosas.restaurante import Restaurante
from gestorAplicacion.Cosas.turno import Turno

class Empleado(Persona):
    def __init__(self, nombre="", cedula=000000, puesto=None, restaurante=None, turno=None):
        super.__init__(nombre, cedula)
        self.puesto = puesto
        self.restaurante = restaurante
        self.turnos = []
        self.turnos.append(turno)
        self.turno = turno
        self.salario = 0.0
        self.puntuacion = 0.0
        self.fechaContratacion = None
        self.setFechaContratacion(datetime.date.today().day())

    def getTurno(self):
      return self.turno

    def getTurnos(self):
      return self.turnos

    def getPuesto(self):
      return self.puesto

    def getSalario(self):
      return self.salario

    def getFechaContratacion(self):
      return self.fechaContratacion

    def getRestaurante(self):
      return self.restaurante

    def getPuntuacion(self):
      return self.puntuacion

    def setTurnos(self, turnos):
      self.turnos = turnos

    def setTurno(self, turnos):
      self.turnos = turnos

    def setPuesto(self, puesto):
      self.puesto = puesto

    def setSalario(self, salario):
      self.salario = salario

    def setRestaurante(self, restaurante):
      self.restaurante=restaurante

    def setPuntuacion(self, puntuacion):
      self.puntuacion = puntuacion

    def setFechaContratacion(self, fechaContratacion):
      self.fechaContratacion = fechaContratacion

    def clasificarDia(self, fecha):
      diaDeLaSemana = fecha.strftime('%A')
      if (diaDeLaSemana=="Saturday"):
        return "SABADO"
      elif (diaDeLaSemana=="SUNDAY"):
        return "DOMINGO"
      else:
        return "SEMANA"

    def verificarTiempo(self, empleado, tiempoPreparacion=0):
        fechaActual = datetime.date.today()
        dia = self.clasificarDia(fechaActual)
        if (tiempoPreparacion == 0):
            for (turno in empleado.getTurnos()):
                if (turno.getTipo().toString().equals(dia)):
                    if not (turno.isCobrado()):
                        tiempoDisponible = turno.getHoras() * 60
                        if (tiempoDisponible > tiempoPreparacion):
                            return True
        return False
        else:
            if(empleado.getPuesto().equals("domiciliario")):
                for (turno in empleado.getTurnos()):
                    if (turno.getTipo().toString().equals(dia)):
                        if not (turno.isCobrado()):
                            tiempoDisponible = turno.getHoras()* 60 
                                if(tiempoDisponible > Pedido.TIEMPO_DOMICILIO) :
                                    return True
            elif (empleado.getPuesto().equals("mesero")):
                for (turno in empleado.getTurnos()):
                    if (turno.getTipo().toString().equals(dia)):
                        if not(turno.isCobrado()):
                            tiempoDisponible = turno.getHoras()* 60 
                                if(tiempoDisponible > Pedido.TIEMPO_MESERO):
                                    return True
          return False


    def reportarDano(self, material, cantidad):
       self.restaurante.botarMaterial(material, cantidad)


    def turnosCompletados(self, empleado):
		for(turno in empleado.getTurnos()):
			if (turno.isCompletado()==True & turno.isCobrado()==False):
					turno.setCobrado(True)
					empleado.setSalario(turno.getSalario())

	def turnoActual(self):
		for(turno in self.turnos):
			if not (turno.isCobrado()):
				return turno
		return None

	def toString(self):
		return "Nombre: " + self.getNombre()+ " Puesto: "+ self.getPuesto()  
	
    def agregarTurno(Turno turno:
		self.turnos.add(turno)
	//Metodo para mostrar la puntuacion del Empleado
	String puntuacion(:
	  return "La puntacion del Empleado es: "+ self.getPuntuacion()

	//Metodo para mostrar la descripcion del trabajo del Empleado
	String trabajo(:
	  return "Empleado del restaurante"
	//Metodo para mostrar detalles de los empleados
	String detallesEmpleado(:
		return 
		  "Nombre: " + self.getNombre()+
		  "\nCedula: " + self.getCedula()+
		  "\nPuesto: " + self.getPuesto()+
		  "\nTurno: " + self.getTurnos().get(0).getTipo()+
		  "\nSalario: " + self.getTurnos().get(0).getSalario()+		  
		  "\n"+self.puntuacion()+

		  "\n"+self.trabajo()+"\n"


