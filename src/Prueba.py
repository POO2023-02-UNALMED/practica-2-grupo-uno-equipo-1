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
