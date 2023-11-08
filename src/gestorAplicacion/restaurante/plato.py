from Restaurante.material import Tipo

class Plato:
    def __init__(self, nombre="", precio=0, tiempoPreparacion=0, descripcion = 'Platillo simple'):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.tiempoPreparacion = tiempoPreparacion
        self.ingredientes = {}
        self.verificadoInsumos = False
    
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
        return self.tiempoPreparacion

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
        self.verificadoInsumos = verificadoInsumos
    
    # Metodo para verificar los insumos de un plato
    def verificar_insumos(self, plato):
        for ingrediente, cantidad_plato in plato.get_ingredientes().items():
            if ingrediente.get_cantidad() >= cantidad_plato:
                self.setVerificadoInsumos(True)
        return self.isVerificadoInsumos()
    
    def mostrarIngredientes(self):
        tipos=[]
        for ingrediente in self.ingredientes:
            tipos.append(ingrediente.getNombre())
        return tipos
    
    def detallesPlato(self):
        return f"\nNombre: {self.getNombre()}\nPrecio: {self.getPrecio()}\nDescripcion: {self.getDescripcion()}\nTiempo de preparacion: {self.getTiempoPreparacion()}\nIngredientes: {self.mostrarIngredientes().__str__()}