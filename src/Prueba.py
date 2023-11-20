# Fieldframe para consultas
from tkinter import *
from tkinter import messagebox

class FieldFrame(Frame):
    """
    hay dos formularios para que data se van guardando la inforfmacion de los widgets
    para poder deshabilitarlos luego de haber respondido el formulario, en dataform
    puedes visualizar los datos de los criterios que has mandado, como un diccionario
    con el titulo de el criterio 
    """
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, consulta):
        super().__init__(master)

        self.data = {}
        self.dataform = {}

        self.tituloValores = tituloValores
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.valores = valores
        self.habilitado = habilitado
        self.consulta = consulta

        # Contenedor que tiene todo el formulario de la consulta
        frameForm = Frame(self, bg="blue", borderwidth=1, relief="solid")
        frameForm.grid(padx=5, pady=5)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que tiene el titulo de la consulta
        tituloCriterios = Label(frameForm, text=f"{tituloCriterios}")
        tituloCriterios.grid(row=0, column=0, padx=5, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que contiene el titulo de valores
        tituloValores = Label(frameForm, text=f"{tituloValores}")
        tituloValores.grid(row=0, column=1, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)

        # Etiqueta para mostrar el titulo de la consulta
        for index, criterio in enumerate(criterios):
            criterio_label = Label(frameForm, text=f"{criterio}")
            criterio_label.grid(row=index+1, column=0, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            input_widget = Entry(frameForm)
            input_widget.grid(row=index+1, column=1, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            if valores and index < len(valores):
                input_widget.insert(0, valores[index])
            
            if not habilitado[index]:
                input_widget.config(state="disabled")
            # Esta parte es necesaria para deshabilitarlos luego de haber 
            # Mnadado el trabajo
            self.data[criterio] = {
                "widget": input_widget,
                "value": None
            }

        # Botón para enviar el formulario
        self.buttonSubmmit = Button(frameForm, text="enviar", command=self.enviar, height=1, width=7)
        self.buttonSubmmit.grid(row=index+2, column=0, pady=20)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Crear boton de eliminar campos
        self.buttonClear = Button(frameForm, text="clear", bg="white", command=self.clear, height=1, width=6)
        self.buttonClear.grid(row=index + 2, column=1)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)
    
    # Obtener valores por titulo de criterio
    def getValue(self, criterio):
        return self.dataform[criterio]["value"]
    
    # Obtener todos los valores
    def getValues(self):
        return self.dataform
    
    # Limpiar los campos
    def clear(self):
        for criterio, info in self.data.items():
            info["widget"].delete(0, END)
            info["value"] = None

    def enviar(self):
        """
        Al momento de enviar el formulario, se selecciona los
        valores de los campos y se deshabilitan los botones de clear
        y submit, se manda la consulta de el usuario con los valores,
        para que se vayan haciendo consultas en cadena, en caso de
        que una consulta dependa de la otr
        """
        print("entra")
        from diseñoGráfico.GestionPedidosApp import GestionPedidosApp
        if GestionPedidosApp.plato_seleccionado == False:
            print("captura la funcion")
            messagebox.showinfo("Alerta", "Debes seleccionar al menos un plato antes de continuar.")
        else:
            self.submitForm()
            valores = self.getValues()
            self.consulta(valores)
            self.buttonClear.destroy()
            self.buttonSubmmit.destroy()

    def submitForm(self):
        """
        Aqui se envia el formulario, se verifica que todos los campos
        esten llenos, en caso de que no, se muestra una alerta, y se
        retorna, en caso de que si, se deshabilitan los campos y se
        guardan los valores en dataform
        """
        for criterio, info in self.data.items():
            valor = info["widget"].get()
            if valor is None or valor == "":
                messagebox.showinfo("Alerta", f"Campo '{criterio}' no puede estar vacío.")
                return
            self.data[criterio]["widget"].config(state="disabled")
            self.data[criterio]["widget"].config(state="disabled")

            # Obtener el valor de el widget
            self.data[criterio]["value"] = valor

            # Guardar el valor en el formulario de dataform
            self.dataform[criterio] = valor
            # self.data["submit"].destroy()
            # self.data["clear"].destroy()


class FieldFrame2(Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado=None):
        super().__init__()

        self.titulo_criterios = Label(self, text=tituloCriterios)
        self.titulo_criterios.grid(row=0, column=0, padx=5, pady=5)

        self.titulo_valores = Label(self, text=tituloValores)
        self.titulo_valores.grid(row=0, column=1, padx=5, pady=5)

        self.entries = {}
        for i, criterio in enumerate(criterios, start=1):
            label = Label(self, text=criterio)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)

            entry = Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=W)
            self.entries[criterio] = entry

            if habilitado and habilitado[i - 1] is  None:
                entry.configure(state=DISABLED)

            if valores and valores[i - 1] is not None:
                entry.insert(0, valores[i - 1])

        self.boton_aceptar = Button(self, text="Aceptar", command=self.guardar_datos)
        self.boton_aceptar.grid(row=len(criterios) + 1, column=0, columnspan=2, pady=10)

        self.boton_borrar = Button(self, text="Borrar", command=self.borrar_campos)
        self.boton_borrar.grid(row=len(criterios) + 2, column=0, columnspan=2, pady=10)

    def getValue(self, criterio):
        entry = self.entries.get(criterio)
        if entry:
            return entry.get()
        else:
            return None

    def guardar_datos(self):
        for criterio, entry in self.entries.items():
            if not entry.get():
                messagebox.showwarning("Advertencia", f"Campo '{criterio}' no puede estar vacío.")
                return  # Si un campo está vacío, mostrar advertencia y salir

        # Aquí puedes guardar los datos según tus necesidades
        # Por ejemplo, puedes imprimir los datos
        print("Datos guardados:")
        for criterio, entry in self.entries.items():
            print(f"{criterio}: {entry.get()}")

    def borrar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, END)# Fieldframe para consultas
from tkinter import *
from tkinter import messagebox

class FieldFrame(Frame):
    """
    hay dos formularios para que data se van guardando la inforfmacion de los widgets
    para poder deshabilitarlos luego de haber respondido el formulario, en dataform
    puedes visualizar los datos de los criterios que has mandado, como un diccionario
    con el titulo de el criterio 
    """
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, consulta):
        super().__init__(master)

        self.data = {}
        self.dataform = {}

        self.tituloValores = tituloValores
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.valores = valores
        self.habilitado = habilitado
        self.consulta = consulta

        # Contenedor que tiene todo el formulario de la consulta
        frameForm = Frame(self, bg="blue", borderwidth=1, relief="solid")
        frameForm.grid(padx=5, pady=5)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que tiene el titulo de la consulta
        tituloCriterios = Label(frameForm, text=f"{tituloCriterios}")
        tituloCriterios.grid(row=0, column=0, padx=5, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que contiene el titulo de valores
        tituloValores = Label(frameForm, text=f"{tituloValores}")
        tituloValores.grid(row=0, column=1, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)

        # Etiqueta para mostrar el titulo de la consulta
        for index, criterio in enumerate(criterios):
            criterio_label = Label(frameForm, text=f"{criterio}")
            criterio_label.grid(row=index+1, column=0, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            input_widget = Entry(frameForm)
            input_widget.grid(row=index+1, column=1, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            if valores and index < len(valores):
                input_widget.insert(0, valores[index])
            
            if not habilitado[index]:
                input_widget.config(state="disabled")
            # Esta parte es necesaria para deshabilitarlos luego de haber 
            # Mnadado el trabajo
            self.data[criterio] = {
                "widget": input_widget,
                "value": None
            }

        # Botón para enviar el formulario
        self.buttonSubmmit = Button(frameForm, text="enviar", command=self.enviar, height=1, width=7)
        self.buttonSubmmit.grid(row=index+2, column=0, pady=20)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Crear boton de eliminar campos
        self.buttonClear = Button(frameForm, text="clear", bg="white", command=self.clear, height=1, width=6)
        self.buttonClear.grid(row=index + 2, column=1)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)
    
    # Obtener valores por titulo de criterio
    def getValue(self, criterio):
        return self.dataform[criterio]["value"]
    
    # Obtener todos los valores
    def getValues(self):
        return self.dataform
    
    # Limpiar los campos
    def clear(self):
        for criterio, info in self.data.items():
            info["widget"].delete(0, END)
            info["value"] = None

    def enviar(self):
        """
        Al momento de enviar el formulario, se selecciona los
        valores de los campos y se deshabilitan los botones de clear
        y submit, se manda la consulta de el usuario con los valores,
        para que se vayan haciendo consultas en cadena, en caso de
        que una consulta dependa de la otr
        """
        print("entra")
        from diseñoGráfico.GestionPedidosApp import GestionPedidosApp
        if GestionPedidosApp.plato_seleccionado == False:
            print("captura la funcion")
            messagebox.showinfo("Alerta", "Debes seleccionar al menos un plato antes de continuar.")
        else:
            self.submitForm()
            valores = self.getValues()
            self.consulta(valores)
            self.buttonClear.destroy()
            self.buttonSubmmit.destroy()

    def submitForm(self):
        """
        Aqui se envia el formulario, se verifica que todos los campos
        esten llenos, en caso de que no, se muestra una alerta, y se
        retorna, en caso de que si, se deshabilitan los campos y se
        guardan los valores en dataform
        """
        for criterio, info in self.data.items():
            valor = info["widget"].get()
            if valor is None or valor == "":
                messagebox.showinfo("Alerta", f"Campo '{criterio}' no puede estar vacío.")
                return
            self.data[criterio]["widget"].config(state="disabled")
            self.data[criterio]["widget"].config(state="disabled")

            # Obtener el valor de el widget
            self.data[criterio]["value"] = valor

            # Guardar el valor en el formulario de dataform
            self.dataform[criterio] = valor
            # self.data["submit"].destroy()
            # self.data["clear"].destroy()


class FieldFrame2(Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado=None):
        super().__init__()

        self.titulo_criterios = Label(self, text=tituloCriterios)
        self.titulo_criterios.grid(row=0, column=0, padx=5, pady=5)

        self.titulo_valores = Label(self, text=tituloValores)
        self.titulo_valores.grid(row=0, column=1, padx=5, pady=5)

        self.entries = {}
        for i, criterio in enumerate(criterios, start=1):
            label = Label(self, text=criterio)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)

            entry = Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=W)
            self.entries[criterio] = entry

            if habilitado and habilitado[i - 1] is  None:
                entry.configure(state=DISABLED)

            if valores and valores[i - 1] is not None:
                entry.insert(0, valores[i - 1])

        self.boton_aceptar = Button(self, text="Aceptar", command=self.guardar_datos)
        self.boton_aceptar.grid(row=len(criterios) + 1, column=0, columnspan=2, pady=10)

        self.boton_borrar = Button(self, text="Borrar", command=self.borrar_campos)
        self.boton_borrar.grid(row=len(criterios) + 2, column=0, columnspan=2, pady=10)

    def getValue(self, criterio):
        entry = self.entries.get(criterio)
        if entry:
            return entry.get()
        else:
            return None

    def guardar_datos(self):
        for criterio, entry in self.entries.items():
            if not entry.get():
                messagebox.showwarning("Advertencia", f"Campo '{criterio}' no puede estar vacío.")
                return  # Si un campo está vacío, mostrar advertencia y salir

        # Aquí puedes guardar los datos según tus necesidades
        # Por ejemplo, puedes imprimir los datos
        print("Datos guardados:")
        for criterio, entry in self.entries.items():
            print(f"{criterio}: {entry.get()}")

    def borrar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, END)# Fieldframe para consultas
from tkinter import *
from tkinter import messagebox

class FieldFrame(Frame):
    """
    hay dos formularios para que data se van guardando la inforfmacion de los widgets
    para poder deshabilitarlos luego de haber respondido el formulario, en dataform
    puedes visualizar los datos de los criterios que has mandado, como un diccionario
    con el titulo de el criterio 
    """
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, consulta):
        super().__init__(master)

        self.data = {}
        self.dataform = {}

        self.tituloValores = tituloValores
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.valores = valores
        self.habilitado = habilitado
        self.consulta = consulta

        # Contenedor que tiene todo el formulario de la consulta
        frameForm = Frame(self, bg="blue", borderwidth=1, relief="solid")
        frameForm.grid(padx=5, pady=5)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que tiene el titulo de la consulta
        tituloCriterios = Label(frameForm, text=f"{tituloCriterios}")
        tituloCriterios.grid(row=0, column=0, padx=5, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que contiene el titulo de valores
        tituloValores = Label(frameForm, text=f"{tituloValores}")
        tituloValores.grid(row=0, column=1, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)

        # Etiqueta para mostrar el titulo de la consulta
        for index, criterio in enumerate(criterios):
            criterio_label = Label(frameForm, text=f"{criterio}")
            criterio_label.grid(row=index+1, column=0, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            input_widget = Entry(frameForm)
            input_widget.grid(row=index+1, column=1, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            if valores and index < len(valores):
                input_widget.insert(0, valores[index])
            
            if not habilitado[index]:
                input_widget.config(state="disabled")
            # Esta parte es necesaria para deshabilitarlos luego de haber 
            # Mnadado el trabajo
            self.data[criterio] = {
                "widget": input_widget,
                "value": None
            }

        # Botón para enviar el formulario
        self.buttonSubmmit = Button(frameForm, text="enviar", command=self.enviar, height=1, width=7)
        self.buttonSubmmit.grid(row=index+2, column=0, pady=20)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Crear boton de eliminar campos
        self.buttonClear = Button(frameForm, text="clear", bg="white", command=self.clear, height=1, width=6)
        self.buttonClear.grid(row=index + 2, column=1)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)
    
    # Obtener valores por titulo de criterio
    def getValue(self, criterio):
        return self.dataform[criterio]["value"]
    
    # Obtener todos los valores
    def getValues(self):
        return self.dataform
    
    # Limpiar los campos
    def clear(self):
        for criterio, info in self.data.items():
            info["widget"].delete(0, END)
            info["value"] = None

    def enviar(self):
        """
        Al momento de enviar el formulario, se selecciona los
        valores de los campos y se deshabilitan los botones de clear
        y submit, se manda la consulta de el usuario con los valores,
        para que se vayan haciendo consultas en cadena, en caso de
        que una consulta dependa de la otr
        """
        print("entra")
        from diseñoGráfico.GestionPedidosApp import GestionPedidosApp
        if GestionPedidosApp.plato_seleccionado == False:
            print("captura la funcion")
            messagebox.showinfo("Alerta", "Debes seleccionar al menos un plato antes de continuar.")
        else:
            self.submitForm()
            valores = self.getValues()
            self.consulta(valores)
            self.buttonClear.destroy()
            self.buttonSubmmit.destroy()

    def submitForm(self):
        """
        Aqui se envia el formulario, se verifica que todos los campos
        esten llenos, en caso de que no, se muestra una alerta, y se
        retorna, en caso de que si, se deshabilitan los campos y se
        guardan los valores en dataform
        """
        for criterio, info in self.data.items():
            valor = info["widget"].get()
            if valor is None or valor == "":
                messagebox.showinfo("Alerta", f"Campo '{criterio}' no puede estar vacío.")
                return
            self.data[criterio]["widget"].config(state="disabled")
            self.data[criterio]["widget"].config(state="disabled")

            # Obtener el valor de el widget
            self.data[criterio]["value"] = valor

            # Guardar el valor en el formulario de dataform
            self.dataform[criterio] = valor
            # self.data["submit"].destroy()
            # self.data["clear"].destroy()


class FieldFrame2(Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado=None):
        super().__init__()

        self.titulo_criterios = Label(self, text=tituloCriterios)
        self.titulo_criterios.grid(row=0, column=0, padx=5, pady=5)

        self.titulo_valores = Label(self, text=tituloValores)
        self.titulo_valores.grid(row=0, column=1, padx=5, pady=5)

        self.entries = {}
        for i, criterio in enumerate(criterios, start=1):
            label = Label(self, text=criterio)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)

            entry = Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=W)
            self.entries[criterio] = entry

            if habilitado and habilitado[i - 1] is  None:
                entry.configure(state=DISABLED)

            if valores and valores[i - 1] is not None:
                entry.insert(0, valores[i - 1])

        self.boton_aceptar = Button(self, text="Aceptar", command=self.guardar_datos)
        self.boton_aceptar.grid(row=len(criterios) + 1, column=0, columnspan=2, pady=10)

        self.boton_borrar = Button(self, text="Borrar", command=self.borrar_campos)
        self.boton_borrar.grid(row=len(criterios) + 2, column=0, columnspan=2, pady=10)

    def getValue(self, criterio):
        entry = self.entries.get(criterio)
        if entry:
            return entry.get()
        else:
            return None

    def guardar_datos(self):
        for criterio, entry in self.entries.items():
            if not entry.get():
                messagebox.showwarning("Advertencia", f"Campo '{criterio}' no puede estar vacío.")
                return  # Si un campo está vacío, mostrar advertencia y salir

        # Aquí puedes guardar los datos según tus necesidades
        # Por ejemplo, puedes imprimir los datos
        print("Datos guardados:")
        for criterio, entry in self.entries.items():
            print(f"{criterio}: {entry.get()}")

    def borrar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, END)# Fieldframe para consultas
from tkinter import *
from tkinter import messagebox

class FieldFrame(Frame):
    """
    hay dos formularios para que data se van guardando la inforfmacion de los widgets
    para poder deshabilitarlos luego de haber respondido el formulario, en dataform
    puedes visualizar los datos de los criterios que has mandado, como un diccionario
    con el titulo de el criterio 
    """
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, consulta):
        super().__init__(master)

        self.data = {}
        self.dataform = {}

        self.tituloValores = tituloValores
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.valores = valores
        self.habilitado = habilitado
        self.consulta = consulta

        # Contenedor que tiene todo el formulario de la consulta
        frameForm = Frame(self, bg="blue", borderwidth=1, relief="solid")
        frameForm.grid(padx=5, pady=5)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que tiene el titulo de la consulta
        tituloCriterios = Label(frameForm, text=f"{tituloCriterios}")
        tituloCriterios.grid(row=0, column=0, padx=5, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Contenedor que contiene el titulo de valores
        tituloValores = Label(frameForm, text=f"{tituloValores}")
        tituloValores.grid(row=0, column=1, pady =10)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)

        # Etiqueta para mostrar el titulo de la consulta
        for index, criterio in enumerate(criterios):
            criterio_label = Label(frameForm, text=f"{criterio}")
            criterio_label.grid(row=index+1, column=0, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            input_widget = Entry(frameForm)
            input_widget.grid(row=index+1, column=1, padx=5, pady=10)
            frameForm.grid_rowconfigure(index+1, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)
            
            if valores and index < len(valores):
                input_widget.insert(0, valores[index])
            
            if not habilitado[index]:
                input_widget.config(state="disabled")
            # Esta parte es necesaria para deshabilitarlos luego de haber 
            # Mnadado el trabajo
            self.data[criterio] = {
                "widget": input_widget,
                "value": None
            }

        # Botón para enviar el formulario
        self.buttonSubmmit = Button(frameForm, text="enviar", command=self.enviar, height=1, width=7)
        self.buttonSubmmit.grid(row=index+2, column=0, pady=20)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Crear boton de eliminar campos
        self.buttonClear = Button(frameForm, text="clear", bg="white", command=self.clear, height=1, width=6)
        self.buttonClear.grid(row=index + 2, column=1)
        frameForm.grid_rowconfigure(index+2, weight=1)
        frameForm.grid_columnconfigure(1, weight=1)
    
    # Obtener valores por titulo de criterio
    def getValue(self, criterio):
        return self.dataform[criterio]["value"]
    
    # Obtener todos los valores
    def getValues(self):
        return self.dataform
    
    # Limpiar los campos
    def clear(self):
        for criterio, info in self.data.items():
            info["widget"].delete(0, END)
            info["value"] = None

    def enviar(self):
        """
        Al momento de enviar el formulario, se selecciona los
        valores de los campos y se deshabilitan los botones de clear
        y submit, se manda la consulta de el usuario con los valores,
        para que se vayan haciendo consultas en cadena, en caso de
        que una consulta dependa de la otr
        """
        print("entra")
        from diseñoGráfico.GestionPedidosApp import GestionPedidosApp
        if GestionPedidosApp.plato_seleccionado == False:
            print("captura la funcion")
            messagebox.showinfo("Alerta", "Debes seleccionar al menos un plato antes de continuar.")
        else:
            self.submitForm()
            valores = self.getValues()
            self.consulta(valores)
            self.buttonClear.destroy()
            self.buttonSubmmit.destroy()

    def submitForm(self):
        """
        Aqui se envia el formulario, se verifica que todos los campos
        esten llenos, en caso de que no, se muestra una alerta, y se
        retorna, en caso de que si, se deshabilitan los campos y se
        guardan los valores en dataform
        """
        for criterio, info in self.data.items():
            valor = info["widget"].get()
            if valor is None or valor == "":
                messagebox.showinfo("Alerta", f"Campo '{criterio}' no puede estar vacío.")
                return
            self.data[criterio]["widget"].config(state="disabled")
            self.data[criterio]["widget"].config(state="disabled")

            # Obtener el valor de el widget
            self.data[criterio]["value"] = valor

            # Guardar el valor en el formulario de dataform
            self.dataform[criterio] = valor
            # self.data["submit"].destroy()
            # self.data["clear"].destroy()


class FieldFrame2(Frame):
    def __init__(self, tituloCriterios, criterios, tituloValores, valores, habilitado=None):
        super().__init__()

        self.titulo_criterios = Label(self, text=tituloCriterios)
        self.titulo_criterios.grid(row=0, column=0, padx=5, pady=5)

        self.titulo_valores = Label(self, text=tituloValores)
        self.titulo_valores.grid(row=0, column=1, padx=5, pady=5)

        self.entries = {}
        for i, criterio in enumerate(criterios, start=1):
            label = Label(self, text=criterio)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)

            entry = Entry(self)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=W)
            self.entries[criterio] = entry

            if habilitado and habilitado[i - 1] is  None:
                entry.configure(state=DISABLED)

            if valores and valores[i - 1] is not None:
                entry.insert(0, valores[i - 1])

        self.boton_aceptar = Button(self, text="Aceptar", command=self.guardar_datos)
        self.boton_aceptar.grid(row=len(criterios) + 1, column=0, columnspan=2, pady=10)

        self.boton_borrar = Button(self, text="Borrar", command=self.borrar_campos)
        self.boton_borrar.grid(row=len(criterios) + 2, column=0, columnspan=2, pady=10)

    def getValue(self, criterio):
        entry = self.entries.get(criterio)
        if entry:
            return entry.get()
        else:
            return None

    def guardar_datos(self):
        for criterio, entry in self.entries.items():
            if not entry.get():
                messagebox.showwarning("Advertencia", f"Campo '{criterio}' no puede estar vacío.")
                return  # Si un campo está vacío, mostrar advertencia y salir

        # Aquí puedes guardar los datos según tus necesidades
        # Por ejemplo, puedes imprimir los datos
        print("Datos guardados:")
        for criterio, entry in self.entries.items():
            print(f"{criterio}: {entry.get()}")

    def borrar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, END)
