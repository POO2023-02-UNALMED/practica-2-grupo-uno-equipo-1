from datetime import datetime
from gestorAplicacion.Personas.persona import Persona
from gestorAplicacion.Restaurante.material import Material
from gestorAplicacion.Restaurante.turno import Turno
from gestorAplicacion.Restaurante.restaurante import Restaurante
from gestorAplicacion.Restaurante.pedido import Pedido

class Empleado(Persona):

    #Constructor de la Clase Empleado

    def __init__(self,nombre="",cedula=000000,puesto=None,restaurante=None,turno=None):
        super().__init__(nombre,cedula)
        self.puesto=puesto
        self.restaurante=restaurante
        self.turnos=[]
        self.turnos.append(turno)
        self.turno=turno
        self.salario=0
        self.puntuacion=0
        self.fechaContracion=None
        self.setFechaContratacion(datetime.now().day)

    #Metodos getter

    def getTurno(self):
        return self.turno

    def getTurnos(self):
        return self.turnos

    def getPuesto(self):
        return self.puesto

    def getSalario(self):
        return self.salario

    def getFechaContratacion(self):
        return self.fechaContracion

    def getRestaurante(self):
        return self.restaurante

    def getPuntuacion(self):
        return self.puntuacion

    #Metodos Setter

    def setTurnos(self,turnos):
        self.turnos=turnos

    def setTurno(self,turno):
        self.turno=turno

    def setPuesto(self,puesto):
        self.puesto=puesto

    def setSalario(self,salario):
        self.salaio=salario

    def setRestaurante(self,restaurante):
        self.restaurante=restaurante

    def setPuntuacion(self,puntuacion):
        self.puntuacion=puntuacion

    def setFechaContratacion(self,fecha):
        self.fechaContracion=fecha

    #Metodo encargado de transformar los dias de la libreria Datetime al ENUM de turnos

    def clasificarDia(self, fecha):
        diaDeLaSemana = fecha.strftime('%A')
        if (diaDeLaSemana=="Saturday"):
            return "SABADO"
        elif (diaDeLaSemana=="SUNDAY"):
            return "DOMINGO"
        else:
            return "SEMANA"

    #Metodo encargado de verificar la capacidad del empleado de cumplir con su trabajo

    def verificarTiempo(self, empleado, tiempoPreparacion=0):
        fechaActual = datetime.date.today()
        dia = self.clasificarDia(fechaActual)
        if (tiempoPreparacion == 0):
            for turno in empleado.getTurnos():
                if (turno.getTipo().toString() == dia):
                    if not (turno.isCobrado()):
                        tiempoDisponible = turno.getHoras() * 60
                        if (tiempoDisponible > tiempoPreparacion):
                            return True
            return False
        else:
            if(empleado.getPuesto() == "domiciliario"):
                for turno in empleado.getTurnos():
                    if (turno.getTipo().toString() == dia):
                        if not (turno.isCobrado()):
                            tiempoDisponible = turno.getHoras()* 60
                            if (tiempoDisponible > Pedido.TIEMPO_DOMICILIO):
                                return True
            elif (empleado.getPuesto() == "mesero"):
                for turno in empleado.getTurnos():
                    if (turno.getTipo().toString() == dia):
                        if not(turno.isCobrado()):
                            tiempoDisponible = turno.getHoras()* 60
                            if(tiempoDisponible > Pedido.TIEMPO_MESERO):
                                return True
            return False

    #Metodo encargado de reportar el daño en un material y lo elimina del inventario automaticamente

    def reportarDano(self, material, cantidad):
        self.restaurante.botarMaterial(material, cantidad)

    #Metodo encargado de verificar que se completen los turnos

    def turnosCompletados(self, empleado):
        for turno in empleado.getTurnos():
            if (turno.isCompletado()==True & turno.isCobrado()==False):
                turno.setCobrado(True)
                empleado.setSalario(turno.getSalario())

    #Metodo encargado de verificar que un turno ha sido completado

    def turnoActual(self):
        for turno in self.turnos:
            if not (turno.isCobrado()):
                return turno
        return None

    def toString(self):
        return "Nombre: " + self.getNombre()+ " Puesto: "+ self.getPuesto()

    #Metodo encargado de agregar turnos a los empleados

    def agregarTurno(self, turno):
        self.turnos.append(turno)

    def puntuacion(self):
        return "La puntacion del Empleado es: "+ self.getPuntuacion()

    def trabajo(self):
        return "Empleado del restaurante"

    def detallesEmpleado(self):
        return "Nombre: " + self.getNombre()+"\nCedula: " + self.getCedula()+"\nPuesto: " + self.getPuesto()+"\nTurno: " + self.getTurnos().get(0).getTipo()+"\nSalario: " + self.getTurnos().get(0).getSalario()+"\n"+self.puntuacion()+"\n"+self.trabajo()+"\n"