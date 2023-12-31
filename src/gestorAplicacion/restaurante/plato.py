class Plato:
    def __init__(self, nombre="", precio=0, tiempoPreparacion=0, descripcion = 'Platillo simple', ingredientes={}):
        from gestorAplicacion.Restaurante.material import Material
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.tiempoPreparacion = tiempoPreparacion
        self.ingredientes = ingredientes
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
    def verificarInsumos(self, plato):
        for ingrediente, cantidad_plato in plato.getIngredientes().items():
            if ingrediente.getCantidad() >= cantidad_plato:
                self.setVerificadoInsumos(True)
        return self.isVerificadoInsumos()

    def mostrarIngredientes(self):
        strIngredientes = ""
        for ingrediente in self.ingredientes:
            strIngredientes += f'\n{ingrediente.getNombre()}'
        return strIngredientes

    def detallesPlato(self):
        return f"\n  Nombre: {self.getNombre()}\nPrecio: {self.getPrecio()}\n               Descripcion: {self.getDescripcion()}\n    Tiempo de preparacion: {self.getTiempoPreparacion()}\n    Ingredientes: {self.mostrarIngredientes()}"