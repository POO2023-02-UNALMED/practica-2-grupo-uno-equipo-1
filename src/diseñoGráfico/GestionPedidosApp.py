from tkinter import *
from diseñoGráfico.FieldFrame import FieldFrame
from gestorAplicacion.Restaurante.pedido import Pedido

class GestionPedidosApp:
    """
    Aqui se plantea toda la funcionalidad de gestion de pedidos
    """
    plato_seleccionado=False
    def __init__(self, framePadre, menu, imagenes_recetas, restaurante):
        self.row_height = 200
        self.col_width = 200
        self.restaurante = restaurante
        self.menu = menu
        self.imagenes_recetas = imagenes_recetas
        # self.rows = 2

        self.frames_temporales = []
        # self.root.geometry('700x650')
        # self.root.title('Gestión de Pedidos')
        # self.root.pack_propagate(False)
        self.framePadre = framePadre
        self.funcionalidad_gestionPedidos = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionPedidos.grid(row=0, column=0, sticky="nsew")
        self.options_frame = Frame(self.funcionalidad_gestionPedidos, bg='#c3c3c3', width=100, height=500)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        self.options_frame.pack_propagate(False)

        self.platos_seleccionados = []
        self.platos_temp = []
        self.pedido = {}

        # Crear una lista de platos (nombre, imagen)
        self.platos = []

        for i, plato in enumerate(menu):
            plato_dict = {
                "nombre": plato.getNombre(),
                "precio": plato.getPrecio(),
                "descripcion": plato.getDescripcion(),
                "tiempo de preparacion": plato.getTiempoPreparacion(),
                "ingredientes": plato.getIngredientes(),
                "imagen": imagenes_recetas[i]
            }
            self.platos.append(plato_dict)

        self.main_frame = Frame(self.funcionalidad_gestionPedidos,
                                highlightbackground='black',
                                highlightthickness=2,
                                width=500,
                                height=400)

        # Crear botones de selección de opción
        self.btn_home_page = Button(self.options_frame, text="Inicio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_home_page, self.home_indicate))
        self.btn_home_page.grid(row=0, column=0, padx=0, pady=30)

        self.btn_consultar_domicilio = Button(self.options_frame, text="pedidos\n domicilio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_frame_domicilio, self.indicate_pedidos_dm))
        self.btn_consultar_domicilio.grid(row=1, column=0, padx=0, pady=30)

        self.btn_consultar_restaurante = Button(self.options_frame, text="pedidos\n     restaurante", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_restaurante, self.indicate_pedidos_rs))
        self.btn_consultar_restaurante.grid(row=2, column=0, padx=0, pady=30)

        btn_anadir_pedidos = Button(self.options_frame, text="añadir\n  pedidos", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_pedidos, self.indicate_anadir_pedidos))
        btn_anadir_pedidos.grid(row=3, column=0, padx=0, pady=30)

        # Crear indicadores de opción seleccionada
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=20, y=30, width=5, height=40, )

        self.indicate_pedidos_dm = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_pedidos_dm.place(x=20, y=135, width=5, height=40, )
        
        self.indicate_pedidos_rs = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_pedidos_rs.place(x=20, y=255, width=5, height=40, )
        
        self.indicate_anadir_pedidos = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_anadir_pedidos.place(x=20, y=375, width=5, height=40, )


        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_page(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la gestion de pedidos", font=("Bold", 15)).place(x=150, y=30)
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_domicilio(self):
        self.frame_domicilio = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_domicilio, text="Domicilios", font=("Bold", 15)).place(x=150, y=30)
        self.frame_domicilio.grid(pady=5, padx=5)
        self.frame_domicilio.pack_propagate(False)

    def function_frame_restaurante(self):
        self.frame_restaurante = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_restaurante, text="Restaurante", font=("Bold", 15)).place(x=150, y=30)
        self.frame_restaurante.grid(pady=5, padx=5)
        self.frame_restaurante.pack_propagate(False)

    def function_frame_pedidos(self):
        # Definir frame pedidos
        self.frame_pedidos = Frame(self.main_frame, width=500, height=400)
        # Título de frame pedidos
        # self.titulo_pedidos = Label(self.frame_pedidos, text="Pedidos", font=("Bold", 15)).place(x=150, y=30)

        # Frame de interacción
        self.frameSeleccionPlatos = Frame(self.frame_pedidos, width=500, height=400)
        self.busquedadPlatos = FieldFrame(self.frameSeleccionPlatos, "platos deseados y tipo de pedido", ["platos", "tipo pedido"], "Ingresa lo platos deseados y tipo de pedido", ["presiona los platos que desees"], [False, True], self.seleccionarCocinero)
        self.busquedadPlatos.grid(row = 0, column=0, padx=10, pady=10)

        # Crear un Canvas para la cuadrícula dentro del Frame principal
        self.canvas = Canvas(self.frameSeleccionPlatos)
        self.canvas.grid(row = 1, column=0, padx=10, pady=10)

        self.frames_temporales.append(self.canvas)

        # Ubicación del frame seleccionPlatos dentro de frame_pedidos mediante grid
        self.frameSeleccionPlatos.grid(row=0, column=0)

        # Configurar la cuadrícula
        cols=2
        rows = len(self.platos) // cols+1

        # Dentro del bucle para mostrar platos en la cuadrícula
        for i, plato in enumerate(self.platos):
            row = i // cols
            col = i % cols

            # Crear un Frame para cada plato dentro del Canvas
            frame = Frame(self.canvas, width=self.col_width, height=self.row_height, bd=2, relief=RIDGE)
            frame.grid(row=row, column=col, padx=5, pady=5)

            # Cargar la imagen (reemplaza 'ruta_a_tu_imagen' con la ruta real de tus imágenes)
            # imagen_path = "ruta_a_tu_imagen"  # Reemplazar con la ruta correcta
            imagen = plato["imagen"]

            # Mostrar imagen del plato (esto podría ser un botón en lugar de una etiqueta)
            boton_plato = Button(frame, image=imagen, command=lambda i=i: self.toggle_seleccion(i))
            boton_plato.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # sticky="w" alinea a la izquierda

            # Mostrar nombre del plato
            nombre_label = Label(frame, text=plato["nombre"])
            nombre_label.grid(row=0, column=1, padx=5, pady=1)

            # Mostrar precio del plato
            precio_label = Label(frame, text=f"Precio: {plato['precio']}")
            precio_label.grid(row=1, column=1, padx=5, pady=1)


        # Ubicación frame pedidos
        self.frame_pedidos.grid(pady=5, padx=5)
        self.frame_pedidos.pack_propagate(False)
    
    
    def toggle_seleccion(self, indice):
        print(indice)
        if self.platos_seleccionados.count(indice) == 0:
            # Si no está seleccionado, agregarlo a la lista
            self.platos_seleccionados.append(indice)
            GestionPedidosApp.plato_seleccionado=True
        elif indice in self.platos_seleccionados:
            # Si ya está seleccionado, quitarlo de la lista
            self.platos_seleccionados.remove(indice)
        
    def seleccionarCocinero(self, valores):

        # Almacenar los platos seleccionados y el tipo de pedido en el objeto de pedido
        print(self.platos_temp)

        # Obtener el tipo de pedido
        tipo_pedido = valores["tipo pedido"]
        
        self.pedido["platos"] = self.platos_temp
        self.pedido["tipo_pedido"] = tipo_pedido

        # Se guardan los platos
        print(self.pedido)

        # Destruir el canvas existente
        self.canvas.destroy()
        self.frameSeleccionPlatos.destroy()

        # Filtrar los platos seleccionados
        for i in self.platos_seleccionados:
            self.platos_temp.append(self.menu[i-1])

        # no se esta usando 
        # # Obtener los platos seleccionados
        # index_platos_escogidos = valores["platos"].split()


        #Seleccionar cocineros
        cocineros = self.restaurante.verificarCocinero(self.restaurante.getEmpleados(), self.platos_temp)

        print(cocineros)

        # Lista de cocineros (corregir la clave 'idenrificacion' a 'identificacion')
        self.cocineros = []

        for i, cocinero in enumerate(cocineros):
            cocinero_dict= {
                "nombre": cocinero.getNombre(),
                "identificacion": cocinero.getCedula(),
                "puesto": cocinero.getPuesto(),
            }
            self.cocineros.append(cocinero_dict)
        
        # Según el tipo de pedido, mostrar diferentes frames y resultados
        if tipo_pedido == "restaurante":
            # Crear un nuevo Frame para la selección del cocinero
            self.seleccionarCocineroFrame = Frame(self.frame_pedidos, width=500, height=400) 

            # Crear el Frame de resultados para el cocinero
            self.frameResultadosCocinero = FieldFrame( self.seleccionarCocineroFrame, "Cocinero", ["cocinero"], "Ingrese el nombre del cocinero", [], [True], self.seleccionarMesero)
            
            # Colocar el Frame de resultados en el grid
            self.frameResultadosCocinero.grid(padx=10, pady=10)
            
            # Colocar el Frame de resultados en el grid
            self.frameResultadosCocinero.grid(padx=10, pady=10)

            # Crear un Canvas para mostrar los cocineros
            self.canvascocineros = Canvas( self.seleccionarCocineroFrame)
            self.frames_temporales.append(self.canvascocineros)
            
            # Colocar el Canvas en el grid
            self.canvascocineros.grid(row=1, column=0, padx=10, pady=10)

            # Colocar el Frame de selección del cocinero en el grid
            self.seleccionarCocineroFrame.grid(row=0, column=0)
            print("valores", valores)

            cols=2
            rows = len(self.platos) // cols+1

            for i, cocinero in enumerate(self.cocineros):
                row = i // cols
                col = i % cols

                # Crear un Frame para cada cocinero dentro del Canvas
                frame = Frame(self.canvascocineros, width=self.col_width, height=self.row_height, bd=2, relief=RIDGE)
                frame.grid(row=row, column=col, padx=5, pady=5)
                
                # Mostrar nombre del cocinero
                nombre_label = Label(frame, text=cocinero["nombre"])
                nombre_label.pack(pady=5)

                # Mostrar identificación del cocinero
                identificacion_label = Label(frame, text=f"Identificación: {cocinero['identificacion']}")
                identificacion_label.pack(pady=5)

        elif tipo_pedido == "domicilio":
            # Crear un nuevo Frame para la selección del cocinero
            self.seleccionarCocineroFrame = Frame(self.frame_pedidos, width=500, height=400) 

            # Crear el Frame de resultados para el cocinero
            self.frameResultadosCocinero = FieldFrame( self.seleccionarCocineroFrame, "Cocinero", ["cocinero"], "Ingrese el nombre del cocinero", [], [True], self.seleccionarDomiciliario)
            
            # Colocar el Frame de resultados en el grid
            self.frameResultadosCocinero.grid(padx=10, pady=10)

            # Crear un Canvas para mostrar los cocineros
            self.canvascocineros = Canvas( self.seleccionarCocineroFrame)
            # Colocar el Canvas en el grid
            self.canvascocineros.grid(row=1, column=0, padx=10, pady=10)
            self.frames_temporales.append(self.canvascocineros)

            # Colocar el Frame de selección del cocinero en el grid
            self.seleccionarCocineroFrame.grid(row=0, column=0)
            print("valores", valores)

            # Configurar la cuadrícula
            cols=2
            rows = len(self.platos) // cols+1

            for i, cocinero in enumerate(self.cocineros):
                row = i // cols
                col = i % cols

                # Crear un Frame para cada cocinero dentro del Canvas
                frame = Frame(self.canvascocineros, width=self.col_width, height=self.row_height, bd=2, relief=RIDGE)
                frame.grid(row=row, column=col, padx=5, pady=5)
                
                # Mostrar nombre del cocinero
                nombre_label = Label(frame, text=cocinero["nombre"])
                nombre_label.pack(pady=5)

                # Mostrar identificación del cocinero
                identificacion_label = Label(frame, text=f"Identificación: {cocinero['identificacion']}")
                identificacion_label.pack(pady=5)


    
    def seleccionarDomiciliario(self, valores):
        self.seleccionarCocineroFrame.destroy()
        self.pedido["cocinero"] = valores["cocinero"]
        self.domiciliarios = [
            {"nombre": "Juliana", "identificacion": "123456789L"},
            {"nombre": "Ana", "identificacion": "123456789L"},
            {"nombre": "Jhon", "identificacion": "123456789L"},
            {"nombre": "Andres", "identificacion": "123456789L"},
        ]
        self.frameSeleccionarDomiciliario = Frame(self.frame_pedidos, width=500, height=400)

        self.frameResultadosDomiciliario = FieldFrame( self.frameSeleccionarDomiciliario, "Domiciliario", ["domiciliario"], "ingrese el nombre del domiciliario", [], [True], self.crearPedido)
        self.frameResultadosDomiciliario.grid(padx=10, pady=10)

        self.canvasdomiciliarios = Canvas(self.frameSeleccionarDomiciliario)
        self.canvasdomiciliarios.grid(row=1, column=0, padx=10, pady=10)
        self.frames_temporales.append(self.canvasdomiciliarios)

        self.frameSeleccionarDomiciliario.grid(row=0, column=0)

        cols=2
        rows = len(self.platos) // cols+1
        
        for i, domiciliario in enumerate(self.domiciliarios):
                row = i // cols
                col = i % cols

                # Crear un Frame para cada cocinero dentro del Canvas
                frame = Frame(self.canvasdomiciliarios, width=self.col_width, height=self.row_height, bd=2, relief=RIDGE)
                frame.grid(row=row, column=col, padx=5, pady=5)
                
                # Mostrar nombre del cocinero
                nombre_label = Label(frame, text=domiciliario["nombre"])
                nombre_label.pack(pady=5)

                # Mostrar identificación del cocinero
                identificacion_label = Label(frame, text=f"Identificación: {domiciliario['identificacion']}")
                identificacion_label.pack(pady=5)


    def seleccionarMesero(self, valores):
        self.seleccionarCocineroFrame.destroy()
        self.pedido["cocinero"] = valores["cocinero"]
        self.meseros = [
              {"nombre": "Karen", "identificacion": "123456789L"},
                {"nombre": "Daniel", "identificacion": "123456789L"},
                {"nombre": "Dario", "identificacion": "123456789L"},
                {"nombre": "Duvan", "identificacion": "123456789L"},
        ]
        self.frameSeleccionarMesero = Frame(self.frame_pedidos, width=500, height=400)

        self.frameResultadosMesero = FieldFrame(self.frameSeleccionarMesero, "Mesero", ["mesero"], "ingrese el nombre del mesero", [], [True], self.detectarReserva)
        self.frameResultadosMesero.grid(padx=10, pady=10)

        self.canvasmeseros = Canvas(self.frameSeleccionarMesero)
        self.canvasmeseros.grid(row=1, column=0, padx=10, pady=10)
        self.frames_temporales.append(self.canvasmeseros)

        self.frameSeleccionarMesero.grid(row=0, column=0)

        # Configurar la cuadrícula
        cols=2
        rows = len(self.platos) // cols+1

        for i, mesero in enumerate(self.meseros):
                row = i // cols
                col = i % cols

                # Crear un Frame para cada cocinero dentro del Canvas
                frame = Frame(self.canvasmeseros, width=self.col_width, height=self.row_height, bd=2, relief=RIDGE)
                frame.grid(row=row, column=col, padx=5, pady=5)
                
                # Mostrar nombre del cocinero
                nombre_label = Label(frame, text=mesero["nombre"])
                nombre_label.pack(pady=5)

                # Mostrar identificación del cocinero
                identificacion_label = Label(frame, text=f"Identificación: {mesero['identificacion']}")
                identificacion_label.pack(pady=5)
                
    def detectarReserva(self, valores):
        print("ENTRA A RESERVA")
        self.frameSeleccionarMesero.destroy()
        self.pedido["mesero"] = valores["mesero"]
        self.frameDetectarReserva = Frame(self.frame_pedidos, width=500, height=400)
        self.frameResultadosReserva = FieldFrame(self.frameDetectarReserva, "Datos de reserva", ["mesa", "dueño reserva"], "ingrese los datos de la reserva", [], [True, True], self.crearPedido)
        self.frameResultadosReserva.grid(padx=10, pady=10)
        self.frameDetectarReserva.grid(padx=10, pady=10)
    
    def crearPedido(self, valores, restaurante):
        self.frameSeleccionPlatos.destroy()
        self.frameDetectarReserva.destroy()
        if self.pedido["tipo_pedido"] == "domicilio":
            self.frameSeleccionarDomiciliario.destroy()
            self.pedido["domiciliario"] = valores["domiciliario"]
        if self.pedido["tipo_pedido"] == 'restaurante':
            numMesa = valores["mesa"]
            dueñoReserva = valores["dueño reserva"]
            reserva = restaurante.encontrarReserva(numMesa, dueñoReserva)
            mesaTemporal = restaurante.encontrarMesa(numMesa)
            if reserva == None:
                pedido1 = Pedido(mesaTemporal, self.pedido["tipo_pedido"], self.pedido["cocinero"], self.pedido["mesero"], self.pedido["platosTemp"], restaurante)
                if(not Pedido.verificarPedido(restaurante, pedido1) == None):
                      Pedido.verificarPedido(restaurante, pedido1)
            if reserva != None:
                  nombre1 = reserva.getDuenoReserva().getNombre()
                  pedido1 = Pedido(reserva.getMesa, self.pedido["tipo_pedido"], self.pedido["cocinero"], self.pedido["mesero"], self.pedido["platosTemp"], restaurante, reserva)				      
                  pedido1.setVerificado(True)
                  Pedido.actualizarInventario(restaurante, pedido1)
        self.delete_frames()

    # def delete_frames(self):
    #     widgets = self.main_frame.winfo_children()
    #     # Recorrer y destruir todos los frames temporales
    #     for widget in widgets:
    #         if widget.winfo_children():
    #             # Si el widget tiene hijos, también eliminar esos hijos
    #             child_widgets = widget.winfo_children()
    #             for child_widget in child_widgets:
    #                 child_widget.destroy()


    def delete_pages(self):
        """
        Esta se hace para borrar los frames actuales 
        y evitar que se superpongan los frames,
        para que solo se muestre el frame indicado
        dentro de la funcionalidad
        """
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def hide_indicators(self):
        self.home_indicate.config(bg='#c3c3c3')
        self.indicate_pedidos_dm.config(bg='#c3c3c3')
        self.indicate_pedidos_rs.config(bg='#c3c3c3')
        self.indicate_anadir_pedidos.config(bg='#c3c3c3')

    def indicador(self, pagina, lb):
        """
        hide_indicatros para ocultar indicadores,
        se configura para que se muestre el de la que
        se selecciona, se elimina las paginas y se
        muestra la pagina seleccionada
        """
        self.hide_indicators()
        lb.config(bg='#158aff')
        self.delete_pages()
        pagina()