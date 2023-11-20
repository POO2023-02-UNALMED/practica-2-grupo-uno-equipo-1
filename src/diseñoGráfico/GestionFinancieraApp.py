from tkinter import *
from diseñoGráfico.FieldFrame import FieldFrame
from gestorAplicacion.Restaurante.financia import Financia
from gestorAplicacion.Restaurante.material import Material


class GestionFinancieraApp:
    """
    Aqui se plantea toda la funcionalidad de gestion Financiera
    """
    def __init__(self, framePadre, restaurante):
        self.row_height = 200
        self.col_width = 200
        self.restaurante = restaurante
    
        self.frames_temporales = []
        self.framePadre = framePadre
        self.funcionalidad_gestionFinanciera = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionFinanciera.grid(row=0, column=0, sticky="nsew")
        self.options_frame = Frame(self.funcionalidad_gestionFinanciera, bg='#c3c3c3', width=100, height=500)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        self.options_frame.pack_propagate(False)
        self.main_frame = Frame(self.funcionalidad_gestionFinanciera, highlightbackground='black', highlightthickness=2, width=500, height=400)

        # Crear botones de selección de opción
        self.btn_home_page = Button(self.options_frame, text="Inicio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_home_inicio, self.home_indicate))
        self.btn_home_page.grid(row=0, column=0, padx=0, pady=30)

        self.btn_consultar_presupuesto = Button(self.options_frame, text="Presupuesto", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_frame_presupuesto, self.indicate_consultarPresupuesto))
        self.btn_consultar_presupuesto.grid(row=1, column=0, padx=0, pady=30)

        self.btn_consultar_ganancias = Button(self.options_frame, text="Ganancias", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gananciasBrutas, self.indicate_consultarGB))
        self.btn_consultar_ganancias.grid(row=2, column=0, padx=0, pady=30)

        self.btn_consultar_gastos = Button(self.options_frame, text="Gastos", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gastosMateriales, self.indicate_consultarGastosMateriales))
        self.btn_consultar_gastos.grid(row=3, column=0, padx=0, pady=30)

        # Crear indicadores de opción seleccionada
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=0, y=30, width=5, height=40, )

        self.indicate_consultarPresupuesto = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarPresupuesto.place(x=0, y=135, width=5, height=40, )
        
        self.indicate_consultarGanancias = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGanancias.place(x=0, y=255, width=5, height=40, )

        self.indicate_consultarGastos = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGastos.place(x=0, y=375, width=5, height=40, )


        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_inicio(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la Gestion de Financiera", font=("Bold", 15)).place(x=150, y=30)
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_presupuesto(self):
        self.frame_presupuesto = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_presupuesto, text="Presupuesto", font=("Bold", 15)).place(x=150, y=30)
        self.frame_presupuesto.grid(pady=5, padx=5)
        self.frame_presupuesto.pack_propagate(False)

    def function_frame_ganancias(self):
        self.frame_ganancias = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_ganancias, text="Ganancias", font=("Bold", 15)).place(x=150, y=30)
        self.frame_ganancias.grid(pady=5, padx=5)
        self.frame_ganancias.pack_propagate(False)

    def function_frame_gastos(self):
        self.frame_gastos = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_gastos, text="Gastos", font=("Bold", 15)).place(x=150, y=30)
        self.frame_gastos.grid(pady=5, padx=5)
        self.frame_gastos.pack_propagate(False)

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
        self.indicate_consultarPresupuesto.config(bg='#c3c3c3')
        self.indicate_consultarGanancias.config(bg='#c3c3c3')
        self.indicate_consultarGastos.config(bg='#c3c3c3')