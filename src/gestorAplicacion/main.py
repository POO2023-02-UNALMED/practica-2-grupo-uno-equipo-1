from tkinter import *
from PIL import Image, ImageTk

def salir():
    ventanaprincipal.destroy()

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

ventanaprincipal = Tk()
ventanaprincipal.title("Sistema de Gestión de Restaurante")
ventanaprincipal.geometry("800x600")

frameIzquierdo = Frame(ventanaprincipal, highlightthickness=2)
frameDerecho = Frame(ventanaprincipal, highlightthickness=2)
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

# agregar el texto a la etiqueta
saludoBienvenida.insert(END, "Bienvenido al Sistema de Gestión de Restaurante, Esta aplicacion esta diseñada para que puedas llevar toda la gestion de tu restaurante como administrador, reservas, pedidos, empleados y materiales")
saludoBienvenida.config(state="disabled")

# Posicionamiento de la etiqueta de bienvenida
saludoBienvenida.pack(padx=10, pady=10)

imagenesIzquierda = Frame(frameIzquierdo, highlightthickness=2)
imagenesIzquierda.pack(side="right", padx=10, pady=10)

# Dimensiones de las imágenes


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

logoLeQuaso = Image.open("src\logo_leQuaso.png")
localLeQuaso = Image.open("src\local_leQuaso.png")
especialidad1 = Image.open("src\boeufbourguinon.png")
especialidad2 = Image.open("src\coqauvin.png")
especialidad3 = Image.open("src\ratatoulile.png")

# Redimensionamiento de las imágenes
logoLeQuaso = logoLeQuaso.resize((200, 200))
localLeQuaso = localLeQuaso.resize((200, 200))
especialidad1 = especialidad1.resize((200, 200))
especialidad2 = especialidad2.resize((200, 200))
especialidad3 = especialidad3.resize((200, 200))

# Creación de PhotoImage desde las imágenes redimensionadas
logoLeQuaso_imagen = ImageTk.PhotoImage(logoLeQuaso)
localLeQuaso_imagen = ImageTk.PhotoImage(localLeQuaso)
especialidad1_imagen = ImageTk.PhotoImage(especialidad1)
especialidad2_imagen = ImageTk.PhotoImage(especialidad2)
especialidad3_imagen = ImageTk.PhotoImage(especialidad3)

# Etiquetas de las imágenes
logoLeQuaso = Label(imagenesIzquierda, image=logoLeQuaso_imagen)
localLeQuaso = Label(imagenesIzquierda, image=localLeQuaso_imagen)
especialidad1 = Label(imagenesIzquierda, image=especialidad1_imagen)
especialidad2 = Label(imagenesIzquierda, image=especialidad2_imagen)
especialidad3 = Label(imagenesIzquierda, image=especialidad3_imagen)

Image


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


menuPrincipal = Menu(ventanaprincipal)
ventanaprincipal.config(menu=menuPrincipal)

menuInicio = Menu(menuPrincipal)
menuPrincipal.add_cascade(label="Inicio", menu=menuInicio)
menuInicio.add_command(label="Salir", command=salir)
menuInicio.add_command(label="Descripcion", command=ver_descripcion)

ventanaprincipal.mainloop()