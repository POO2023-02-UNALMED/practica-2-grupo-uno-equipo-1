from tkinter import *
from tkinter import messagebox, font
from PIL import Image, ImageTk

# funciones ventana de inicio
def salir():
    """
    Salir de la aplicacion
    """
    ventanaInicio.destroy()

def ver_descripcion():
    pass

def cambiarHojaVida(hojaVida, widget):
    """
    En esta funcion se cambia la hoja de vida
    segun el indice de la hoja de vida actual,
    el modulo se tiene en cuenta para que este
    en el rango de las hojas de vidas disponibles
    """
    global indice_texto
    global indice_imagenes
    global imagenesP6
    
    # cambiar hoja de vida
    hojaVida.config(state="normal")
    # Indice de texto este en el rango de la lista
    indice_texto = (indice_texto + 1) % len(hojasDeVida)
    texto_siguiente = hojasDeVida[indice_texto]
    hojaVida.delete("1.0", END)
    hojaVida.insert(END, texto_siguiente)
    hojaVida.config(state="disabled")

    # Indice de imagenes este en elr ango de la lista
    indice_imagenes = (indice_imagenes + 4) % len(imagenesP6)
    
    # Esto se hace para borrar las imagenes que estan en el frame
    for imagen in imagenesP6:
        imagen.grid_forget()

    # Esto se hace para mostrar las imagenes en el frame
    imagenesP6[indice_imagenes].grid(row=0, column=0, padx=2, pady=2)
    imagenesP6[indice_imagenes+1].grid(row=0, column=1, padx=2, pady=2)
    imagenesP6[indice_imagenes+2].grid(row=1, column=0, padx=2, pady=2)
    imagenesP6[indice_imagenes+3].grid(row=1, column=1, padx=2, pady=2)

def irVentanaPrincipal():
    """
    Aqui se oculta la ventana de inicio y se muestra
    la ventana principal
    """
    ventanaInicio.withdraw()
    ventanaPrincipal.deiconify()

def cambiarImagen(widget, event):
    """
    segun esta imagen se cambia la iamgen que se muestra en
    la ventana de inicio
    """
    global indice_imagen
    global imagen_mostrar

    # Obtener las coordenadas de la esquina superior izquierda del widget
    x_inicio = widget.winfo_rootx()
    y_inicio = widget.winfo_rooty()

    # Obtener las coordenadas de la esquina inferior derecha del widget
    ancho_imagen = 320
    alto_imagen = 275
    x_final = x_inicio + ancho_imagen
    y_final = y_inicio + alto_imagen

    x_raton = event.x_root
    y_raton = event.y_root

    if x_inicio <= x_raton <= x_final and y_inicio <= y_raton <= y_final:
        indice_imagen = (indice_imagen + 1) % len(imagenesP5)
        imagen_mostrar = Label(imagenesIzquierda, image=imagenesP5[indice_imagen])
        imagen_mostrar.grid(row=0, column=0, padx=5, pady=5)

# Funciones ventana principal
def nada():
    pass

def infoApp():
    opcion=messagebox.showinfo("Información sobre la aplicación","Esta aplicacion esta diseñada para que puedas llevar toda la gestion de tu restaurante como administrador, reservas, pedidos, empleados y materiales")

def volverAInicio():
    ventanaInicio.deiconify()
    ventanaPrincipal.withdraw()

def gReserva():
    v1 = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    v1.pack(fill="y", expand=False, anchor="c")
    label1 = Label(v1, text="Gestión de reservas", font=("arial", 30), fg="blue", bg="gray77")
    botonConsultarRSV = Button(v1, text="Reservas sin verificar", width=30, height=10)
    botonConsultarRV = Button(v1, text="Reservas verificadas", width=30, height=10)
    botonCrearR = Button(v1, text="Crear reserva", width=30, height=10)
    botonCancelarR = Button(v1, text="Cancelar reservas", width=30, height=10)
    botonAsignarM= Button(v1, text="Asignar mesas a las reservas", width=30, height=10)
    label1.grid(row=0, column=1, padx=10, pady=10)
    botonConsultarRSV.grid(row=1, column=0, padx=20, pady=10)
    botonConsultarRV.grid(row=1, column=2, padx=10, pady=10)
    botonCrearR.grid(row=2, column=1, padx=10, pady=10)
    botonCancelarR.grid(row=3, column=0, padx=20, pady=10)
    botonAsignarM.grid(row=3, column=2, padx=10, pady=10)
    for i in range(5):
        v1.grid_columnconfigure(i, weight=1)

def gestion_pedidos(widget):
    widget.tkraise()
    pass

def gEmpleado():
    pass

def gInventario():
    pass

def gFinanciera():
    v5 = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    v5.pack(fill="y", expand=False, anchor="c")

    presupuesto = financia.presupuesto()
    gananciasNetas = financia.gananciasNetas()
    gananciasBrutas = financia.gananciasBrutas()
    gastoMaterialEspecifico = financia.gastoMaterialEspecifico()
    totalGastosMateriales = financia.gastosMateriales()
    totalPagosEmpleados = financia.pagosEmpleados()
    pagoempleado = financia.pagoEmpleado()
    liquidacion = financia.liquidacionEmpleado()
    costoPromedioPlato = financia.costoPromedioPorPlato()

    # Configurar el Frame de Finanzas
    frameFinanzas = FieldFrame(ventanaPrincipal, text="Finanzas")
    frameFinanzas.pack(pady=10)

    # Asociar botones con métodos
    buttonPresupuesto = Button(v1, text="Presupuesto",  command=lambda: mostrarResultado(presupuesto))
    buttonPresupuesto.pack()

    buttonGananciasNetas = Button(frameFinanzas, text="Ganancias Netas", command=lambda: mostrarResultado(gananciasNetas))
    buttonGananciasNetas.pack()

    buttonGananciasBrutas = Button(frameFinanzas, text="Ganancias Brutas", command=lambda: mostrarResultado(gananciasBrutas))
    buttonGananciasBrutas.pack()
    
    buttonGastosMateriales = Button(frameFinanzas, text="Gastos Materiales", command=lambda: mostrarResultado(totalGastosMateriales))
    buttonGastosMateriales.pack()

    buttonGastoMaterialEsp = Button(frameFinanzas, text="Gasto Material Especifico", command=lambda: mostrarResultado(gastoMaterialEspecifico))
    buttonGastosMaterialesEsp.pack()

    buttonPagosEmpleados = Button(frameFinanzas, text="Pagos a Empleados", command=lambda: mostrarResultado(totalPagosEmpleados))
    buttonPagosEmpleados.pack()

    buttonPagoEmpleado = Button(frameFinanzas, text="Pago a Empleado", command=lambda: mostrarResultado(pagoempleado))
    buttonPagoEmpleado.pack()

    buttonLiquidacion = Button(frameFinanzas, text="Liquidación", command=lambda: mostrarResultado(liquidacion))
    buttonLiquidacion.pack()

    buttonCostoPromedioPlato = Button(frameFinanzas, text="Costo Promedio por Plato", command=lambda: mostrarResultado(costoPromedioPlato))
    buttonCostoPromedioPlato.pack()

def mostrarResultado(resultado):
    labelResultado = Label(frameFinanzas, text=f"Resultado: {resultado}")
    labelResultado.pack()

#mmmm
    label1 = Label(v1, text="Gestión Financiera", font=("arial", 30), fg="blue", bg="gray77")
    botonPresupuesto = Button(v1, text="Presupuesto del Restaurante", width=30, height=10)
    botonGananciasBrutas = Button(v1, text="Ganancias Brutas del Restaurante", width=30, height=10)
    botonGananciasNetas = Button(v1, text="Ganancias Netas del Restaurante", width=30, height=10)
    botonGastosMateriales = Button(v1, text="Consultar Gastos del Inventario", width=30, height=10)
    botonGastosMaterialesEsp= Button(v1, text="Consultar Gasto Especifico de un Material", width=30, height=10)
    botonLiquidacion= Button(v1, text="Consultar Liquidación de un Empleado", width=30, height=10)
    botonPagoEmpleados= Button(v1, text="Consultar Pago total de los Empleados", width=30, height=10)
    botonPagoEmpleadosEsp= Button(v1, text="Consultar Pago total de un Empleado", width=30, height=10)
    botonCostoPromedio= Button(v1, text="Consultar el costo Promedio de realizar un plato", width=30, height=10)
    label1.grid(row=0, column=1, padx=10, pady=10)
    botonPresupuesto.grid(row=1, column=0, padx=20, pady=10)
    botonGananciasBrutas.grid(row=1, column=2, padx=10, pady=10)
    botonGananciasNetas.grid(row=2, column=1, padx=10, pady=10)
    botonGastosMateriales.grid(row=3, column=0, padx=20, pady=10)
    botonGastosMaterialesEsp.grid(row=3, column=2, padx=10, pady=10)

def ayuda():
    opcion=messagebox.showinfo("Autores la aplicación","Daniel Garzón\n Samuel Ortiz\n Jhogert Bita\n Sebastian Hoyos\n Nicole Guaranguay")


# Creacion de ventana de inicio
ventanaInicio = Tk()
ventanaInicio.title("Sistema de Gestión de Restaurante Le Quaso")
ventanaInicio.geometry("800x600")


# Creacion  de frames
frameIzquierdo = Frame(ventanaInicio,bd=2, relief="solid")
frameDerecho = Frame(ventanaInicio,bd=2, relief="solid")
frameDerecho.pack(side="right", padx=10, pady=10)
frameIzquierdo.pack(side="left", padx=10, pady=10)

# Organizacion frameIzquierdo
# Etiqueta de bienvenida(Creacion de p3)
saludoBienvenida = Text(
    frameIzquierdo,
    bg="gray80",
    width=50,
    height=5,
    font=("Arial", 10),
    )
# indice_imagen
indice_imagen = 0

# agregar el texto a la etiqueta
saludoBienvenida.insert(END, "Bienvenido al Sistema de Gestión de Restaurante\nEsta aplicacion esta diseñada para que puedas llevar toda lagestion de tu restaurante.")
saludoBienvenida.config(state="disabled")

# Posicionamiento de la etiqueta de bienvenida
saludoBienvenida.pack(padx=10, pady=10)

# Imagenes de la izquierda
imagenesIzquierda = Frame(frameIzquierdo, highlightthickness=2)
imagenesIzquierda.pack(side="bottom", padx=10, pady=10)

# Imagenes leQuaso
logoLeQuaso = Image.open("src\logo_leQuaso.png")
localLeQuaso = Image.open("src\local_leQuaso.png")
especialidad1 = Image.open("src\especialidad1.png")
especialidad2 = Image.open("src\especialidad2.png")
especialidad3 = Image.open("src\especialidad3.png")


# Redimensionamiento de las imágenes
logoLeQuaso = logoLeQuaso.resize((320, 275))
localLeQuaso = localLeQuaso.resize((320, 275))
especialidad1 = especialidad1.resize((320, 275))
especialidad2 = especialidad2.resize((320, 275))
especialidad3 = especialidad3.resize((320, 275))

# Creación de PhotoImage desde las imágenes redimensionadas
logoLeQuaso_imagen = ImageTk.PhotoImage(logoLeQuaso)
localLeQuaso_imagen = ImageTk.PhotoImage(localLeQuaso)
especialidad1_imagen = ImageTk.PhotoImage(especialidad1)
especialidad2_imagen = ImageTk.PhotoImage(especialidad2)
especialidad3_imagen = ImageTk.PhotoImage(especialidad3)

# Imagenes disponibles
imagenesP5 = [logoLeQuaso_imagen, localLeQuaso_imagen, especialidad1_imagen, especialidad2_imagen, especialidad3_imagen]

# Boton de cambio
botonCambio = Button(imagenesIzquierda, text="Ingresar", bg="gray37",fg="white",command=irVentanaPrincipal, width=10, height=2)

# mostrar imagen
imagen_mostrar = Label(imagenesIzquierda, image=imagenesP5[indice_imagen])
imagen_mostrar.grid(row=0, column=0, padx=5, pady=5)
imagenesIzquierda.bind('<Motion>', lambda event: cambiarImagen(imagenesIzquierda, event))
botonCambio.grid(row=1, column=0, padx=5, pady=5)


# Organizacion frameDerecho
# Hojas de vida
hojasDeVida = [
    "hojaVida1",
    "Nombre: Samuel Ortiz Toro\nFecha de Nacimiento: 6 de Mayo de 2004\nPasatiempos: Política y Religión",
    "hojaVida3",
    "Nombre: Juan Sebastian Hoyos Castillo\nFecha de Nacimiento: 7 de Febrero de 2002\nPasatiempos: Jugar videojuegos y ver anime",
    "Nombre: Nicole Natalia Guaranguay Parra\nFecha de Nacimiento: 11 de Abril de 2005\nPasatiempos: Ver anime y salir con mis amigos"
    ]

# Indice de la hoja de vida actualizada
indice_texto = 0

# Etiqueta de descripcion(Creacion de p5)
hojaVida = Text(
    frameDerecho,
    bg="gray80",
    width=40,
    height=5,
    font=("Arial", 11),
    )

# Configuracion de imagenes con eventos(Creacion de p5)
imagenesDerecha = Frame(frameDerecho, highlightthickness=2)
imagenesDerecha.pack(side="bottom", padx=10, pady=10)

# Dimensiones de las imágenes
ancho = 150
alto = 150

# Rutas de las imágenes
imagen_daniel1 = Image.open("src\imagen_daniel1.png")
imagen_daniel2 = Image.open("src\imagen_daniel2.png")
imagen_daniel3 = Image.open("src\imagen_daniel3.png")
imagen_daniel4 = Image.open("src\imagen_daniel4.png")

imagen_samuel1 = Image.open("src\imagen_samuel1.png")
imagen_samuel2 = Image.open("src\imagen_samuel2.png")
imagen_samuel3 = Image.open("src\imagen_samuel3.png")
imagen_samuel4 = Image.open("src\imagen_samuel4.png")

imagen_jhogert1 = Image.open("src\imagen_jhogert1.png")
imagen_jhogert2 = Image.open("src\imagen_jhogert2.png")
imagen_jhogert3 = Image.open("src\imagen_jhogert3.png")
imagen_jhogert4 = Image.open("src\imagen_jhogert4.png")

imagen_sebastian1 = Image.open("src\imagen_sebastian1.png")
imagen_sebastian2 = Image.open("src\imagen_sebastian2.png")
imagen_sebastian3 = Image.open("src\imagen_sebastian3.png")
imagen_sebastian4 = Image.open("src\imagen_sebastian1.png")

imagen_nicole1 = Image.open("src\imagen_nicole1.png")
imagen_nicole2 = Image.open("src\imagen_nicole2.png")
imagen_nicole3 = Image.open("src\imagen_nicole3.png")
imagen_nicole4 = Image.open("src\imagen_nicole4.png")


# Redimensionamiento de las imágenes
imagen_daniel1 = imagen_daniel1.resize((ancho, alto))
imagen_daniel2 = imagen_daniel2.resize((ancho, alto))
imagen_daniel3 = imagen_daniel3.resize((ancho, alto))
imagen_daniel4 = imagen_daniel4.resize((ancho, alto))

imagen_samuel1 = imagen_samuel1.resize((ancho, alto))
imagen_samuel2 = imagen_samuel2.resize((ancho, alto))
imagen_samuel3 = imagen_samuel3.resize((ancho, alto))
imagen_samuel4 = imagen_samuel4.resize((ancho, alto))

imagen_jhogert1 = imagen_jhogert1.resize((ancho, alto))
imagen_jhogert2 = imagen_jhogert2.resize((ancho, alto))
imagen_jhogert3 = imagen_jhogert3.resize((ancho, alto))
imagen_jhogert4 = imagen_jhogert4.resize((ancho, alto))

imagen_sebastian1 = imagen_sebastian1.resize((ancho, alto))
imagen_sebastian2 = imagen_sebastian2.resize((ancho, alto))
imagen_sebastian3 = imagen_sebastian3.resize((ancho, alto))
imagen_sebastian4 = imagen_sebastian4.resize((ancho, alto))

imagen_nicole1 = imagen_nicole1.resize((ancho, alto))
imagen_nicole2 = imagen_nicole2.resize((ancho, alto))
imagen_nicole3 = imagen_nicole3.resize((ancho, alto))
imagen_nicole4 = imagen_nicole4.resize((ancho, alto))

# Creación de PhotoImage desde las imágenes redimensionadas(P6)
desarrollador_daniel_imagen1 = ImageTk.PhotoImage(imagen_daniel1)
desarrollador_daniel_imagen2 = ImageTk.PhotoImage(imagen_daniel2)
desarrollador_daniel_imagen3 = ImageTk.PhotoImage(imagen_daniel3)
desarrollador_daniel_imagen4 = ImageTk.PhotoImage(imagen_daniel4)

desarrollador_samuel_imagen1 = ImageTk.PhotoImage(imagen_samuel1)
desarrollador_samuel_imagen2 = ImageTk.PhotoImage(imagen_samuel2)
desarrollador_samuel_imagen3 = ImageTk.PhotoImage(imagen_samuel3)
desarrollador_samuel_imagen4 = ImageTk.PhotoImage(imagen_samuel4)

desarrollador_jhogert_imagen1 = ImageTk.PhotoImage(imagen_jhogert1)
desarrollador_jhogert_imagen2 = ImageTk.PhotoImage(imagen_jhogert2)
desarrollador_jhogert_imagen3 = ImageTk.PhotoImage(imagen_jhogert3)
desarrollador_jhogert_imagen4 = ImageTk.PhotoImage(imagen_jhogert4)

desarrollador_sebastian_imagen1 = ImageTk.PhotoImage(imagen_sebastian1)
desarrollador_sebastian_imagen2 = ImageTk.PhotoImage(imagen_sebastian2)
desarrollador_sebastian_imagen3 = ImageTk.PhotoImage(imagen_sebastian3)
desarrollador_sebastian_imagen4 = ImageTk.PhotoImage(imagen_sebastian4)

desarrollador_nicole_imagen1 = ImageTk.PhotoImage(imagen_nicole1)
desarrollador_nicole_imagen2 = ImageTk.PhotoImage(imagen_nicole2)
desarrollador_nicole_imagen3 = ImageTk.PhotoImage(imagen_nicole3)
desarrollador_nicole_imagen4 = ImageTk.PhotoImage(imagen_nicole4)

# Etiquetas de las imágenes
desarrollador_daniel_1 = Label(imagenesDerecha, image=desarrollador_daniel_imagen1)
desarrollador_daniel_2 = Label(imagenesDerecha, image=desarrollador_daniel_imagen2)
desarrollador_daniel_3 = Label(imagenesDerecha, image=desarrollador_daniel_imagen3)
desarrollador_daniel_4 = Label(imagenesDerecha, image=desarrollador_daniel_imagen4)

desarrollador_samuel_1 = Label(imagenesDerecha, image=desarrollador_samuel_imagen1)
desarrollador_samuel_2 = Label(imagenesDerecha, image=desarrollador_samuel_imagen2)
desarrollador_samuel_3 = Label(imagenesDerecha, image=desarrollador_samuel_imagen3)
desarrollador_samuel_4 = Label(imagenesDerecha, image=desarrollador_samuel_imagen4)

desarrollador_jhogert_1 = Label(imagenesDerecha, image=desarrollador_jhogert_imagen1)
desarrollador_jhogert_2 = Label(imagenesDerecha, image=desarrollador_jhogert_imagen2)
desarrollador_jhogert_3 = Label(imagenesDerecha, image=desarrollador_jhogert_imagen3)
desarrollador_jhogert_4 = Label(imagenesDerecha, image=desarrollador_jhogert_imagen4)

desarrollador_sebastian_1 = Label(imagenesDerecha, image=desarrollador_sebastian_imagen1)
desarrollador_sebastian_2 = Label(imagenesDerecha, image=desarrollador_sebastian_imagen2)
desarrollador_sebastian_3 = Label(imagenesDerecha, image=desarrollador_sebastian_imagen3)
desarrollador_sebastian_4 = Label(imagenesDerecha, image=desarrollador_sebastian_imagen4)

desarrollador_nicole_1 = Label(imagenesDerecha, image=desarrollador_nicole_imagen1)
desarrollador_nicole_2 = Label(imagenesDerecha, image=desarrollador_nicole_imagen2)
desarrollador_nicole_3 = Label(imagenesDerecha, image=desarrollador_nicole_imagen3)
desarrollador_nicole_4 = Label(imagenesDerecha, image=desarrollador_nicole_imagen4)

imagenesP6 = [desarrollador_daniel_1, desarrollador_daniel_2, desarrollador_daniel_3, desarrollador_daniel_4,
              desarrollador_samuel_1, desarrollador_samuel_2, desarrollador_samuel_3, desarrollador_samuel_4,
              desarrollador_jhogert_1, desarrollador_jhogert_2, desarrollador_jhogert_3, desarrollador_jhogert_4,
              desarrollador_sebastian_1, desarrollador_sebastian_2, desarrollador_sebastian_3, desarrollador_sebastian_4,
              desarrollador_nicole_1, desarrollador_nicole_2, desarrollador_nicole_3, desarrollador_nicole_4,
              ]
indice_imagenes = 0

# Configruracion de la etiqueta de descripcion
hojaVida.insert(END, hojasDeVida[indice_texto])
hojaVida.config(state="disabled")
hojaVida.pack(side = 'top', padx=10, pady=10)
hojaVida.bind("<Button-1>", lambda event: cambiarHojaVida(hojaVida, imagenesDerecha))

# Configuración con grid
imagenesP6[indice_imagenes].grid(row=0, column=0, padx=2, pady=2)
imagenesP6[indice_imagenes+1].grid(row=0, column=1, padx=2, pady=2)
imagenesP6[indice_imagenes+2].grid(row=1, column=0, padx=2, pady=2)
imagenesP6[indice_imagenes+3].grid(row=1, column=1, padx=2, pady=2)



# Configuracion de menu(ventana inicio)
menuPrincipal = Menu(ventanaInicio)
ventanaInicio.config(menu=menuPrincipal)

# Configuracion de menu inicio
menuInicio = Menu(menuPrincipal)
menuPrincipal.add_cascade(label="Inicio", menu=menuInicio)
menuInicio.add_command(label="Salir", command=salir)
menuInicio.add_command(label="Descripcion", command=ver_descripcion)

# Creacion de ventana principal
ventanaPrincipal = Toplevel()
ventanaPrincipal.title("Gestion Administrativa Le Quasó")
ventanaPrincipal.geometry("1080x720")

# Creacion de frame
frame1 = Frame(ventanaPrincipal,bg="gray89",height=720)

menuBar = Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=menuBar)
menu1 = Menu(menuBar)
menu2 = Menu(menuBar)
menu3 = Menu(menuBar)


menuBar.add_cascade(label="Archivo",menu=menu1)
menuBar.add_cascade(label="Procesos y Consultas",menu=menu2)
menuBar.add_cascade(label="Ayuda",menu=menu3)
menuBar.add_separator()

menu1.add_command(label="Aplicación",command=infoApp)
menu1.add_command(label="Salir",command=volverAInicio)


framePedidos = Frame(ventanaPrincipal)
framePedidos.pack(side="top", padx=10, pady=10)
saludoPedidos = Label(framePedidos, text="Gestion de pedidos")
saludoPedidos.grid(row=1, column=1)

menu2.add_command(label="Gestión de Reservas",command=gReserva)
menu2.add_command(label="Gestión de Pedidos",command=lambda: gestion_pedidos(framePedidos))
menu2.add_command(label="Gestión de Empleados",command=gEmpleado)
menu2.add_command(label="Gestión de Inventario",command=gInventario)
menu2.add_command(label="Gestión Financiera",command=gFinanciera)

menu3.add_command(label="Acerca de",command=ayuda)


# Ocultar ventana principal
ventanaPrincipal.withdraw()

# Configuracion de menu ayuda
ventanaInicio.mainloop()
