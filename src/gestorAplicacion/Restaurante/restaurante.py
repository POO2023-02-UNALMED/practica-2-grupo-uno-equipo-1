from Restaurante.material import *
from datetime import datetime
from Personas import *
from baseDatos.deserializador import Deserializador

class Restaurante():
	
	#Cuenta el tamaño de una lista
	def contadorListado (self, listado):
		contador = 0
		for elemento in listado:
			if (elemento != None):
				contador += 1
		return contador
	
	def __init__(self, listadoMesas=None, listadoEmpleados=None, listadoClientes=None, inventario=None, listadoAspEmpleados=None):
		self.NOMBRE = "Le Quasó"
		self.empleadoDelMes = None
		self.numMesas = 0
		self.numEmpleados = 0
		self.numClientes = 0
		self.pedidos = []
		self.listadoMesas = listadoMesas if listadoMesas is not None else []
		self.listadoEmpleados = listadoEmpleados if listadoEmpleados is not None else []
		self.listadoClientes = listadoClientes if listadoClientes is not None else []
		self.inventario = inventario if inventario is not None else {}
		self.listadoAspEmpleados = listadoAspEmpleados if listadoAspEmpleados is not None else []
		self.numMesas += self.contadorListado(listadoMesas)
		self.numEmpleados += self.contadorListado(listadoEmpleados)
		self.numClientes += self.contadorListado(listadoEmpleados)
		
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
	
	def getInventario (self): 
		return self.inventario
	
	def getPedidos(self):
		return self.pedidos
	
	def getAspEmpleados (self):
		return self.listadoAspEmpleados
	
    #Metodos setter
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
		
    def setMesas(self, mesas):
		self.listadoMesas=mesas
    
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
	def veirificarMenu(self, menu):
		menuVerificado = []
		for plato in menu:
			# Se verifica si cada plato cumple
			if (plato.verificarInsumos(plato)):
				menuVerificado.append(plato)
		return menuVerificado
	
	
	
	#Encontrar reserva, aqui se mira si segun los datos en el pedido hay una reserva
	def encontrarReserva(self, numMesa, nombre):
		mesa = self.encontrarMesa(numMesa)
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
		cocineros = clasificarEmpleados(empleados, "cocinero")
		cocinerosVerificados = []
		tiempoPreparacion = platos[0].getTiempoTotal(platos)
		for empleado in cocineros:
			if (empleado.verificarTiempo(empleado, tiempoPreparacion)):
				cocinerosVerificados.append(empleado)
		return cocinerosVerificados
	
	#Verificar los domiciliarios aptos para entregar el pedido
	def verificarDomiciliarios(self, empleados): 
		domiciliarios = clasificarEmpleados(empleados, "domiciliario")
		domiciliariosVerificados = []
		for empleado in domiciliarios:
			if (empleado.verificarTiempo(empleado)):
				domiciliariosVerificados.append(empleado)
		return domiciliariosVerificados
	
	#Verificar los meseros aptos para entregar
	def verificarMeseros(self, empleados): 
		meseros = clasificarEmpleados(empleados, "mesero")
		meserosVerificados = []
		for empleado in meseros:
			if (empleado.verificarTiempo(empleado)):
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
	imprimirPedidosRestaurante()
		pedidosRestaurante =""
		for(i = 0 i < def getPedidosRestaurante().size() i++)
			pedidosRestaurante+=(i + 1) + ". " + def getPedidosRestaurante().def get(i)
			pedidosRestaurante+="\n-------------------------------------------------------\n"
			
            return pedidosRestaurante
	
	
	
	#Actualizar insumos despues de ya estar verificado el pedido
	def actualizarInsumos(Pedido pedido) 
	    for (Plato plato : pedido.def getPlatos()) 
	        for (Map.Entry<Material, Integer> entrada : plato.def getIngredientes().entrySet()) 
	            Material material = entrada.def getKey()
	            cantidadUtilizada = entrada.def getValue()
	            material.restarCantidad(cantidadUtilizada)
	        
	    
	
	   #Gestion de Pedidos
    def actualizarTiempoEmpleados(Pedido pedido)
    	#Este metodo es  para actualizar el tiempo
    	LocalDate fechaActual = LocalDate.now()
    	dia = pedido.def getCocinero().clasificarDia(fechaActual)
    	for(Pedido pedidoi: def getPedidos()) 
    		if(pedidoi.equals(pedido)) 
    			for(Turno turno : pedido.def getCocinero().def getTurnos())
    				if(turno.def getTipo().toString().equals(dia)) 
    					if(!turno.isCompletado()) 
    						
    						turno.restarTiempo(turno,pedido.def getTiempoTotal())
    					
    					
    				
    		
    	#Llama metodo para cobrar turno
    	
    	pedido.def getCocinero().turnosCompletados(pedido.def getCocinero())
   	 #Si el pedido es de consumo en restaurante se actualiza tiempo a mesero
   	 if(pedido.def getMesero()!=None) 
       	 for(Turno turno :pedido.def getMesero().def getTurnos())
       		if(turno.def getTipo().toString().equals(dia)) 
       		 if(!turno.isCompletado()) 

       			 turno.restarTiempo(turno,Pedido.TIEMPO_MESERO)
       		 
       	 #Llama metodo para cobrar turno
       		

       	pedido.def getMesero().turnosCompletados(pedido.def getMesero()) 
       	
   	 #Si el pedido es de consumo en domicilio se actualiza tiempo a domiciliario
   	 if(pedido.def getDomiciliario()!=None) 
   	 for(Turno turno : pedido.def getDomiciliario().def getTurnos())
   		if(turno.def getTipo().toString().equals(dia)) 
   		 if(!turno.isCobrado()) 
   	
   			 turno.restarTiempo(turno,Pedido.TIEMPO_DOMICILIO)
   		 
   	 #Llama metodo para cobrar turno
   	
   	 pedido.def getDomiciliario().turnosCompletados(pedido.def getDomiciliario())
   	 
	#Buscar un por su nombre y puesto
    buscarEmpleado(nombre, puesto)
    	for(: listadoEmpleados)
    		if((empleado.def getNombre()).equals(nombre) && (empleado.def getPuesto()).equals(puesto))
    
    return empleado
    		
    	
        return  None
    
    //añade un a la lista de empleados
    def contratarEmpleado(novato) 
        self.listadoEmpleados.append(novato)
        a = self.def getNumEmpleados()
        self.setNumEmpleados(a+1)
    
    //Añade el cliente a la lista de clientes
    def afiliarCliente (Cliente nuevoCliente) 
        self.listadoClientes.append(nuevoCliente)
        a = self.def getNumClientes()
        self.setNumClientes(a+1)
    
    //añade la mesa a la lista de mesas
    def comprarMesa (Mesa nuevaMesa) 
        self.listadoMesas.append(nuevaMesa)
        a = self.def getNumMesas()
        self.setNumMesas(a+1)
    
    //elimina la mesa del listado de mesas en base al número
    def eliminarMesa(numeroMesa) 
    	for(Mesa mesa:listadoMesas) 
    		if(mesa.def getNumeroMesa()==numeroMesa) 
    			listadoMesas.remove(mesa)
    
    return
    		
    	
    
    //Metodos gestion de inventario
    
    
    //Añade la cantidad del material suministrado junto a su fecha de vencimiento, en caso de
    //que lo ultimo no coincida se crea una instancia diferente y si no existe la instancia se crea
    def comprarMaterial (Material.Tipo tipo, cantidad, precio, fecha) 
    	//revisa si ya existe el material
        if (self.inventario.containsKey(tipo)) 
        	Material materialComprado = self.inventario.def get(tipo)
        	LocalDate vence = Reserva.deStringaFecha(fecha)
            materialComprado.comprarMaterial(cantidad)
            materialComprado.cambiarPrecioUnitario(precio)
            materialComprado.cambiarFechaVencimiento(vence)
            
            
        
        //no existe por lo que lo crea
        else 
        	LocalDate vence = Reserva.deStringaFecha(fecha)
        	Material nuevoMaterial=new Material(tipo,cantidad,precio,vence)
            inventario.put(tipo, nuevoMaterial)
            nuevoMaterial.cambiarPrecioUnitario(precio)
            nuevoMaterial.cambiarFechaVencimiento(vence)
        
    
    
    //sobrecarga de metodo, hace lo mismo que el de arriba pero sin fecha de vencimiento
    def comprarMaterial (Material.Tipo tipo, cantidad, precio) 
        if (self.inventario.containsKey(tipo)) 
        	Material materialComprado = self.inventario.def get(tipo)
            materialComprado.comprarMaterial(cantidad)
            materialComprado.cambiarPrecioUnitario(precio)
        
        else 
        	Material nuevoMaterial=new Material(tipo,cantidad,precio)
            inventario.put(tipo, nuevoMaterial)
            nuevoMaterial.cambiarPrecioUnitario(precio)
        
    
    //Se encarga de eliminar un material especifico
    def botarMaterial(Material.Tipo tipo,cantidad) 
    	if (self.inventario.containsKey(tipo)) 
    		Material materialEliminado=self.inventario.def get(tipo)
    		if (materialEliminado.def getCantidad()>=cantidad) 
    			materialEliminado.botarMaterial(cantidad)
    		else 
    			operacionInvalida()
    		
    	
    	else 
    		operacionInvalida()
    	
    
  //metodo para decir si una accion no puede ser ejecutada
    operacionInvalida() 
    return "Operacion Inválida"
    
    double calcularValorInventario() 
    	double valorTotal=0
    	for (Material material: inventario.values()) 
    		valorTotal+=material.def getCantidad()*material.def getPrecioUnitario()
    	
        return valorTotal
    
    
    

    #Gestion de Reservas
    def borrarReservasViejas() 
        for (Mesa mesa1 : def getMesas()) 
            mesa1.borrarReservasViejas()
        
        
    //retorna las mesas que son válidas (capacidad y fecha disponible) para la reserva
    listadoMesasValidasParaReserva(Reserva reserva) 
        mesasFiltradas = []
        for (Mesa mesa : listadoMesas) 
            if (mesa.suficienteCapacidad(reserva) && mesa.mesaCompatible(reserva)) 
                mesasFiltradas.append(mesa)
            
        
        return mesasFiltradas
    
    //encuentra una mesa por su numero
    Mesa encontrarMesa(numMesa) 
        Long b = (long) numMesa
        for (Mesa mesa1 : def getMesas()) 
            Long a = (long) mesa1.def getNumeroMesa()
            if (b.equals(a)) 
    
    return mesa1
            
        
        return None
    
    
    
    //Imprime las reservas por confirmar (sin mesa asignada)
    imprimirReservas() 
        r = ""
        List<Reserva> listado = []
        for (Cliente cliente1 : def getClientes()) 
            listado.append(cliente1.def getReserva())
        
        for (Reserva reserva1 : listado) 
            if (reserva1 != None) 
                r += "\n"+reserva1.resumenReserva()+"\n\n+++++++++++++++++++++++++\n"
            
        
        if (r.equals("")) 
            r = "\nNo se han hecho reservas\n"
        
        return r
    
   
	//Imprime las reservas confirmadas (con mesa asignada)
    imprimirReservas2() 
        r = ""
        List<Reserva> listado = []
        for (Mesa mesa1 : def getMesas()) 
            listado.appendAll(mesa1.def getReservas())
        
        for (Reserva reserva1 : listado) 
            if (reserva1 != None) 
                r += "\n"+reserva1.resumenReserva()+"\n\n+++++++++++++++++++++++++\n"
            
        
        if (r.equals("")) 
            r = "\nNo se han confirmado reservas\n"
        
        return r
    
    //dice si el cliente si está guardado en la lista de clientes
    boolean verificarCliente(Long cedula) 
        for (Cliente cliente1 : def getClientes()) 
            if (cedula.equals(cliente1.def getCedula())) 
    
    return false
            
        
        return true
    
    //devuelve el objeto cliente en base a su cédula
    Cliente obtenerCliente(Long cedula) 
        for (Cliente cliente1 : def getClientes()) 
            if (cedula.equals(cliente1.def getCedula())) 
    
    return cliente1
            
        
        return None
    
    //obtiene el cliente en base a la cédula llamando al método obtenerCliente, y le asigna la reserva
    def asignarReservaCliente(Long cedula, nombre, numAsistentes, diaReserva) 
        if (verificarCliente(cedula)) 
            Cliente c1 = new Cliente(nombre, cedula)
            afiliarCliente(c1)
        
        Cliente c1 = obtenerCliente(cedula)
        LocalDate diaReserva2 = Reserva.deStringaFecha(diaReserva)
        c1.setReserva(new Reserva(c1, numAsistentes, diaReserva2))
    
    //retorna el listado de mesas que cumplen para la reserva que tenga asignada ek cliente
    mesasQueCumplen(Long cedulaDuenoReserva) 
        t = ""
        Cliente c1 = obtenerCliente(cedulaDuenoReserva)
        Reserva r1 = c1.def getReserva()
        listado = self.listadoMesasValidasParaReserva(r1)
        for (Mesa mesa1 : listado) 
                t += "\n"+mesa1.resumenMesa()+"\n\n+++++++++++++++++++++++++\n"
        
        if (t.equals("")) 
            t = "\nNo hay mesas válidas para esa reserva\n"
        
        return t
    

    //Si la mesa seleccionada cumple, le asigna la reserva a la mesa
    confirmarReserva(numMesa, Long cedula) 
        Cliente c1 = obtenerCliente(cedula)
        Reserva r1 = c1.def getReserva()
        if (Mesa.verificarNumero(numMesa)) 
            Mesa mesa1 = encontrarMesa(numMesa)
            if (mesa1.suficienteCapacidad(r1)) 
                mesa1.reservarMesa(r1)
                c1.setReserva(None)
    
    return "Reserva asignada a la mesa #"+numMesa
            
            else 
    
    return "La mesa seleccionada no tiene la capacidad suficiente, vuelva a intentarlo"
            
        
        else 

return "No existe una mesa con ese número, por favor vuelva a intentarlo"
        
    
	


