from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# funciones ventana de inicio
def salir():
    """
    Salir de la aplicacion
    """
    ventanaInicio.destroy()

def ver_descripcion():
    pass


def cambiarHojaVida(hojaVida):
    """
    En esta funcion se cambia la hoja de vida
    segun el indice de la hoja de vida actual,
    el modulo se tien en cuenta para que este 
    en el rango de las hojas de vidas disponibles
    """
    global indice_texto
    hojaVida.config(state="normal")
    indice_texto = (indice_texto + 1) % len(hojasDeVida)
    texto_siguiente = hojasDeVida[indice_texto]
    hojaVida.delete("1.0", END)
    hojaVida.insert(END, texto_siguiente)
    hojaVida.config(state="disabled")

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


def gReserva():
    pass

def gPedido():
    pass

def gEmpleado():
    pass

def gInventario():
    pass

def gFinanciera():
    pass

def ayuda():
    opcion=messagebox.showinfo("Autores la aplicación","Daniel Garzón\n Samuel Ortiz\n Jhogert Bita\n Sebastian Hoyos\n Nicole Guaranguay")


# Creacion de ventana de inicio
ventanaInicio = Tk()
ventanaInicio.title("Sistema de Gestión de Restaurante Le Quaso")
ventanaInicio.geometry("800x600")


# Creacion  de frames
frameIzquierdo = Frame(ventanaInicio, highlightthickness=2)
frameDerecho = Frame(ventanaInicio, highlightthickness=2)
frameDerecho.pack(side="right", padx=10, pady=10)
frameIzquierdo.pack(side="left", padx=10, pady=10)

# Organizacion frameIzquierdo
# Etiqueta de bienvenida(Creacion de p3)
saludoBienvenida = Text(
    frameIzquierdo,
    width=40,
    height=5,
    font=("Arial", 11),
    )
# indice_imagen
indice_imagen = 0

# agregar el texto a la etiqueta
saludoBienvenida.insert(END, "Bienvenido al Sistema de Gestión de Restaurante, Esta aplicacion esta diseñada para que puedas llevar toda la gestion de tu restaurante como administrador, reservas, pedidos, empleados y materiales")
saludoBienvenida.config(state="disabled")

# Posicionamiento de la etiqueta de bienvenida
saludoBienvenida.pack(padx=10, pady=10)

# Imagenes de la izquierda
imagenesIzquierda = Frame(frameIzquierdo, highlightthickness=2)
imagenesIzquierda.pack(side="right", padx=10, pady=10)

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
botonCambio = Button(imagenesIzquierda, text="Ventana Principal", command=irVentanaPrincipal, width=45, height=2)

# mostrar imagen
imagen_mostrar = Label(imagenesIzquierda, image=imagenesP5[indice_imagen]) 
imagen_mostrar.grid(row=0, column=0, padx=5, pady=5)
imagenesIzquierda.bind('<Motion>', lambda event: cambiarImagen(imagenesIzquierda, event))
botonCambio.grid(row=1, column=0, padx=5, pady=5)


# Organizacion frameDerecho
# Hojas de vida
hojasDeVida = [
    "hojaVida1",
    "hojaVida2",
    "hojaVida3",
    "hojaVida4",
    "hojaVida5"
    ]

# Indice de la hoja de vida actualizada
indice_texto = 0

# Etiqueta de descripcion(Creacion de p5)
hojaVida = Text(
    frameDerecho,
    width=40,
    height=5,
    font=("Arial", 11),
    )
# Configruracion de la etiqueta de descripcion
hojaVida.insert(END, hojasDeVida[indice_texto])
hojaVida.config(state="disabled")
hojaVida.pack(padx=10, pady=10)
hojaVida.bind("<Button-3>", lambda event: cambiarHojaVida(hojaVida))

# Configuracion de imagenes con eventos(Creacion de p5)
imagenesDerecha = Frame(frameDerecho, highlightthickness=2)
imagenesDerecha.pack(side="right", padx=10, pady=10)

# Dimensiones de las imágenes
ancho = 100
alto = 100

# Rutas de las imágenes
imagen_daniel = Image.open("src\desarrollador1.png")
imagen_samuel = Image.open("src\desarrollador2.png")
imagen_jhogert = Image.open("src\desarrollador3.png")
imagen_sebastian = Image.open("src\desarrollador4.png")
imagen_nicole = Image.open("src\desarrollador5.png")

# Redimensionamiento de las imágenes
imagen_daniel = imagen_daniel.resize((ancho, alto))
imagen_samuel = imagen_samuel.resize((ancho, alto))
imagen_jhogert = imagen_jhogert.resize((ancho, alto))
imagen_sebastian = imagen_sebastian.resize((ancho, alto))
imagen_nicole = imagen_nicole.resize((ancho, alto))

# Creación de PhotoImage desde las imágenes redimensionadas
desarrollador_daniel_imagen = ImageTk.PhotoImage(imagen_daniel)
desarrollador_samuel_imagen = ImageTk.PhotoImage(imagen_samuel)
desarrollador_jhogert_imagen = ImageTk.PhotoImage(imagen_jhogert)
desarrollador_sebastian_imagen = ImageTk.PhotoImage(imagen_sebastian)
desarrollador_nicole_imagen = ImageTk.PhotoImage(imagen_nicole)

# Etiquetas de las imágenes
desarrollador_daniel = Label(imagenesDerecha, image=desarrollador_daniel_imagen)
desarrollador_samuel = Label(imagenesDerecha, image=desarrollador_samuel_imagen)
desarrollador_jhogert = Label(imagenesDerecha, image=desarrollador_jhogert_imagen)
desarrollador_sebastian = Label(imagenesDerecha, image=desarrollador_sebastian_imagen)
desarrollador_nicole = Label(imagenesDerecha, image=desarrollador_nicole_imagen)

# Configuración con grid
desarrollador_daniel.grid(row=0, column=0, padx=5, pady=5)
desarrollador_samuel.grid(row=0, column=1, padx=5, pady=5)
desarrollador_jhogert.grid(row=1, column=0, padx=5, pady=5)
desarrollador_sebastian.grid(row=1, column=1, padx=5, pady=5)
desarrollador_nicole.grid(row=2, column=0, padx=5, pady=5)

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
menu1.add_command(label="Salir",command=salir)

menu2.add_command(label="Gestión de Reservas",command=gReserva)
menu2.add_command(label="Gestión de Pedidos",command=gPedido)
menu2.add_command(label="Gestión de Empleados",command=gEmpleado)
menu2.add_command(label="Gestión de Inventario",command=gInventario)
menu2.add_command(label="Gestión Financiera",command=gFinanciera)

menu3.add_command(label="Acerca de",command=ayuda)


# Ocultar ventana principal
ventanaPrincipal.withdraw()

# Configuracion de menu ayuda
ventanaInicio.mainloop()