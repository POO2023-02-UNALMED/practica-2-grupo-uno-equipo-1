from tkinter import *
from diseñoGráfico.FieldFrame import FieldFrame
from gestorAplicacion.Restaurante.restaurante import Restaurante

class GestionInventarioApp:
    """
    Aqui se plantea la funcionalidad de gestion de inventario
    """
    def __init__(self,framePadre,imagenes_ingredientes,restaurante):
        self.row_height = 300
        self.col_width = 300
        self.restaurante=restaurante
        self.imagenes_ingredientes=imagenes_ingredientes

        self.frames_temporales=[]
        self.framePadre=framePadre
        self.funcionalidad_gestionInv = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionInv.grid(row=0, column=0, sticky="nsew")
        self.options_frame = Frame(self.funcionalidad_gestionInv, bg='#c3c3c3', width=120, height=500)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        self.options_frame.pack_propagate(False)

        self.main_frame = Frame(self.funcionalidad_gestionInv,
                                highlightbackground='black',
                                highlightthickness=2,
                                width=500,
                                height=400)
        #Botones frame
        self.btn_home_page = Button(self.options_frame, text="Inicio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_home_page, self.home_indicate))
        self.btn_home_page.grid(row=0, column=0, padx=0, pady=30)

        self.btn_consultar_inventario = Button(self.options_frame, text="Consultar\n Inventario", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_frame_consultar_inventario, self.indicate_consultar_inventario))
        self.btn_consultar_inventario.grid(row=1, column=0, padx=0, pady=30)

        self.btn_comprar_mat = Button(self.options_frame, text="Comprar\n Materiales", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_comprar_mat, self.indicate_comprar_mat))
        self.btn_comprar_mat.grid(row=2, column=0, padx=0, pady=30)

        self.btn_desechar_mat = Button(self.options_frame, text="Desechar\n Materiales", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_desechar_mat, self.indicate_desechar_mat))
        self.btn_desechar_mat.grid(row=3, column=0, padx=0, pady=30)

        #Indicadores de los botones
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=5, y=30, width=5, height=40, )

        self.indicate_consultar_inventario = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultar_inventario.place(x=5, y=135, width=5, height=40, )

        self.indicate_comprar_mat = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_comprar_mat.place(x=5, y=255, width=5, height=40, )

        self.indicate_desechar_mat = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_desechar_mat.place(x=5, y=375, width=5, height=40, )


        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_page(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la gestion de Inventario", font=("Bold", 15)).place(x=150, y=30)
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_consultar_inventario(self):
        self.frame_inventario = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_inventario, text="Inventario", font=("Bold", 15)).place(x=150, y=30)
        self.frame_inventario.grid(pady=5, padx=5)
        self.frame_inventario.pack_propagate(False)

    def function_frame_comprar_mat(self):
        self.frame_comprar = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_comprar, text="Comprar materiales", font=("Bold", 15)).place(x=150, y=30)
        self.frame_comprar.grid(pady=5, padx=5)
        self.frame_comprar.pack_propagate(False)

    def function_frame_desechar_mat(self):
        # Definir frame pedidos
        self.frame_desechar_mat = Frame(self.main_frame, width=500, height=400)
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
        self.indicate_consultar_inventario.config(bg='#c3c3c3')
        self.indicate_comprar_mat.config(bg='#c3c3c3')
        self.indicate_desechar_mat.config(bg='#c3c3c3')

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