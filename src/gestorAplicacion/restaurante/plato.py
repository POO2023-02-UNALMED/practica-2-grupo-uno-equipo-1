from gestorAplicacion.personas.empleado import Empleado

class Plato:
    def __init__(self, nombre="", precio=0, tiempoPreparacion=0, descripcion = 'Platillo simple'):
        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._tiempoPreparacion = tiempoPreparacion
        self._ingredientes = {}
        self._verificadoInsumos = False
    
    # Métodos getter
    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getPrecio(self):
        return self.precio

    def getIngredientes(self):
        return self.ingredientes

    def getTiempoTotal(self, platos):
        tiempoTotal = 0
        for plato in platos:
            tiempoTotal += plato.getTiempoPreparacion()
        return tiempoTotal
    
    def getNumeroDeIngredientes(self):
        return len(self.ingredientes)
    
    def getTiempoPreparacion(self):
        return self.tiempoPreparacion;

    def isVerificadoInsumos(self):
        return self.verificadoInsumos
    
    # Métodos setter
    def setNombre(self, nombre):
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setPrecio(self, precio):
        self.precio = precio

    def setIngredientes(self, ingredientes):
        self.ingredientes = ingredientes
    
    def setTiempoPreparacion(self, tiempoPreparacion): 
        self.tiempoPreparacion = tiempoPreparacion
    
    def setVerificadoInsumos(self,verificadoInsumos):
        self.verificadoInsumos = verificadoInsumos;
    
    # Metodo para verificar los insumos de un plato
    def verificar_insumos(self, plato):
        for ingrediente, cantidad_plato in plato.get_ingredientes().items():
            if ingrediente.get_cantidad() < cantidad_plato:
                # Dejarlo en False (no se hace nada aquí en Python)
                pass
            if ingrediente.get_cantidad() >= cantidad_plato:
                self.set_verificado_insumos(True)
        return self.is_verificado_insumos()
    def mostrarIngredientes(self):
        tipos=[]
        for ingrediente in self.ingredientes:
            tipos.append(ingrediente.getNombre())

        return tipos
    def __str__(self):
        return 
    "\n   Nombre: " + getNombre()  + "\n   Precio: " + getPrecio() + "\n   Descripcion: " + getDescripcion()  + "\n   Tiempo de preparacion: " + getTiempoPreparacion() + "\n   Ingredientes: " + mostrarIngredientes().str()