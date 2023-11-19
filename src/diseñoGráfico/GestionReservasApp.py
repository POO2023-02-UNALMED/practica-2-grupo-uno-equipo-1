from tkinter import *
from diseñoGráfico.FieldFrame import FieldFrame
from gestorAplicacion.Restaurante.reserva import Reserva

class GestionReservasApp:
    """
    Aqui se plantea toda la funcionalidad de gestion de reservas
    """
    def __init__(self, framePadre, restaurante):
        self.row_height = 200
        self.col_width = 200
        self.frames_temporales = []
        self.framePadre = framePadre
        self.restaurante = restaurante
        self.funcionalidad_gestionReservas = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionReservas.grid(row=0, column=0, sticky="nsew")
        self.options_frame = Frame(self.funcionalidad_gestionReservas, bg='#c3c3c3', width=100, height=500)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        self.options_frame.pack_propagate(False)
        self.main_frame = Frame(self.funcionalidad_gestionReservas, highlightbackground='black', highlightthickness=2, width=500, height=400)

        # Crear botones de selección de opción
        self.btn_home_page = Button(self.options_frame, text="Inicio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_home_page, self.home_indicate))
        self.btn_home_page.grid(row=0, column=0, padx=0, pady=30)

        self.btn_consultar_reservas_NC = Button(self.options_frame, text="reservas sin\nconfirmar", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_frame_RNC, self.indicate_reservas_NC))
        self.btn_consultar_reservas_NC.grid(row=1, column=0, padx=0, pady=30)

        self.btn_consultar_reservas_C = Button(self.options_frame, text="reservas\nconfirmadas", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_RC, self.indicate_RESERVAS_C))
        self.btn_consultar_reservas_C.grid(row=2, column=0, padx=0, pady=30)

        btn_anadir_reservas = Button(self.options_frame, text="añadir\n  reservas", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_ANADIR_R, self.indicate_anadir_reservas))
        btn_anadir_reservas.grid(row=3, column=0, padx=0, pady=30)

        btn_cancelar_reservas = Button(self.options_frame, text="cancelar\n  reservas", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_cancelar_R, self.indicate_cancelar_reservas))
        btn_cancelar_reservas.grid(row=3, column=0, padx=0, pady=30)

        btn_asignar_mesas = Button(self.options_frame, text="añadir\nreservas", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_confirmar_R, self.indicate_confirmar))
        btn_asignar_mesas.grid(row=3, column=0, padx=0, pady=30)
        # Crear indicadores de opción seleccionada
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=20, y=30, width=5, height=40, )

        self.indicate_reservas_NC = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_reservas_NC.place(x=20, y=135, width=5, height=40, )
        
        self.indicate_RESERVAS_C = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_RESERVAS_C.place(x=20, y=255, width=5, height=40, )
        
        self.indicate_anadir_reservas = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_anadir_reservas.place(x=20, y=375, width=5, height=40, )

        self.indicate_cancelar_reservas = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_cancelar_reservas.place(x=20, y=375, width=5, height=40, )

        self.indicate_confirmar = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_confirmar.place(x=20, y=375, width=5, height=40, )

        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_page(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la gestion de reservas", font=("Bold", 15)).place(x=150, y=30)
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_RNC(self):
        self.frame_RNC = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_RNC, text="Reservas sin\nmesa asignada", font=("Bold", 15)).place(x=150, y=30)
        self.frame_RNC.grid(pady=5, padx=5)
        self.frame_RNC.pack_propagate(False)

    def function_frame_RC(self):
        self.frame_RC = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_RC, text="Reservas", font=("Bold", 15)).place(x=150, y=30)
        self.frame_RC.grid(pady=5, padx=5)
        self.frame_RC.pack_propagate(False)

    def function_frame_ANADIR_R(self):
        # Definir frame reservas
        self.frame_ANADIR_R = Frame(self.main_frame, width=500, height=400)
        # Frame de interacción
        self.frame_AR = Frame(self.frame_ANADIR_R, width=500, height=400)
        self.V_AR = FieldFrame(self.frame_AR, "información del reservista", ["cedula", "nombre", "numero de asistentes", "dia de la reserva"], "Ingresa la información", ["Ej: 1022142545", "Solo si reservista no está registrado", "", "En formato dia-mes-año"], [True, True, True, True], self.anadirR)
        self.V_AR.grid(row = 0, column=0, padx=10, pady=10)
        self.frame_ANADIR_R.grid(pady=5, padx=5)
        self.frame_ANADIR_R.pack_propagate(False)

    def function_frame_cancelar_R(self):
        self.frame_ANADIR_R = Frame(self.main_frame, width=500, height=400)
        # Frame de interacción
        self.frame_AR = Frame(self.frame_ANADIR_R, width=500, height=400)
        self.V_AR = FieldFrame(self.frame_AR, "información del reservista", ["cedula"], "Ingresa la información", ["Ej: 1022142545"], [True], self.cancelarR)
        self.V_AR.grid(row = 0, column=0, padx=10, pady=10)
        self.frame_ANADIR_R.grid(pady=5, padx=5)
        self.frame_ANADIR_R.pack_propagate(False)

    def function_frame_confirmar_R(self):
        self.confirmar_R = Frame(self.main_frame, width=500, height=400)
        # Frame de interacción
        self.frame_re = Frame(self.confirmar_R, width=500, height=400)
        self.conf_R = FieldFrame(self.frame_re, "Información del reservista", ["cedula", "numero de mesa"], "Ingresa la información", [], [True, True], self.confirmarR)
        self.conf_R.grid(row = 0, column=0, padx=10, pady=10)
        self.confirmar_R.grid(pady=5, padx=5)
        self.confirmar_R.pack_propagate(False)
        
    def anadirR(self, valores):


    elif tipo_pedido == "domicilio":
        # Crear un nuevo Frame para la selección del cocinero
        self.anadirRFrame = Frame(self.frame_ANADIR_R, width=500, height=400) 

        # Crear el Frame de resultados para el cocinero
        self.frameResultadosCocinero = FieldFrame( self.anadirRFrame, "Cocinero", ["cocinero"], "Ingrese el nombre del cocinero", [], [True], self.cancelarR)
        
        # Colocar el Frame de resultados en el grid
        self.frameResultadosCocinero.grid(padx=10, pady=10)

        # Crear un Canvas para mostrar los cocineros
        self.canvascocineros = Canvas( self.anadirRFrame)
        # Colocar el Canvas en el grid
        self.canvascocineros.grid(row=1, column=0, padx=10, pady=10)
        self.frames_temporales.append(self.canvascocineros)

        # Colocar el Frame de selección del cocinero en el grid
        self.anadirRFrame.grid(row=0, column=0)
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



    def cancelarR(self, valores):
        self.anadirRFrame.destroy()
        self.pedido["cocinero"] = valores["cocinero"]
        self.domiciliarios = [
            {"nombre": "Juliana", "identificacion": "123456789L"},
            {"nombre": "Ana", "identificacion": "123456789L"},
            {"nombre": "Jhon", "identificacion": "123456789L"},
            {"nombre": "Andres", "identificacion": "123456789L"},
        ]
        self.framecancelarR = Frame(self.frame_ANADIR_R, width=500, height=400)

        self.frameResultadosDomiciliario = FieldFrame( self.framecancelarR, "Domiciliario", ["domiciliario"], "ingrese el nombre del domiciliario", [], [True], self.crearPedido)
        self.frameResultadosDomiciliario.grid(padx=10, pady=10)

        self.canvasdomiciliarios = Canvas(self.framecancelarR)
        self.canvasdomiciliarios.grid(row=1, column=0, padx=10, pady=10)
        self.frames_temporales.append(self.canvasdomiciliarios)

        self.framecancelarR.grid(row=0, column=0)

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


    def confirmarR(self, valores):
        self.anadirRFrame.destroy()
        self.pedido["cocinero"] = valores["cocinero"]
        self.meseros = [
              {"nombre": "Karen", "identificacion": "123456789L"},
                {"nombre": "Daniel", "identificacion": "123456789L"},
                {"nombre": "Dario", "identificacion": "123456789L"},
                {"nombre": "Duvan", "identificacion": "123456789L"},
        ]
        self.frameconfirmarR = Frame(self.frame_ANADIR_R, width=500, height=400)

        self.frameResultadosMesero = FieldFrame(self.frameconfirmarR, "Mesero", ["mesero"], "ingrese el nombre del mesero", [], [True], self.detectarReserva)
        self.frameResultadosMesero.grid(padx=10, pady=10)

        self.canvasmeseros = Canvas(self.frameconfirmarR)
        self.canvasmeseros.grid(row=1, column=0, padx=10, pady=10)
        self.frames_temporales.append(self.canvasmeseros)

        self.frameconfirmarR.grid(row=0, column=0)

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
        self.frameconfirmarR.destroy()
        self.pedido["mesero"] = valores["mesero"]
        self.frameDetectarReserva = Frame(self.frame_ANADIR_R, width=500, height=400)
        self.frameResultadosReserva = FieldFrame(self.frameDetectarReserva, "Datos de reserva", ["mesa", "dueño reserva"], "ingrese los datos de la reserva", [], [True, True], self.crearPedido)
        self.frameResultadosReserva.grid(padx=10, pady=10)
        self.frameDetectarReserva.grid(padx=10, pady=10)
    
    def crearPedido(self, valores, restaurante):
        self.frame_AR.destroy()
        self.frameDetectarReserva.destroy()
        if self.pedido["tipo_pedido"] == "domicilio":
            self.framecancelarR.destroy()
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
        self.indicate_anadir_reservas.config(bg='#c3c3c3')

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