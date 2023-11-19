from tkinter import Frame, Button, Label

class GestionFinancieraApp:
    """
    Aqui se plantea toda la funcionalidad de gestion Financiera
    """
    def __init__(self, framePadre, menu, imagenes_recetas):
        self.row_height = 200
        self.col_width = 200
        # self.rows = 2
        self.material_seleccionado=False  #colocar los materiales de inventario, para asi calcular cuanto se gasto de el

        self.frames_temporales = []
        self.framePadre = framePadre
        self.funcionalidad_gestionFinanciera = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionFinanciera.grid(row=0, column=0, sticky="nsew")
        self.options_frame = Frame(self.funcionalidad_gestionFinanciera, bg='#c3c3c3', width=100, height=500)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        self.options_frame.pack_propagate(False)


        # Crear una lista de platos (nombre, imagen)
        self.material = []

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

        self.main_frame = Frame(self.funcionalidad_gestionFinanciera,
                                highlightbackground='black',
                                highlightthickness=2,
                                width=500,
                                height=400)

        # Crear botones de selección de opción
        self.btn_home_page = Button(self.options_frame, text="Inicio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_home_page, self.home_indicate))
        self.btn_home_page.grid(row=0, column=0, padx=0, pady=30)

        self.btn_consultar_presupuesto = Button(self.options_frame, text="Presupuesto", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_frame_presupuesto, self.indicate_consultarPresupuesto))
        self.btn_consultar_presupuesto.grid(row=1, column=0, padx=0, pady=30)

        self.btn_consultar_gananciasBrutas = Button(self.options_frame, text="Ganancias\n  Brutas", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gananciasBrutas, self.indicate_consultarGB))
        self.btn_consultar_gananciasBrutas.grid(row=2, column=0, padx=0, pady=30)

        self.btn_consultar_gananciasNetas = Button(self.options_frame, text="Ganancias\n  Netas", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gananciasNetas, self.indicate_consultarGN))
        self.btn_consultar_gananciasNetas.grid(row=3, column=0, padx=0, pady=30)

        self.btn_consultar_gastosMateriales = Button(self.options_frame, text="Gastos\n  Inventario", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gastosMateriales, self.indicate_consultarGastosMateriales))
        self.btn_consultar_gastosMateriales.grid(row=4, column=0, padx=0, pady=30)

        self.btn_consultar_pagosEmpleados = Button(self.options_frame, text="Pagos\n  Empleados", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_pagosEmpleados, self.indicate_consultarPagosEmpleados))
        self.btn_consultar_pagosEmpleados.grid(row=6, column=0, padx=0, pady=30)

        btn_seleccionar_MaterialEspecifico = Button(self.options_frame, text="Gasto\n  Material Especifico", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_gastosMaterialesEspecificos, self.indicate_seleccionarMaterialEsp))
        btn_seleccionar_MaterialEspecifico.grid(row=3, column=0, padx=0, pady=30)

        # Crear indicadores de opción seleccionada
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=20, y=30, width=5, height=40, )

        self.indicate_consultarPresupuesto = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarPresupuesto.place(x=20, y=135, width=5, height=40, )
        
        self.indicate_consultarGB = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGB.place(x=20, y=255, width=5, height=40, )

        self.indicate_consultarGN = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGN.place(x=20, y=375, width=5, height=40, )

        self.indicate_consultarGastosMateriales = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGastosMateriales.place(x=20, y=435, width=5, height=40, )

        self.indicate_consultarPagosEmpleados = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarPagosEmpleados.place(x=20, y=555, width=5, height=40, )
        
        self.indicate_seleccionarMaterialEsp = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_seleccionarMaterialEsp.place(x=20, y=675, width=5, height=40, )


        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_page(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la gestion de Financiera", font=("Bold", 15)).place(x=150, y=30)
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_presupuesto(self):
        self.frame_presupuesto = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_presupuesto, text="Presupuesto", font=("Bold", 15)).place(x=150, y=30)
        self.frame_presupuesto.grid(pady=5, padx=5)
        self.frame_presupuesto.pack_propagate(False)

    def function_frame_gananciasBrutas(self):
        self.frame_gananciasBrutas = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_gananciasBrutas, text="Ganancias Brutas", font=("Bold", 15)).place(x=150, y=30)
        self.frame_gananciasBrutas.grid(pady=5, padx=5)
        self.frame_gananciasBrutas.pack_propagate(False)

    def function_frame_gananciasNetas(self):
        self.frame_gananciasNetas = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_gananciasNetas, text="Ganancias Netas", font=("Bold", 15)).place(x=150, y=30)
        self.frame_gananciasNetas.grid(pady=5, padx=5)
        self.frame_gananciasNetas.pack_propagate(False)

    def function_frame_gastosMateriales(self):
        self.frame_gastosMateriales = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_gastosMateriales, text="Gastos Inventario", font=("Bold", 15)).place(x=150, y=30)
        self.frame_gastosMateriales.grid(pady=5, padx=5)
        self.frame_gastosMateriales.pack_propagate(False)

    def function_frame_pagosEmpleados(self):
        self.frame_pagosEmpleados = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_pagosEmpleados, text="Pagos Empleados", font=("Bold", 15)).place(x=150, y=30)
        self.frame_pagosEmpleados.grid(pady=5, padx=5)
        self.frame_pagosEmpleados.pack_propagate(False)

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