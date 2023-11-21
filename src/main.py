from tkinter import *
from tkinter import messagebox, ttk
#import keyboard
from PIL import Image, ImageTk
from gestorAplicacion.Personas.empleado import Empleado
from gestorAplicacion.Personas.persona import Persona
from gestorAplicacion.Personas.cliente import Cliente
from gestorAplicacion.Personas.cocinero import Cocinero
from gestorAplicacion.Personas.domiciliario import Domiciliario
from gestorAplicacion.Personas.mesero import Mesero
from gestorAplicacion.Restaurante.financia import Financia
from gestorAplicacion.Restaurante.material import Material, Tipo
from gestorAplicacion.Restaurante.mesa import Mesa
from gestorAplicacion.Restaurante.pedido import Pedido
from gestorAplicacion.Restaurante.plato import Plato
from gestorAplicacion.Restaurante.reserva import Reserva
from gestorAplicacion.Restaurante.restaurante import Restaurante
from gestorAplicacion.Restaurante.turno import Turno, TipoTurno
from baseDatos.Serializacion import serializar,deserializar


restaurante=deserializar()
"""for material in restaurante.getInventario():
    print(material)
    print(restaurante.inventario[material].getCantidad())
    print(restaurante.inventario[material].getPrecioUnitario())

print(restaurante.getNombre())
for mesa in restaurante.getMesas():
    print(mesa)"""

#Crear un objeto Financia
financia = Financia(restaurante)


"""
restaurante.comprarMaterial(Tipo.RES, 100, 100,None)
restaurante.comprarMaterial(Tipo.ESPECIAS, 100, 50,None)
restaurante.comprarMaterial(Tipo.ACEITES, 100, 100,None)
restaurante.comprarMaterial(Tipo.POLLOS, 100, 200,None)
restaurante.comprarMaterial(Tipo.VINOS, 100, 300,None)
restaurante.comprarMaterial(Tipo.CEBOLLAS, 100, 50,None)
restaurante.comprarMaterial(Tipo.CHAMPINONES, 500, 100,None)
restaurante.comprarMaterial(Tipo.AJOS, 100, 30,None)
restaurante.comprarMaterial(Tipo.TOMATES, 400, 200,None)
restaurante.comprarMaterial(Tipo.QUESOS, 300, 150,None)
restaurante.comprarMaterial(Tipo.CERDOS, 100, 200,None)
restaurante.comprarMaterial(Tipo.ATUN, 100, 250,None)
restaurante.comprarMaterial(Tipo.PANES, 200, 50,None)
restaurante.comprarMaterial(Tipo.PAPAS ,200 ,100,None)
restaurante.comprarMaterial(Tipo.HUEVOS ,200 ,100,None)
restaurante.comprarMaterial(Tipo.PESCADOS ,200 ,300,None)
restaurante.comprarMaterial(Tipo.CUCHARAS,300,10,None)
restaurante.comprarMaterial(Tipo.TENEDORES,300,10,None)
restaurante.comprarMaterial(Tipo.PLATOS,200,35,None)
restaurante.comprarMaterial(Tipo.VASOS,150,25,None)"""
#restaurante.comprarMaterial(Tipo.RES,13,100,None)

# res = Material(Tipo.RES, 100, 100)
# especias = Material(Tipo.ESPECIAS, 100, 50)
# aceites = Material(Tipo.ACEITES, 100, 100)
# pollos = Material(Tipo.POLLOS, 100, 200)
# vinos = Material(Tipo.VINOS, 100, 300)
# cebollas = Material(Tipo.CEBOLLAS, 100, 50)
# champinones = Material(Tipo.CHAMPINONES, 500, 100)
# ajos = Material(Tipo.AJOS, 100, 30)
# tomates = Material(Tipo.TOMATES, 400, 200)
# quesos = Material(Tipo.QUESOS, 300, 150)
# cerdos = Material(Tipo.CERDOS, 100, 200)
# atun = Material(Tipo.ATUN, 100, 250)
# panes = Material(Tipo.PANES, 200, 50)
# pescados = Material(Tipo.PESCADOS ,200 ,300 )
# papas = Material(Tipo.PAPAS ,200 ,100 )
# huevos = Material(Tipo.HUEVOS ,200 ,100)
# cucharas=Material(Tipo.CUCHARAS,300,10)
# tenedores=Material(Tipo.TENEDORES,300,10)
# platos=Material(Tipo.PLATOS,200,35)
# vasos=Material(Tipo.VASOS,150,25)


# # Crear ingredientes de cada plato
# Muton = {res: 1, especias: 10, aceites: 1}
# coq = {pollos: 1, vinos: 1, cebollas: 1, champinones: 5, ajos: 1}
# ratatouille = {champinones: 5, tomates: 4, aceites: 1, ajos: 2}
# boeuf = {res: 1, vinos: 1, cebollas: 1, champinones: 5, ajos: 1}
# quiche = {huevos: 3, quesos: 3, cerdos: 1}
# salade = {huevos: 3, tomates: 3, atun: 1, cebollas: 2, aceites: 1}
# soupe = {cebollas: 5, panes: 2, quesos: 3}
# croque = {panes: 2, cerdos: 1, quesos: 1}
# bouilla = {pescados: 2, tomates: 2, ajos: 2, aceites: 1}
# tartiflette = {papas: 2, cebollas: 2, cerdos: 1, quesos: 1}

# # Crear menu de restaurante
# menu = [
#     Plato("Muton Shot", 30000, 30, "Costillas de Res con Salsa especial", Muton, ),
#     Plato("Coq au Vin", 45000, 25,  "Guiso de Pollo cocido en Vino y Verduras", coq),
#     Plato("Rat a Toulile", 15000, 20, "Verduras asadas en aceite de oliva", ratatouille),
#     Plato("Boeuf Bourguignon", 60000,  30, "Guiso de Res cocido en Vino y Verduras",boeuf),
#     Plato("Quiche Lorraine", 30000, 35, "Pastel salado con cerdo", quiche),
#     Plato("Salade Nicoise", 15000, 10, "Ensalada con Huevo y Atun", salade),
#     Plato("Soupe a l'oignon", 20000, 25, "Sopa espesa de Cebolla", soupe),
#     Plato("Croque Monsieur", 15000, 25, "Sandwich con Cerdo y Queso", croque),
#     Plato("Bouillabaisse", 20000, 25, "Sopa de Pescado tradicional", bouilla),
#     Plato("Tartiflette", 40000, 20, "Gratinado de Papa y Cerdo", tartiflette)
#     ]
# restaurante.setMenu(menu)

# #Crear turnos
# turno1 = Turno(TipoTurno.SEMANA, 5.0, 50000)
# turno2 = Turno(TipoTurno.SEMANA, 8.0, 60000)
# turno3 = Turno(TipoTurno.SEMANA, 2.0, 70000)
# turno4 = Turno(TipoTurno.SEMANA, 8.0, 55000)
# turno5 = Turno(TipoTurno.SEMANA, 2.0, 65000)
# turno6 = Turno(TipoTurno.SEMANA, 8.0, 75000)
# turno7 = Turno(TipoTurno.SEMANA, 2.0, 60000)
# turno8 = Turno(TipoTurno.SEMANA, 2.0, 70000)
# turno9 = Turno(TipoTurno.SEMANA, 8.0, 80000)
# turno10 = Turno(TipoTurno.SEMANA, 8.0, 65000)
# turno11 = Turno(TipoTurno.SEMANA, 3.0, 80000)
# turno12 = Turno(TipoTurno.SABADO, 7.0, 50000)
# turno13 = Turno(TipoTurno.SABADO, 3.0, 60000)
# turno14 = Turno(TipoTurno.SEMANA, 7.0, 70000)
# turno15 = Turno(TipoTurno.SEMANA, 2.0, 55000)
# turno16 = Turno(TipoTurno.SEMANA, 3.0, 55000)
# turno17 = Turno(TipoTurno.SEMANA, 2.0, 55000)

# #Crear empleados
# empleado1 = Mesero("Juan", 123456789, "mesero", restaurante, turno1)
# empleado1.agregarTurno(turno2)
# restaurante.contratarEmpleado(empleado1)
# empleado2 = Cocinero("Fernando", 234567891, "cocinero", restaurante, turno2)
# empleado2.agregarTurno(turno3)
# restaurante.contratarEmpleado(empleado2)
# empleado3 = Domiciliario("Santiago", 345678912, "domiciliario", restaurante, turno4)
# empleado1.agregarTurno(turno5)
# restaurante.contratarEmpleado(empleado3)
# empleado4 = Mesero("Jhon", 123456789, "mesero", restaurante, turno6)
# empleado1.agregarTurno(turno7)
# restaurante.contratarEmpleado(empleado4)
# empleado5 = Cocinero("Moises", 234567891, "cocinero", restaurante, turno8)
# empleado2.agregarTurno(turno9)
# restaurante.contratarEmpleado(empleado5)
# empleado6 = Domiciliario("Rigo", 345678912, "domiciliario", restaurante, turno10)
# empleado6.agregarTurno(turno11)
# restaurante.contratarEmpleado(empleado6)
# empleado7 = Mesero("Brayan", 123456789, "mesero", restaurante, turno12)
# empleado1.agregarTurno(turno13)
# restaurante.contratarEmpleado(empleado7)
# empleado8 = Cocinero("Felipe", 234567891, "cocinero", restaurante, turno14)
# empleado2.agregarTurno(turno15)
# restaurante.contratarEmpleado(empleado8)
# empleado9 = Domiciliario("Martin", 345678912, "domiciliario", restaurante, turno16)
# empleado1.agregarTurno(turno17)
# restaurante.contratarEmpleado(empleado9)


#for mesa1 in restaurante.getMesas():
#    mesa1.anadirNumero(mesa1.getNumeroMesa())
#restaurante.borrarReservasViejas()



# funciones ventana de inicio
def salir():
    """
    Salir de la aplicacion
    """
    serializar(restaurante)
    exit()

def ver_descripcion():
    saludoBienvenida.config(state=NORMAL)
    saludoBienvenida.delete(1.0,END)
    saludoBienvenida.insert(END, "Esta aplicacion esta diseñada para que puedas llevar toda\nla gestion de tu restaurante como administrador\nreservas, pedidos, empleados y materiales")
    saludoBienvenida.config(state=DISABLED)

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
        # Añadir un retraso de 500 milisegundos antes de cambiar la imagen
        widget.after(500, actualizarImagen)

def actualizarImagen():
    global indice_imagen
    global imagen_mostrar

    indice_imagen = (indice_imagen + 1) % len(imagenesP5)
    imagen_mostrar.configure(image=imagenesP5[indice_imagen])
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
    delete_frames_ventana_principal()
    gestion_reservas = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    gestion_reservas_app = GestionReservasApp(gestion_reservas, restaurante)
    gestion_reservas.grid(row=1, column=0, sticky="nsew")
    gestion_reservas.pack_propagate(False)

def delete_frames_ventana_principal():
    for widget in ventanaPrincipal.winfo_children():
        if(isinstance(widget,Frame)):
            widget.destroy()

def gestion_pedidos():
    delete_frames_ventana_principal()
    gestion_pedidos = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    gestion_pedidos_app = GestionPedidosApp(gestion_pedidos)
    gestion_pedidos.grid(row=1, column=0, sticky="nsew")
    gestion_pedidos.pack_propagate(False)

# (NO BORRAR) 
# def añadir_pedido():
#     frameAñadirPedido = Frame(padx=20, pady=20, bg="gray77")
#     frameAñadirPedido.pack(row = 0, column = 0, sticky = "nsew")
#     GestionEmpleados(ventanaPrincipal)
    # framePedidos = Frame(ventanaPrincipal)
    # framePedidos.grid(row=0, column=0, sticky="nsew")
    # saludoPedidos = Label(framePedidos, text="Gestion de pedidos")
    # saludoPedidos.grid(row=1, column=1, padx=10, pady=10)

    # frameAñadirPedido = Frame(framePedidos)
    # frameAñadirPedido.grid(row=2, column=0)
    # tituloPlato = Label(frameAñadirPedido, text="Plato")
    # # Creacion para hacer un pedido
    # tituloPedido = Label(frameAñadirPedido, text="Añadir pedido")
    # ListboxPlatos = Listbox(frameAñadirPedido)
    # tituloPedido.grid(row=0, column=0)
    # tituloPlato.grid(row=0, column=1)


    # for plato in menu:
    #     index = menu.index(plato)
    #     item = f"{index+1}. {plato.getNombre()} - {plato.getPrecio()} - {plato.getDescripcion()} - {plato.getTiempoPreparacion()} - {plato.getIngredientes()}"
    #     ListboxPlatos.insert(END, item)

    # ListboxPlatos.grid(row=1, column=3)

    # consulta1 = FieldFrame(frameAñadirPedido, "Platos" , ["platos"], "Platos deseados", [], [True])


def gEmpleado():
    pass

def gInventario():

    #Elimina los frames aparte de inventario

    delete_frames_ventana_principal()

    #crea un frame para la gestion de inventario

    gestion_inv = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")

    #crea un objeto gestionInventarioApp que se encarga de configurar el frame dentro del frame de inventario

    gestion_inv_app = GestionInventarioApp(gestion_inv,imagen_mat,restaurante)

    #Ubica el frame de inventario

    gestion_inv.grid(row=1, column=0, sticky="nsew")

    #Evita que el frame se ponga al lado otro frame

    gestion_inv.pack_propagate(False)

def gFinanciera():
    delete_frames_ventana_principal()
    gestion_financiera = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    gestion_financiera_app = GestionFinancieraApp(gestion_financiera,imagen_mat, restaurante)
    gestion_financiera.grid(row=1, column=0, sticky="nsew")
    gestion_financiera.pack_propagate(False)

def ayuda():
    opcion=messagebox.showinfo("Autores la aplicación","Daniel Garzón\n Samuel Ortiz\n Jhogert Bita\n Sebastian Hoyos\n Nicole Guaranguay")


# Creacion de ventana de inicio
ventanaInicio = Tk()
ventanaInicio.title("Sistema de Gestión de Restaurante Le Quaso")
ventanaInicio.geometry("800x600")
ventanaInicio.resizable(False,False)


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
logoLeQuaso = Image.open("src\imagenes\logo_leQuaso.png")
localLeQuaso = Image.open("src\imagenes\local_leQuaso.png")
especialidad1 = Image.open("src\imagenes\especialidad1.png")
especialidad2 = Image.open("src\imagenes\especialidad2.png")
especialidad3 = Image.open("src\imagenes\especialidad3.png")

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
    "Nombre: Daniel Felipe Garzon Acosta\nFecha de Nacimiento: 25 de Septiembre de 2005\nPasatiempos: Videojuegos y ver series",
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
imagen_daniel1 = Image.open("src\imagenes\imagen_daniel1.png")
imagen_daniel2 = Image.open("src\imagenes\imagen_daniel2.png")
imagen_daniel3 = Image.open("src\imagenes\imagen_daniel3.png")
imagen_daniel4 = Image.open("src\imagenes\imagen_daniel4.png")

imagen_samuel1 = Image.open("src\imagenes\imagen_samuel1.png")
imagen_samuel2 = Image.open("src\imagenes\imagen_samuel2.png")
imagen_samuel3 = Image.open("src\imagenes\imagen_samuel3.png")
imagen_samuel4 = Image.open("src\imagenes\imagen_samuel4.png")

imagen_jhogert1 = Image.open("src\imagenes\imagen_jhogert1.png")
imagen_jhogert2 = Image.open("src\imagenes\imagen_jhogert2.png")
imagen_jhogert3 = Image.open("src\imagenes\imagen_jhogert3.png")
imagen_jhogert4 = Image.open("src\imagenes\imagen_jhogert4.png")

imagen_sebastian1 = Image.open("src\imagenes\imagen_sebastian1.jpeg")
imagen_sebastian2 = Image.open("src\imagenes\imagen_sebastian2.jpeg")
imagen_sebastian3 = Image.open("src\imagenes\imagen_sebastian3.jpeg")
imagen_sebastian4 = Image.open("src\imagenes\imagen_sebastian4.jpeg")

imagen_nicole1 = Image.open("src\imagenes\imagen_nicole1.png")
imagen_nicole2 = Image.open("src\imagenes\imagen_nicole2.png")
imagen_nicole3 = Image.open("src\imagenes\imagen_nicole3.png")
imagen_nicole4 = Image.open("src\imagenes\imagen_nicole4.png")


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

ancho_receta, alto_receta = 30, 30

# Rutas de las imágenes
muton_shot = Image.open("src\imagenes\muton_shot.png")
coq_au_vin = Image.open("src\imagenes\coq_au_vin.png")
rat_a_toulile = Image.open("src\imagenes\\rat_a_toulile.png")
boeuf_bourguignon = Image.open("src\imagenes\imagen_burginon.png")
quiche_lorraine = Image.open("src\imagenes\quiche_lorraine.png")
salade_nicoise = Image.open("src\imagenes\salade_nicoise.png")
soupe_a_loignon = Image.open("src\imagenes\soupe_a_loignon.png")
croque_monsieur = Image.open("src\imagenes\croque_monsieur.png")
bouillabaisse = Image.open("src\imagenes\imagen_bullabaise.png")
tartiflette = Image.open("src\imagenes\imagen_tartiflete.png")

# Redimensionamiento de las imágenes
muton_shot = muton_shot.resize((ancho_receta, alto_receta))
coq_au_vin = coq_au_vin.resize((ancho_receta, alto_receta))
rat_a_toulile = rat_a_toulile.resize((ancho_receta, alto_receta))
boeuf_bourguignon = boeuf_bourguignon.resize((ancho_receta, alto_receta))
quiche_lorraine = quiche_lorraine.resize((ancho_receta, alto_receta))
salade_nicoise = salade_nicoise.resize((ancho_receta, alto_receta))
soupe_a_loignon = soupe_a_loignon.resize((ancho_receta, alto_receta))
croque_monsieur = croque_monsieur.resize((ancho_receta, alto_receta))
bouillabaisse = bouillabaisse.resize((ancho_receta, alto_receta))
tartiflette = tartiflette.resize((ancho_receta, alto_receta))

# Leer imagenes de recetas
muton_shot_imagen = ImageTk.PhotoImage(muton_shot)
coq_au_vin_imagen = ImageTk.PhotoImage(coq_au_vin)
rat_a_toulile_imagen = ImageTk.PhotoImage(rat_a_toulile)
boeuf_bourguignon_imagen = ImageTk.PhotoImage(boeuf_bourguignon)
quiche_lorraine_imagen = ImageTk.PhotoImage(quiche_lorraine)
salade_nicoise_imagen = ImageTk.PhotoImage(salade_nicoise)
soupe_a_loignon_imagen = ImageTk.PhotoImage(soupe_a_loignon)
croque_monsieur_imagen = ImageTk.PhotoImage(croque_monsieur)
bouillabaisse_imagen = ImageTk.PhotoImage(bouillabaisse)
tartiflette_imagen = ImageTk.PhotoImage(tartiflette)

# Crear lista de imagenes de recetas
imagenes_recetas = [
    muton_shot_imagen,
    coq_au_vin_imagen,
    rat_a_toulile_imagen,
    boeuf_bourguignon_imagen,
    quiche_lorraine_imagen,
    salade_nicoise_imagen,
    soupe_a_loignon_imagen,
    croque_monsieur_imagen,
    bouillabaisse_imagen,
    tartiflette_imagen
]

# Rutas de las imágenes  FINANCIA
tomates = Image.open("src\\imagenes\\tomate.jpg")
cebollas = Image.open("src\\imagenes\\cebolla-roja-1.jpg")
papas = Image.open("src\\imagenes\\papaa.jpg")
aceites = Image.open("src\\imagenes\\aceite.jpg")
vinos = Image.open("src\\imagenes\\vino.jpg")
quesos = Image.open("src\\imagenes\\queso.jpg")
champiñones = Image.open("src\\imagenes\\champiñones.jpg")
res = Image.open("src\\imagenes\\res.jpg")
pescados = Image.open("src\\imagenes\\pescado.jpg")
cerdos = Image.open("src\\imagenes\\cerdo.jpg")
pollos = Image.open("src\\imagenes\\pollo.jpg")
panes = Image.open("src\\imagenes\\pan.jpg")
ajos = Image.open("src\\imagenes\\ajos.jpg")
especies = Image.open("src\\imagenes\\especies.jpg")
huevos = Image.open("src\\imagenes\\huevo.jpg")
atun = Image.open("src\\imagenes\\atun.jpg")
cuchara = Image.open("src\\imagenes\\cuchara.jpg")
tenedores = Image.open("src\\imagenes\\tenedores.jpg")
plato = Image.open("src\\imagenes\\plato.jpg")
vasos = Image.open("src\\imagenes\\vasos.jpg")

# Redimensionamiento de las imágenes  FINANCIA

tomates = tomates.resize((ancho_receta, alto_receta))
cebollas = cebollas.resize((ancho_receta, alto_receta))
papas = papas.resize((ancho_receta, alto_receta))
aceites = aceites.resize((ancho_receta, alto_receta))
vinos = vinos.resize((ancho_receta, alto_receta))
quesos = quesos.resize((ancho_receta, alto_receta))
champiñones = champiñones.resize((ancho_receta, alto_receta))
res = res.resize((ancho_receta, alto_receta))
pescados = pescados.resize((ancho_receta, alto_receta))
cerdos = cerdos.resize((ancho_receta, alto_receta))
pollos = pollos.resize((ancho_receta, alto_receta))
panes = panes.resize((ancho_receta, alto_receta))
ajos = ajos.resize((ancho_receta, alto_receta))
especies = especies.resize((ancho_receta, alto_receta))
huevos = huevos.resize((ancho_receta, alto_receta))
atun = atun.resize((ancho_receta, alto_receta))
cuchara = cuchara.resize((ancho_receta, alto_receta))
tenedores = tenedores.resize((ancho_receta, alto_receta))
plato = plato.resize((ancho_receta, alto_receta))
vasos = vasos.resize((ancho_receta, alto_receta))

# Leer imagenes de FINANCIA

tomates_imagen = ImageTk.PhotoImage(tomates)
cebollas_imagen = ImageTk.PhotoImage(cebollas)
papas_imagen = ImageTk.PhotoImage(papas)
aceites_imagen = ImageTk.PhotoImage(aceites)
vinos_imagen = ImageTk.PhotoImage(vinos)
quesos_imagen = ImageTk.PhotoImage(quesos)
champiñones_imagen = ImageTk.PhotoImage(champiñones)
res_imagen = ImageTk.PhotoImage(res)
pescados_imagen = ImageTk.PhotoImage(pescados)
cerdos_imagen = ImageTk.PhotoImage(cerdos)
pollos_imagen = ImageTk.PhotoImage(pollos)
panes_imagen = ImageTk.PhotoImage(panes)
ajos_imagen = ImageTk.PhotoImage(ajos)
especies_imagen = ImageTk.PhotoImage(especies)
huevos_imagen = ImageTk.PhotoImage(huevos)
atun_imagen = ImageTk.PhotoImage(atun)
cuchara_imagen = ImageTk.PhotoImage(cuchara)
tenedores_imagen = ImageTk.PhotoImage(tenedores)
plato_imagen = ImageTk.PhotoImage(plato)
vasos_imagen = ImageTk.PhotoImage(vasos)

# Crear lista de imagenes de FINANCIAS
imagenes_materiales = [
    tomates_imagen, 
    cebollas_imagen, 
    papas_imagen, 
    aceites_imagen, 
    vinos_imagen, 
    quesos_imagen, 
    champiñones_imagen, 
    res_imagen, 
    pescados_imagen, 
    cerdos_imagen, 
    pollos_imagen, 
    panes_imagen, 
    ajos_imagen, 
    especies_imagen, 
    huevos_imagen, 
    atun_imagen,
    cuchara_imagen,
    tenedores_imagen,
    plato_imagen,
    vasos_imagen
]

# imagen_mat={
#     Tipo.TOMATES:{"imagen": tomates_imagen, "cantidad": restaurante.inventario[Tipo.TOMATES].getCantidad(), "precio unitario": restaurante.inventario[Tipo.TOMATES].getPrecioUnitario()},
#     Tipo.CEBOLLAS:{"imagen": cebollas_imagen, "cantidad": restaurante.inventario[Tipo.CEBOLLAS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.CEBOLLAS].getPrecioUnitario()},
#     Tipo.PAPAS:{"imagen": papas_imagen, "cantidad": restaurante.inventario[Tipo.PAPAS].getCantidad(),"precio unitario": restaurante.inventario[Tipo.PAPAS].getPrecioUnitario()},
#     Tipo.ACEITES:{"imagen": aceites_imagen, "cantidad": restaurante.inventario[Tipo.ACEITES].getCantidad(),"precio unitario": restaurante.inventario[Tipo.ACEITES].getPrecioUnitario()},
#     Tipo.VINOS:{"imagen": vinos_imagen, "cantidad": restaurante.inventario[Tipo.VINOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.VINOS].getPrecioUnitario()},
#     Tipo.QUESOS:{"imagen": quesos_imagen, "cantidad": restaurante.inventario[Tipo.QUESOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.QUESOS].getPrecioUnitario()},
#     Tipo.CHAMPINONES:{"imagen":champiñones_imagen, "cantidad": restaurante.inventario[Tipo.CHAMPINONES].getCantidad(), "precio unitario": restaurante.inventario[Tipo.CHAMPINONES].getPrecioUnitario()},
#     Tipo.RES:{"imagen": res_imagen, "cantidad": restaurante.inventario[Tipo.RES].getCantidad(), "precio unitario": restaurante.inventario[Tipo.RES].getPrecioUnitario()},
#     Tipo.PESCADOS:{"imagen": pescados_imagen, "cantidad": restaurante.inventario[Tipo.PESCADOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.PESCADOS].getPrecioUnitario()},
#     Tipo.CERDOS:{"imagen": cerdos_imagen, "cantidad": restaurante.inventario[Tipo.CERDOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.CERDOS].getPrecioUnitario()},
#     Tipo.POLLOS:{"imagen": pollos_imagen, "cantidad": restaurante.inventario[Tipo.POLLOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.POLLOS].getPrecioUnitario()},
#     Tipo.PANES:{"imagen": panes_imagen, "cantidad": restaurante.inventario[Tipo.PANES].getCantidad(), "precio unitario": restaurante.inventario[Tipo.PANES].getPrecioUnitario()},
#     Tipo.AJOS:{"imagen":ajos_imagen, "cantidad": restaurante.inventario[Tipo.AJOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.AJOS].getPrecioUnitario()},
#     Tipo.ESPECIAS:{"imagen": especies_imagen, "cantidad": restaurante.inventario[Tipo.ESPECIAS].getCantidad(),"precio unitario": restaurante.inventario[Tipo.ESPECIAS].getPrecioUnitario()},
#     Tipo.HUEVOS:{"imagen": huevos_imagen, "cantidad": restaurante.inventario[Tipo.HUEVOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.HUEVOS].getPrecioUnitario()},
#     Tipo.ATUN:{"imagen": atun_imagen, "cantidad": restaurante.inventario[Tipo.ATUN].getCantidad(),"precio unitario": restaurante.inventario[Tipo.ATUN].getPrecioUnitario()},
#     Tipo.CUCHARAS:{"imagen": cuchara_imagen, "cantidad": restaurante.inventario[Tipo.CUCHARAS].getCantidad(),"precio unitario": restaurante.inventario[Tipo.CUCHARAS].getPrecioUnitario()},
#     Tipo.TENEDORES:{"imagen": tenedores_imagen, "cantidad": restaurante.inventario[Tipo.TENEDORES].getCantidad(),"precio unitario": restaurante.inventario[Tipo.TENEDORES].getPrecioUnitario()},
#     Tipo.PLATOS:{"imagen": plato_imagen, "cantidad": restaurante.inventario[Tipo.PLATOS].getCantidad(), "precio unitario": restaurante.inventario[Tipo.PLATOS].getPrecioUnitario()},
#     Tipo.VASOS:{"imagen": vasos_imagen, "cantidad": restaurante.inventario[Tipo.VASOS].getCantidad(),"precio unitario": restaurante.inventario[Tipo.VASOS].getPrecioUnitario()}
#     }

# Fieldframe para consultas

from tkinter import Frame, Label, Entry, Button, DISABLED, messagebox, E, W

class FieldFrame(Frame):
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None, consulta=None):
        super().__init__(master)
        self.nombre = ""
        self.labels = {}
        self.entries = {}
        self.dataform = {}
        self.consulta = consulta

        # Contenedor que tiene todo el formulario de la consulta
        frameForm = Frame(self, bg="#c3c3c3", borderwidth=1, relief="solid")
        frameForm.grid(padx=5, pady=5)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Títulos
        label_criterios = Label(frameForm, text=tituloCriterios)
        label_criterios.grid(row=0, column=0, padx=5, pady=5, sticky=E)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        label_valores = Label(frameForm, text=tituloValores)
        label_valores.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        frameForm.grid_rowconfigure(0, weight=1)
        frameForm.grid_columnconfigure(0, weight=1)

        # Crear etiquetas y entradas dinámicamente
        for i, criterio in enumerate(criterios, start=1):
            label = Label(frameForm, text=criterio)
            label.grid(row=i, column=0, padx=5, pady=5, sticky=E)
            frameForm.grid_rowconfigure(i, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)

            self.labels[criterio] = label

            entry = Entry(frameForm)
            entry.grid(row=i, column=1, padx=5, pady=5, sticky=W)
            frameForm.grid_rowconfigure(i, weight=1)
            frameForm.grid_columnconfigure(0, weight=1)

            self.entries[criterio] = entry

            if habilitado and (not habilitado[i - 1] or habilitado[i - 1] is None):
                entry.configure(state="disabled")

            if valores and valores[i - 1] is not None:
                entry.insert(0, valores[i - 1])

        # Botones
        self.boton_aceptar = Button(frameForm, text="Aceptar", command=self.guardar_datos)
        self.boton_aceptar.grid(row=i + 1, column=0, columnspan=2, pady=10)

        self.boton_borrar = Button(frameForm, text="Borrar", command=self.borrar_campos)
        self.boton_borrar.grid(row=i + 2, column=0, columnspan=2, pady=10)
    #funcion que se activa cuando le das a Aceptar, se encarga de verificar que todos los campos del FieldFrame esten llenos y dependiendo del nombre del
    #FielFrame se ejecuta una logica distinta
    def guardar_datos(self):
        for criterio, entry in self.entries.items():
            valor = entry.get()
            estado = entry.cget("state")
            if not valor and estado != "disabled":
                messagebox.showwarning("Advertencia", f"Campo '{criterio}' no puede estar vacío.")
                return  # Si un campo está vacío, mostrar advertencia y salir
            if valor or estado == "disabled":
                self.dataform[criterio] = valor

        # Omitir la siguiente línea para evitar la impresión de None
        # print(self.dataform)


        if self.consulta is not None:
            if GestionPedidosApp.plato_seleccionado == False:
                messagebox.showinfo("Alerta", "Debes presionar al menos un plato antes de continuar.")
            else:
                valores = self.dataform
                self.consulta(valores)
        else:
            mensaje = ""
            for criterio, entry in self.entries.items():
                mensaje += f"{criterio}: {entry.get()}\n"
            messagebox.showinfo("Operación exitosa", mensaje)
            if self.nombre == "mesa":
                numeroMesa = self.get_valor_by_criterio("Mesa")
                capacidadMesa = self.get_valor_by_criterio("Capacidad")
                restaurante.listadoMesas.append(Mesa(capacidadMesa, numeroMesa))
            elif self.nombre == "comprar":
                tipo = self.get_valor_by_criterio("Material")
                tipos = getattr(Tipo, tipo.upper(), None)
                cantidad = int(self.get_valor_by_criterio("Cantidad"))
                precio = int(self.get_valor_by_criterio("Precio"))
                restaurante.comprarMaterial(tipos, cantidad, precio, None)
            elif self.nombre == "desechar":
                tipo = self.get_valor_by_criterio("Material")
                tipos = getattr(Tipo, tipo.upper(), None)
                cantidad = int(self.get_valor_by_criterio("Cantidad"))
                restaurante.botarMaterial(tipos, cantidad)
            elif self.nombre == "crear-reserva":
                cedula = self.get_valor_by_criterio("cedula")
                nombre = self.get_valor_by_criterio("nombre")
                numAsistentes = self.get_valor_by_criterio("numero de asistentes")
                diaReserva = self.get_valor_by_criterio("dia de la reserva")
                try:
                    Reserva.revisarFecha(diaReserva)
                    restaurante.asignarReservaCliente(cedula, nombre, numAsistentes, diaReserva)
                except ValueError:
                    messagebox.showinfo("Alerta", "formato de fecha ingresado no válido")
            elif self.nombre == "cancelar-reserva":
                cedula = self.get_valor_by_criterio("cedula")
                if (restaurante.verificarCliente(cedula)):
                    messagebox.showinfo("Alerta", "El cliente no se encuentra afiliado al restaurante")
                else:
                    restaurante.obtenerCliente(cedula).setReserva(None)
                    messagebox.showinfo("éxito", "Reserva cancelada")
            elif self.nombre == "confirmar-reserva":
                cedula = self.get_valor_by_criterio("cedula")
                numMesa = self.get_valor_by_criterio("numero de mesa")
                if (restaurante.verificarCliente(cedula)):
                    messagebox.showinfo("Alerta", "El cliente no se encuentra afiliado al restaurante, por lo que no tiene una reserva")
                else:
                    if not (restaurante.mesasQueCumplen(cedula) == "No hay mesas válidas para esa reserva"):
                        messagebox.showinfo("Alerta", restaurante.confirmarReserva(numMesa, cedula))

        for criterio, entry in self.entries.items():
            if entry.winfo_exists():
                entry.config(state="disabled")

    #Funcion que se encarga de obtener el valor asociado al un criterio del FieldFrame
    def get_valor_by_criterio(self, criterio):
        return self.dataform.get(criterio)
    #Funcion encargada de borrar la informacion dentro de los entry del FieldFrame
    def borrar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, END)

    def getValues(self):
        self.dataform

    #Metodo encargado de ingresar un valor asociado a un criterio, su uso se nota en el combobox de mas abajo
    def insertar_valor(self, criterio, valor):
        entry = self.entries.get(criterio)
        if entry:
            entry.delete(0, END)
            entry.insert(0, valor)


class ImageFrame(Frame):
    def __init__(self, master, image_paths):
        super().__init__(master)
        self.image_paths = image_paths
        self.current_index = 0

        self.label = Label(self)
        self.label.pack(padx=10, pady=10)

        # Cargar la primera imagen al inicio
        self.load_image()

        # Asociar la función al evento de clic
        self.label.bind("<Button-1>", self.next_image)

    def load_image(self):
        image_path = self.image_paths[self.current_index]
        img = Image.open(image_path)
        img = img.resize((300, 300), Image.ANTIALIAS)  # Ajustar el tamaño según sea necesario
        photo = ImageTk.PhotoImage(img)

        # Actualizar la imagen en el Label
        self.label.config(image=photo)
        self.label.image = photo

    def next_image(self, event):
        # Cambiar a la siguiente imagen al hacer clic
        self.current_index = (self.current_index + 1) % len(self.image_paths)
        self.load_image()


class GestionPedidosApp:
    """
    Aqui se plantea toda la funcionalidad de gestion de pedidos
    """
    plato_seleccionado=False
    def __init__(self, framePadre):
        self.row_height = 200
        self.col_width = 200
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

        # Menu verificado
        menu_verificado = restaurante.verificarMenu(restaurante.getMenu())

        for i, plato in enumerate(menu_verificado):
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
        
        # Saludo inicial
        titulo_bienvenida = Label(self.frame_home, text="¡Bienvenido a la gestión de pedidos!", font=("Bold", 15))
        titulo_bienvenida.place(relx=0.5, rely=0.1, anchor="center")

        # Título de la funcionalidad
        titulo_funcionalidad = Label(self.frame_home, text="Funcionalidad de Gestión de Pedidos", font=("Bold", 12))
        titulo_funcionalidad.place(relx=0.5, rely=0.25, anchor="center")

        # Descripción de la funcionalidad
        descripcion_funcionalidad = Label(self.frame_home, text="Esta plataforma te permite realizar un seguimiento detallado de tus pedidos. En crear pedidos se ajusta a tus necesidades según los materiales que tengas; de acuerdo con esto, se te mostrarán los pedidos que puedes agregar. Con respecto a los empleados, podrás ver según los datos de tu pedido los empleados capacitados para realizar la tarea.", wraplength=400, justify="left")
        descripcion_funcionalidad.place(relx=0.5, rely=0.4, anchor="center")

        # Otros elementos y configuraciones de la página de inicio...

        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_domicilio(self):
        # Definir frame domicilio
        self.frame_domicilio = Frame(self.main_frame, width=400, height=600)
        titulo_domicilios = Label(self.frame_domicilio, text="Pedidos hechos para consumo domicilio", font=("Bold", 15))
        titulo_domicilios.pack(pady=10)

        # Crear un Canvas y un Scrollbar dentro del frame_domicilio
        canvas = Canvas(self.frame_domicilio)
        scrollbar = Scrollbar(self.frame_domicilio, orient="vertical", command=canvas.yview)

        # Crear un Frame principal dentro del Canvas
        main_frame = Frame(canvas)

        # Añadir el Frame principal al Canvas
        canvas.create_window((0, 0), window=main_frame, anchor='nw')

        pedidos_domicilio = restaurante.getPedidosDomicilio()

        # Comprobar si la lista de pedidos_domicilio está vacía
        if not pedidos_domicilio:
            mensaje_vacio = Label(main_frame, text="Hola, aquí puedes visualizar los pedidos que se han hecho en Le Quasó. Agrega pedidos para poder visualizarlos", font=("Bold", 12), wraplength=400, justify="center")
            mensaje_vacio.pack(pady=10)
        else:
            # Añadir un Frame para cada objeto al Frame principal
            for i, objeto in enumerate(pedidos_domicilio):
                frame = Frame(main_frame, bd=2, relief="solid")  # Añadir borde al Frame
                frame.grid(row=i, column=0, pady=5, sticky="ew")  # Usar grid en lugar de pack
                label = Label(frame, text=objeto)
                label.pack(fill=BOTH, expand=1)

        # Configurar el Scrollbar para que se desplace con el Canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Configurar el Canvas para que cambie de tamaño con el Frame principal
        main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Empaquetar el Canvas y el Scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Frame de interacción
        self.frame_domicilio.grid(pady=5, padx=5)
        self.frame_domicilio.pack_propagate(False)


        # Frame de interacción
        self.frame_domicilio.grid(pady=5, padx=5)
        self.frame_domicilio.pack_propagate(False)



    def function_frame_restaurante(self):
        self.frame_restaurante = Frame(self.main_frame, width=400, height=600)
        self.frame_restaurante.grid(pady=5, padx=5)
        self.frame_restaurante.pack_propagate(False)

        titulo_restaurante = Label(self.frame_restaurante, text="Pedidos hechos para consumo restaurante", font=("Bold", 15))
        titulo_restaurante.pack(pady=10)

        # Crear un Canvas y un Scrollbar dentro del frame_restaurante
        canvas = Canvas(self.frame_restaurante)
        scrollbar = Scrollbar(self.frame_restaurante, orient="vertical", command=canvas.yview)

        # Crear un Frame principal dentro del Canvas
        main_frame = Frame(canvas)

        # Añadir el Frame principal al Canvas
        canvas.create_window((0, 0), window=main_frame, anchor='nw')

        # Añadir un Frame para cada objeto al Frame principal (cambia esto según tus necesidades)
        pedidos_restaurante = restaurante.getPedidosRestaurante()
        for i, objeto in enumerate(pedidos_restaurante):
            frame = Frame(main_frame, bd=2, relief="solid")  # Añadir borde al Frame
            frame.grid(row=i, column=0, pady=5, sticky="ew")  # Usar grid en lugar de pack
            label = Label(frame, text=objeto)
            label.pack(fill=BOTH, expand=1)

        # Comprobar si la lista de pedidos_restaurante está vacía
        if not pedidos_restaurante:
            mensaje_vacio = Label(main_frame, text="Hola, aquí puedes visualizar los pedidos que se han hecho en Le Quasó. Agrega pedidos para poder visualizarlos", font=("Bold", 12), wraplength=400, justify="center")
            mensaje_vacio.pack(pady=10)

        # Configurar el Scrollbar para que se desplace con el Canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Configurar el Canvas para que cambie de tamaño con el Frame principal
        main_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Empaquetar el Canvas y el Scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Frame de interacción
        self.frame_restaurante.grid(pady=5, padx=5)
        self.frame_restaurante.pack_propagate(False)


    
    def insertar_opcion_tipo_pedido(self,event):
        opcion_seleccionada = self.combo.get()
        self.busquedadPlatos.insertar_valor("tipo pedido", opcion_seleccionada)

    def function_frame_pedidos(self):
        # Definir frame pedidos
        self.frame_pedidos = Frame(self.main_frame, width=500, height=400)
        # Título de frame pedidos
        # self.titulo_pedidos = Label(self.frame_pedidos, text="Pedidos", font=("Bold", 15)).place(x=150, y=30)

        # Frame de interacción
        self.frameSeleccionPlatos = Frame(self.frame_pedidos, width=500, height=400)
        self.busquedadPlatos = FieldFrame(self.frameSeleccionPlatos, "platos y tipo pedido", ["tipo pedido"], "presione los platos y ingrese tipo pedido", [], [True], self.seleccionarCocinero)
        self.busquedadPlatos.grid(row = 0, column=0, padx=10, pady=10)

        tipoConsumo = ["restaurante","domicilio"]
        valorDefecto=StringVar(value="Seleccione tipo consumo")

        self.combo=ttk.Combobox(self.frameSeleccionPlatos,values=tipoConsumo,textvariable=valorDefecto)

        self.combo.bind("<<ComboboxSelected>>",self.insertar_opcion_tipo_pedido)
        self.combo.grid(row=0,column=1,pady=20,sticky="new")

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
        if self.platos_seleccionados.count(indice) == 0:
            # Si no está seleccionado, agregarlo a la lista
            self.platos_seleccionados.append(indice)
            GestionPedidosApp.plato_seleccionado=True
        elif indice in self.platos_seleccionados:
            # Si ya está seleccionado, quitarlo de la lista
            self.platos_seleccionados.remove(indice)
        
    def insertar_opcion_cocinero(self,event):
        opcion_seleccionada = self.combo.get()
        self.frameResultadosCocinero.insertar_valor("cocinero", opcion_seleccionada)

    def seleccionarCocinero(self, valores):
        # Obtener el tipo de pedido
        tipo_pedido = valores["tipo pedido"]

        # Destruir el canvas existente
        self.canvas.destroy()
        self.frameSeleccionPlatos.destroy()

        # Filtrar los platos seleccionados
        for i in self.platos_seleccionados:
            self.platos_temp.append(restaurante.getMenu()[i-1])
        
        self.pedido["platos"] = self.platos_temp
        self.pedido["tipo pedido"] = tipo_pedido

        # Se guardan los platos
        # no se esta usando 
        # # Obtener los platos seleccionados
        # index_platos_escogidos = valores["platos"].split()


        #Seleccionar cocineros
        cocineros_sin_filtrar = restaurante.clasificarEmpleados(restaurante.getEmpleados(), "cocinero")
        cocineros = restaurante.verificarCocineros(restaurante.getEmpleados(), self.platos_temp)

        # Lista de cocineros (corregir la clave 'idenrificacion' a 'identificacion')
        self.cocineros = []

        for i, cocinero in enumerate(cocineros):
            cocinero_dict= {
                "nombre": cocinero.getNombre(),
                "identificacion": cocinero.getCedula(),
                "puesto": cocinero.getPuesto(),
            }
            self.cocineros.append(cocinero_dict)

        self.cocineros_names=[]

        for cocinero in cocineros:
            self.cocineros_names.append(cocinero.getNombre())

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

            cocineroSelec = self.cocineros_names
            valorDefecto=StringVar(value="Seleccione su cocinero")

            self.combo=ttk.Combobox(self.seleccionarCocineroFrame,values=cocineroSelec,textvariable=valorDefecto)

            self.combo.bind("<<ComboboxSelected>>",self.insertar_opcion_cocinero)
            self.combo.grid(row=0,column=1,pady=20,sticky="new")

            # Crear un Canvas para mostrar los cocineros
            self.canvascocineros = Canvas( self.seleccionarCocineroFrame)
            self.frames_temporales.append(self.canvascocineros)
            
            # Colocar el Canvas en el grid
            self.canvascocineros.grid(row=1, column=0, padx=10, pady=10)

            # Colocar el Frame de selección del cocinero en el grid
            self.seleccionarCocineroFrame.grid(row=0, column=0)

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
            
            cocineroSelec = self.cocineros_names
            valorDefecto=StringVar(value="Seleccione su cocinero")

            self.combo=ttk.Combobox(self.seleccionarCocineroFrame,values=cocineroSelec,textvariable=valorDefecto)

            self.combo.bind("<<ComboboxSelected>>",self.insertar_opcion_cocinero)
            self.combo.grid(row=0,column=1,pady=20,sticky="new")

            # Crear un Canvas para mostrar los cocineros
            self.canvascocineros = Canvas( self.seleccionarCocineroFrame)
            # Colocar el Canvas en el grid
            self.canvascocineros.grid(row=1, column=0, padx=10, pady=10)
            self.frames_temporales.append(self.canvascocineros)

            # Colocar el Frame de selección del cocinero en el grid
            self.seleccionarCocineroFrame.grid(row=0, column=0)

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
    
    def insertar_opcion_cocinero(self,event):
        opcion_seleccionada = self.combo.get()
        self.frameResultadosCocinero.insertar_valor("cocinero", opcion_seleccionada)

    def insertar_opcion_domiciliario(self,event):
        opcion_seleccionada = self.combo.get()
        self.frameResultadosDomiciliario.insertar_valor("domiciliario", opcion_seleccionada)
    
    def seleccionarDomiciliario(self, valores):
        self.seleccionarCocineroFrame.destroy()

        domiciliarios_sin_filtrar = restaurante.clasificarEmpleados(restaurante.getEmpleados(), "domiciliario")
        domiciliarios = restaurante.verificarDomiciliarios(restaurante.getEmpleados())

        name = (valores["cocinero"])
        cocinero = restaurante.buscarEmpleado(name , "cocinero")
        self.pedido["cocinero"] = cocinero

        # Lista de cocineros (corregir la clave 'idenrificacion' a 'identificacion')
        self.domiciliarios = []

        for i, domiciliario in enumerate(domiciliarios):
            domiciliario_dict= {
                "nombre": domiciliario.getNombre(),
                "identificacion": domiciliario.getCedula(),
                "puesto": domiciliario.getPuesto(),
            }
            self.domiciliarios.append(domiciliario_dict)
        
        self.domiciliarios_names = [ domiciliario.getNombre() for domiciliario in domiciliarios]

        self.frameSeleccionarDomiciliario = Frame(self.frame_pedidos, width=500, height=400)

        self.frameResultadosDomiciliario = FieldFrame( self.frameSeleccionarDomiciliario, "Domiciliario", ["domiciliario"], "ingrese el nombre del domiciliario", [], [True], self.crearPedido)
        self.frameResultadosDomiciliario.grid(padx=10, pady=10)

        domiciliarioSelec = self.domiciliarios_names
        valorDefecto = StringVar(value="Seleccione su cocinero")

        self.combo = ttk.Combobox(self.frameSeleccionarDomiciliario,values=domiciliarioSelec,textvariable=valorDefecto)

        self.combo.bind("<<ComboboxSelected>>",self.insertar_opcion_domiciliario)
        self.combo.grid(row=0,column=1,pady=20,sticky="new")

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
    
    def insertar_opcion_mesero(self, event):
        opcion_seleccionada = self.combo.get()
        self.frameResultadosMesero.insertar_valor("mesero", opcion_seleccionada)

    def seleccionarMesero(self, valores):
        self.seleccionarCocineroFrame.destroy()

        meseros_sin_filtrar = restaurante.clasificarEmpleados(restaurante.getEmpleados(), "domiciliario")
        meseros = restaurante.verificarMeseros(restaurante.getEmpleados())

        self.meseros = []

        for i, mesero in enumerate(meseros):
            mesero_dict= {
                "nombre": mesero.getNombre(),
                "identificacion": mesero.getCedula(),
                "puesto": mesero.getPuesto(),
            }
            self.meseros.append(mesero_dict)
        
        self.meseros_names = [ mesero.getNombre() for mesero in meseros]
            
        cocinero = restaurante.buscarEmpleado((valores["cocinero"]), "cocinero")
        self.pedido["cocinero"] = cocinero

        self.frameSeleccionarMesero = Frame(self.frame_pedidos, width=500, height=400)

        self.frameResultadosMesero = FieldFrame(self.frameSeleccionarMesero, "Mesero", ["mesero"], "ingrese el nombre del mesero", [], [True], self.detectarReserva)
        self.frameResultadosMesero.grid(padx=10, pady=10)

        meseroSelec = self.meseros_names
        valorDefecto = StringVar(value="Seleccione su mesero")

        self.combo=ttk.Combobox(self.frameSeleccionarMesero, values=meseroSelec, textvariable=valorDefecto)

        self.combo.bind("<<ComboboxSelected>>", self.insertar_opcion_mesero)
        self.combo.grid(row=0,column=1,pady=20,sticky="new")

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

        mesero = restaurante.buscarEmpleado(((valores["mesero"])), "mesero")
        self.pedido["mesero"] = mesero
        self.frameSeleccionarMesero.destroy()

        self.frameDetectarReserva = Frame(self.frame_pedidos, width=500, height=400)
        self.frameResultadosReserva = FieldFrame(self.frameDetectarReserva, "Datos de reserva", ["mesa", "dueño reserva"], "ingrese los datos de la reserva", [], [True, True], self.crearPedido)
        self.frameResultadosReserva.grid(padx=10, pady=10)
        self.frameDetectarReserva.grid(padx=10, pady=10)
    
    def crearPedido(self, valores):
        self.frameSeleccionPlatos.destroy()
        GestionPedidosApp.plato_seleccionado=False
        if self.pedido["tipo pedido"] == "domicilio":

            self.frameSeleccionarDomiciliario.destroy()
            domiciliario = restaurante.buscarEmpleado(valores["domiciliario"], "domiciliario")
            self.pedido["domiciliario"] = domiciliario
            pedido2 = Pedido(self.platos_temp, None, self.pedido["tipo pedido"], self.pedido["cocinero"], None, restaurante, None, self.pedido["domiciliario"])
            pedido2.actualizarInventario(restaurante, pedido2)
            messagebox.showinfo("Operación exitosa", "Pedido creado")

        if self.pedido["tipo pedido"] == 'restaurante':
            self.frameDetectarReserva.destroy()
            numMesa = valores["mesa"]
            dueñoReserva = valores["dueño reserva"]
            reserva = restaurante.encontrarReserva(numMesa, dueñoReserva)
            mesaTemporal = restaurante.encontrarMesa(numMesa)
            if reserva == None:
                messagebox.showinfo("Operación exitosa", "Pedido creado")
                pedido1 = Pedido(self.platos_temp, mesaTemporal, self.pedido["tipo pedido"], self.pedido["cocinero"], self.pedido["mesero"], restaurante, None, None)
                pedido1.actualizarInventario(restaurante, pedido1)
                try:
                    pedido1.verificarPedido(restaurante, pedido1)
                except:
                    pass

            if reserva != None:
                  messagebox.showinfo("Operación exitosa", "Pedido creado")
                  nombre1 = reserva.getDuenoReserva().getNombre()
                  pedido1 = Pedido(self.platos_temp, reserva.getMesa(), self.pedido["tipo pedido"], self.pedido["cocinero"], self.pedido["mesero"], restaurante, reserva, None)				      
                  pedido1.setVerificado(True)
                  pedido1.actualizarInventario(restaurante, pedido1)


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
class GestionInventarioApp:
    """
    Aqui se plantea la funcionalidad de gestion de inventario
    """
    def __init__(self,framePadre,imagen_mat,restaurante):

        self.row_height = 300
        self.col_width = 300
        self.restaurante=restaurante
        self.imagen_mat=imagen_mat
        self.frames_temporales=[]
        self.framePadre=framePadre
        
        #En este frame se gestionara toda la funcionalidad
        self.funcionalidad_gestionInv = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionInv.grid(row=0, column=0, sticky="nsew")
        #En este frame se desplegaran los botones encargados de cambiar el frame de cada funcion
        self.options_frame = Frame(self.funcionalidad_gestionInv, bg='#c3c3c3', width=120, height=500)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        #Evita que los frames se pongan uno al lado del otro
        self.options_frame.pack_propagate(False)

        #En este frame se iran intercambiando los frames de cada funcion
        self.main_frame = Frame(self.funcionalidad_gestionInv,
                                highlightbackground='black',
                                highlightthickness=2,
                                width=500,
                                height=400)
        #Botones de las opciones
        self.btn_home_page = Button(self.options_frame, text="Inicio", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_home_page, self.home_indicate))
        self.btn_home_page.grid(row=0, column=0, padx=0, pady=30)

        self.btn_consultar_inventario = Button(self.options_frame, text="Consultar\n Inventario", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='#158aff', command = lambda : self.indicador(self.function_frame_consultar_inventario, self.indicate_consultar_inventario))
        self.btn_consultar_inventario.grid(row=1, column=0, padx=0, pady=30)

        self.btn_comprar_mat = Button(self.options_frame, text="Comprar\n Materiales", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_comprar_mat, self.indicate_comprar_mat))
        self.btn_comprar_mat.grid(row=2, column=0, padx=0, pady=30)

        self.btn_desechar_mat = Button(self.options_frame, text="Desechar\n Materiales", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_desechar_mat, self.indicate_desechar_mat))
        self.btn_desechar_mat.grid(row=3, column=0, padx=0, pady=30)

        self.btn_comprar_mesa=Button(self.options_frame,text="Comprar\n Mesas",font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command= lambda :self.indicador(self.function_frame_comprar_mesa,self.indicate_comprar_mesa))
        self.btn_comprar_mesa.grid(row=4,column=0,padx=0,pady=30)

        #Indicadores de los botones
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=5, y=30, width=5, height=40, )

        self.indicate_consultar_inventario = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultar_inventario.place(x=5, y=135, width=5, height=40, )

        self.indicate_comprar_mat = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_comprar_mat.place(x=5, y=255, width=5, height=40, )

        self.indicate_desechar_mat = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_desechar_mat.place(x=5, y=375, width=5, height=40, )

        self.indicate_comprar_mesa=Label(self.options_frame,text="",bg='#c3c3c3')
        self.indicate_comprar_mesa.place(x=5,y=495,width=5,height=40,)


        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)


    #Funcion encargada de cambiar al frame de inicio donde se le dara la bienvenida a la gestion de la funcionalidad

    def function_home_page(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la gestion de Inventario", font=("Bold", 15)).place(x=100, y=30)
        descripcionInv="Con esta funcionalidad puedes consultar los materiales que hayan en tu inventario\nComprar o desechar los mismo y finalmente añadir mesas al restaurante\nde manera rápida y sencilla"
        Label(self.frame_home,text=descripcionInv,font=("Bond",10)).place(x=10,y=150)
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    #Funcion encargada de cambiar al frame que se encarga de mostrar los materiales del inventario y su cantidad

    def function_frame_consultar_inventario(self):
        self.frame_inventario = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_inventario, text="Inventario", font=("Bold", 15)).place(x=150, y=30)
        self.frame_inventario.grid(row=0,column=1,pady=5, padx=5)
        self.frame_inventario.pack_propagate(False)
        #Canvas para crear un frame temporal que se encarga de desplegar las imagenes
        self.canvas = Canvas(self.frame_inventario)
        self.canvas.grid(row = 1, column=0, padx=10, pady=10)
        self.frames_temporales.append(self.canvas)
        #configurar las columnas para las imagenes
        columnas=4
        #contadores para la configuracion de columnas y filas del grid
        fil=0
        col=0
        #El primer parametro el el Tipo de cada material mientras que el segundo parametro es el diccionario asociado al Tipo el cual
        #tiene como elementos 2 diccionarios a los cuales se les asocia la imagen del material y la cantidad de este
        for tipo,dato in imagen_mat.items():

            fila=fil//columnas
            columna=col%columnas

            imagen=dato["imagen"]
            cantidad=dato["cantidad"]
            #se crea un frame para cada material
            frame=Frame(self.canvas,width=self.col_width,height=self.row_height,bd=2,relief=RIDGE)
            frame.grid(row=fila,column=columna,padx=5,pady=5)

            boton=Button(frame,image=imagen)
            boton.grid(row=0,column=0,padx=5,pady=5)

            label=Label(frame,text=f"{tipo.value}")
            label.grid(row=0,column=1,padx=5,pady=5)

            label2=Label(frame,text=f"{cantidad}")
            label2.grid(row=1,column=1,padx=5,pady=5)

            fil+=1
            col+=1
    #Metodos para hacer que una opcion elejida de un combobox se tome como el dato en el entry de un campo del FieldFrame
    def insertar_opcion(self,event):
            opcion_seleccionada = self.combo.get()
            self.ff_desechar.insertar_valor("Material", opcion_seleccionada)

    def insertar_opcion2(self,event):
            opcion_seleccionada = self.combo.get()
            self.ff_comprar.insertar_valor("Material", opcion_seleccionada)
    #Funcion encargada de cambiar al frame de comprar materiales

    def function_frame_comprar_mat(self):

        # Definir frame de comprar materiales
        self.frame_comprar_mat = Frame(self.main_frame, width=500, height=400)
        self.frame_comprar_mat.grid(pady=10,padx=10)

        # Frame de interacción
        self.frameFFcomprar = Frame(self.frame_comprar_mat, width=500, height=400)
        #Se crea un FieldFrame en el cual se pide el tipo de material, la cantidad a comprar y a que precio
        self.ff_comprar = FieldFrame(self.frameFFcomprar, "Criterio", ["Material", "Cantidad","Precio"], "Valor", [], [True, True,True])
        self.ff_comprar.grid(row = 0, column=0, padx=10, pady=10)
        #se le da un nombre al FieldFrame para poder utilizar la logica especifica de esta funcion
        self.ff_comprar.nombre="comprar"
        #Se crea un combobox de los materiales para facilitar la visualizacion de los materiales presentes en el inventario
        materiales=["TOMATES", "CEBOLLAS", "PAPAS", "ACEITES", "VINOS","QUESOS",
        "CHAMPINONES", "RES", "PESCADOS", "CERDOS","POLLOS", "PANES", "AJOS", "ESPECIAS", "HUEVOS",
        "ATUN", "CUCHARAS", "TENEDORES", "PLATOS", "VASOS"]
        valorDefecto=StringVar(value="Seleccione Material")
        #configuracion del combobox
        self.combo=ttk.Combobox(self.frameFFcomprar,values=materiales,textvariable=valorDefecto)
        #asignacion del evento del combobox en el cual se usa la funcion que le asigna el valor seleccionado del combobox al campo de "Material"
        self.combo.bind("<<ComboboxSelected>>",self.insertar_opcion2)
        self.combo.grid(row=0,column=1,pady=20,sticky="new")
        # Crear un Canvas para la cuadrícula dentro del Frame principal
        self.canvas = Canvas(self.frame_comprar_mat)
        self.canvas.grid(row = 1, column=0, padx=10, pady=10)

        self.frames_temporales.append(self.canvas)

        # Ubicación del frame de FieldFrame dentro del frame de interaccion mediante grid
        self.frameFFcomprar.grid(row=0, column=0)

    #funcion encargada de cambiar al frame de desechar materiales
    def function_frame_desechar_mat(self):

        # Definir frame desechar mat
        self.frame_desechar_mat = Frame(self.main_frame, width=500, height=400)
        self.frame_desechar_mat.grid(pady=10,padx=10)

        # Frame de interacción
        self.frameFFdesdechar = Frame(self.frame_desechar_mat, width=500, height=400)
        self.ff_desechar = FieldFrame(self.frameFFdesdechar, "Criterio", ["Material", "Cantidad"], "Valor", [], [True, True])
        self.ff_desechar.grid(row = 0, column=0, padx=10, pady=10)
        #nombre para usar logica especifica desde FieldFrame
        self.ff_desechar.nombre="desechar"
        #Se crea un combobox de los materiales para facilitar la visualizacion de los materiales presentes en el inventario
        materiales=["TOMATES", "CEBOLLAS", "PAPAS", "ACEITES", "VINOS","QUESOS",
        "CHAMPINONES", "RES", "PESCADOS", "CERDOS","POLLOS", "PANES", "AJOS", "ESPECIAS", "HUEVOS",
        "ATUN", "CUCHARAS", "TENEDORES", "PLATOS", "VASOS"]
        valorDefecto=StringVar(value="Seleccione Material")
        #configuracion del combobox
        self.combo=ttk.Combobox(self.frameFFdesdechar,values=materiales,textvariable=valorDefecto)
        #asignacion del evento del combobox en el cual se usa la funcion que le asigna el valor seleccionado del combobox al campo de "Material"
        self.combo.bind("<<ComboboxSelected>>",self.insertar_opcion)
        self.combo.grid(row=0,column=1,pady=20,sticky="new")
        # Crear un Canvas para la cuadrícula dentro del Frame principal
        self.canvas = Canvas(self.frame_desechar_mat)
        self.canvas.grid(row = 1, column=0, padx=10, pady=10)

        self.frames_temporales.append(self.canvas)

        # Ubicación del frame de FieldFrame dentro del frame de interaccion mediante grid
        self.frameFFdesdechar.grid(row=0, column=0)

    #funcion encargada de cambiar al frame para añadir mesas al restaurante
    def function_frame_comprar_mesa(self):
        #definir frame de comprar mesa
        self.frame_comprar_mesa=Frame(self.main_frame,width=500,height=400)
        self.frame_comprar_mesa.grid(pady=10,padx=10)
        #Frame de interaccion
        self.frameFFmesa=Frame(self.frame_comprar_mesa,width=500,height=400)
        self.ff_mesa=FieldFrame(self.frameFFmesa,"Criterio",["Mesa","Capacidad"],"Valor",[],[True,True])
        self.ff_mesa.grid(row=0,column=0,padx=10,pady=10)
        #nombre para usar logica especifica desde FieldFrame
        self.ff_mesa.nombre="mesa"

        self.canvas=Canvas(self.frame_comprar_mesa)
        self.canvas.grid(row=1,column=0,padx=10,pady=10)
        self.frames_temporales.append(self.canvas)
        #ubicacion del FieldFrame dentro del frame de interaccion mediante grid
        self.frameFFmesa.grid(row=0,column=0)
    def delete_pages(self):
        """
        Esta se hace para borrar los frames actuales 
        y evitar que se superpongan los frames,
        para que solo se muestre el frame indicado
        dentro de la funcionalidad
        """
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    #funcion encargada de ocultar los indicadores laterales de los botones de las opciones que no han sido seleccionados
    def hide_indicators(self):
        self.home_indicate.config(bg='#c3c3c3')
        self.indicate_consultar_inventario.config(bg='#c3c3c3')
        self.indicate_comprar_mat.config(bg='#c3c3c3')
        self.indicate_desechar_mat.config(bg='#c3c3c3')
        self.indicate_comprar_mesa.config(bg='#c3c3c3')

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

import tkinter as tkk
class GestionFinancieraApp:
    """
    Aqui se plantea toda la funcionalidad de gestion Financiera
    """
    def __init__(self, framePadre,imagen_mat, restaurante):
        self.row_height = 200
        self.col_width = 200
        self.imagen_mat=imagen_mat
        self.restaurante = restaurante
        self.financia = Financia(restaurante)
        self.empleados = self.restaurante.listadoEmpleados  
        self.frames_temporales = []
        self.material_seleccionado = None
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

        self.btn_consultar_ganancias = Button(self.options_frame, text="Ganancias", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_ganancias, self.indicate_consultarGanancias))
        self.btn_consultar_ganancias.grid(row=2, column=0, padx=0, pady=30)

        self.btn_consultar_gastos = Button(self.options_frame, text="Gastos Totales", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gastos, self.indicate_consultarGastos))
        self.btn_consultar_gastos.grid(row=3, column=0, padx=0, pady=30)

        self.btn_consultar_gastosMaterialEspecifico = Button(self.options_frame, text="Gastos Material\n Especifico", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_gastos_material_especifico, self.indicate_consultarGastosMaterial))
        self.btn_consultar_gastosMaterialEspecifico.grid(row=4, column=0, padx=0, pady=30)

        self.btn_consultar_pagoEmpleadoEspecifico = Button(self.options_frame, text="Pago Empleado\n Especifico", font=('Bold', 15), bd = 0, bg ='#c3c3c3',fg='#158aff', command = lambda : self.indicador(self.function_frame_pago_empleado_especifico, self.indicate_consultarEmpleado))
        self.btn_consultar_pagoEmpleadoEspecifico.grid(row=5, column=0, padx=0, pady=30)

        # Crear indicadores de opción seleccionada
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=0, y=30, width=5, height=30, )

        self.indicate_consultarPresupuesto = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarPresupuesto.place(x=0, y=130, width=5, height=30, )
        
        self.indicate_consultarGanancias = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGanancias.place(x=0, y=220, width=5, height=30, )

        self.indicate_consultarGastos = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGastos.place(x=0, y=320, width=5, height=30, )

        self.indicate_consultarGastosMaterial = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarGastosMaterial.place(x=0, y=420, width=5, height=30, )

        self.indicate_consultarEmpleado = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_consultarEmpleado.place(x=0, y=540, width=5, height=30, )

        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_inicio(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        # Saludo inicial
        titulo_bienvenida = Label(self.frame_home, text="¡Bienvenido a la gestión Financiera!", font=("Bold", 15))
        titulo_bienvenida.place(relx=0.5, rely=0.1, anchor="center")

        # Título de la funcionalidad
        titulo_funcionalidad = Label(self.frame_home, text="Funcionalidad de Gestión de Financia", font=("Bold", 12))
        titulo_funcionalidad.place(relx=0.5, rely=0.25, anchor="center")

        # Descripción de la funcionalidad
        descripcion_funcionalidad = Label(self.frame_home, text="Esta plataforma te permite consultar el presupuesto total que tiene el restaurante, depedendiendo de las ganancias que el lugar genere, se calculara a traves de la ganancia bruta, la cual necesitara conocer los gastos totales del restaurante, como el abastecimiento del inventario y el pago total de los empleados; gracias a la Ganancia bruta se podra calcular la ganancia Neta que dira cuanto fue el lucro que genero como tal el restaurante.", wraplength=400, justify="left")
        descripcion_funcionalidad.place(relx=0.5, rely=0.5, anchor="center")
        
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_presupuesto(self):
        self.frame_presupuesto = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_presupuesto, text="Presupuesto", font=("Bold", 15)).place(x=300, y=30)
        self.frame_presupuesto.grid(pady=5, padx=5)
        self.frame_presupuesto.pack_propagate(False)

        # Calcular los Ganancias Netas
        presupuesto = self.financia.getPresupuesto()
        self.lbl_presupuesto = Label(self.frame_presupuesto, text=f"El Presupuesto del restaurante es: {presupuesto}", font=("Arial", 15) )
        self.lbl_presupuesto.grid(row=2, column=0, pady=300, padx=200)

    def function_frame_ganancias(self):
        self.frame_ganancias = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_ganancias, text="Ganancias", font=("Bold", 15)).place(x=200, y=30)
        self.frame_ganancias.grid(pady=5, padx=5)
        self.frame_ganancias.pack_propagate(False)
   
        # Crear el Label para las Ganancias Netas
        self.label_ganancias_netas = Label(self.frame_ganancias, text="Ganancias Netas: ", font=('Bold', 15))

        # Botón para las Ganancias Netas
        btn_ganancias_netas = Button(self.frame_ganancias, text="Ganancias Netas", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='black', command=self.function_ganancias_netas)
        btn_ganancias_netas.place(x=50, y=100)

        # Botón para las Ganancias Brutas
        btn_ganancias_Brutas = Button(self.frame_ganancias, text="Ganancias Brutas", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='black', command=self.function_ganancias_brutas)
        btn_ganancias_Brutas.place(x=300, y=100)


    def function_ganancias_netas(self):
         # Calcular los Ganancias Netas
        ganancias_netas = self.financia.getGananciasNetas()
        self.lbl_ganancias_netas = Label(self.frame_ganancias, text=f"Las Gananacias Nestas del restaurante son: {ganancias_netas}", font=("Arial", 15) )
        self.lbl_ganancias_netas.grid(row=2, column=0, pady=300, padx=200)


    def function_ganancias_brutas(self):
        # Calcular los Ganancias Brutas
        ganancias_brutas = self.financia.getGananciasBrutas()
        self.lbl_ganancias_brutas = Label(self.frame_ganancias, text=f"Las Gananacias Brutas del restaurante son: {ganancias_brutas}", font=("Arial", 15) )
        self.lbl_ganancias_brutas.grid(row=2, column=0, pady=300, padx=200)

    def function_frame_gastos(self):
        self.frame_gastos = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_gastos, text="Gastos Totales", font=("Bold", 15)).place(x=200, y=30)
        self.frame_gastos.grid(pady=5, padx=5)
        self.frame_gastos.pack_propagate(False)

        # Botón para las Gastos Materiales
        btn_gastos_Materiales = Button(self.frame_gastos, text="Gastos Materiales", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='black', command=self.function_gastos_materiales)
        btn_gastos_Materiales.place(x=50, y=100)

        # Botón para los Pagos Empleados
        btn_pagos_empleados = Button(self.frame_gastos, text="Pagos Empleados", font=('Bold', 15), bg ='#c3c3c3', bd = 0, fg='black', command=self.function_pagos_empleados)
        btn_pagos_empleados.place(x=300, y=100)

    def function_gastos_materiales(self):
        # Calcular los gastos de materiales
        gastos_materiales = self.financia.getGastosMateriales()
        self.lbl_gastos_materiales = Label(self.frame_gastos, text=f"Gasto total del inventario del restaurante es: {gastos_materiales}", font=("Arial", 15) )
        self.lbl_gastos_materiales.grid(row=2, column=0, pady=300, padx=200)

    def function_pagos_empleados(self):
        # Obtener el valor de los pagos a empleados
        pagos_empleados = self.financia.getPagosEmpleados()  
        self.lbl_pagos_empleados = Label(self.frame_gastos, text=f"Pago total de los Empleados del restaurante es: {pagos_empleados}", font=("Arial", 15) )
        self.lbl_pagos_empleados.grid(row=2, column=0, pady=300, padx=200)
        

    
    def function_frame_gastos_material_especifico(self):
        self.frame_gastos_material= Frame(self.main_frame, width=1000, height=800)
        Label(self.frame_gastos_material, text="Gastos Material Especifico", font=("Bold", 15)).grid(row=0, column=0, padx=150, pady=30)
        self.frame_gastos_material.grid(row=0,column=1,pady=5, padx=5)
        self.frame_gastos_material.pack_propagate(False)
        self.canvas = Canvas(self.frame_gastos_material)
        self.canvas.grid(row = 1, column=0, padx=15, pady=15)
        self.frames_temporales.append(self.canvas)
        Label(self.frame_gastos_material, text="SELECCIONE LA FOTO DEL MATERIAL :", font=("Bold", 10)).grid(row=1, column=4, padx=50, pady=80)

        # Agregar una barra de entrada (Entry)
        self.material_entry = Entry(self.frame_gastos_material)
        self.material_entry.grid(row=1, column=5, padx=50, pady=100)
        
        #configurar lista
        columnas=4
        filas=len(self.imagen_mat)//columnas+1
        fil=0
        col=0
        for tipo,dato in imagen_mat.items():

            fila=fil//columnas
            columna=col%columnas

            imagen=dato["imagen"]
            cantidad=dato["cantidad"]
            preciounitario= dato["precio unitario"]


            frame=Frame(self.canvas,width=self.col_width,height=self.row_height,bd=2,relief=RIDGE)
            frame.grid(row=fila,column=columna,padx=5,pady=5)

            boton=Button(frame, image=imagen, command=lambda tipo=tipo: self.escribir_material(tipo))
            boton.grid(row=2,column=0,padx=5,pady=5)

            label=Label(frame,text=f"{tipo.value}")
            label.grid(row=2,column=1,padx=5,pady=5)

            label2=Label(frame,text=f"CantidadTotal: {cantidad}")
            label2.grid(row=3,column=1,padx=5,pady=5)

            label3=Label(frame,text=f"PrecioUnitario: {preciounitario}")
            label3.grid(row=4,column=1,padx=5,pady=5)

            fil+=1
            col+=1
    def escribir_material(self, tipo):
        # Escribir el tipo de material en la barra de entrada
        self.material_entry.delete(0, END)  # Borrar cualquier texto existente
        self.material_entry.insert(0, tipo.value)
        self.material_seleccionado = tipo.value
        self.mostrar_gasto_material()
    def mostrar_gasto_material(self):
        valor_gasto = self.financia.gastoMaterialEspecifico(self.material_seleccionado)

        # Ahora, imprime este valor en algún lugar de tu interfaz
        resultado_label = Label(self.frame_gastos_material, text=f"Gasto del material seleccionado: {valor_gasto}")
        resultado_label.grid(row=6, column=0, padx=5, pady=5)

    def function_frame_pago_empleado_especifico(self):
        self.frame_gastos_material_especifico = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_gastos_material_especifico, text="Pago Empleado Especifico", font=("Bold", 15)).place(x=150, y=30)
        
        # Obtener la lista de empleados del restaurante
        lista_empleados = [empleado.getNombre() for empleado in self.empleados]

        # Crear una etiqueta para el texto
        label = Label(self.main_frame, text="Seleccione el empleado:")
        label.grid(row=0, column=0)  # Ubicar la etiqueta en la fila 0, columna 0

        # Crear el Combobox
        combobox = ttk.Combobox(self.main_frame, values=lista_empleados)
        combobox.grid(row=0, column=1)  # Ubicar el combobox en la fila 0, columna 1

        # Ubicación frame pago_empleado_especifico
        self.main_frame.grid(pady=5, padx=5)
        self.main_frame.pack_propagate(False)
    def pagar_empleado_seleccionado(self):
        empleado_seleccionado = combobox.get()
        if empleado_seleccionado:
            pago = self.financia.pagoempleadoespecifico(específico)
            messagebox.showinfo( f"Pagar a el empleado {empleado_seleccionado}: {pago}")
        else:
            messagebox.showwarning("Error", "Por favor, selecciona un empleado.")


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

from tkinter import scrolledtext
class GestionReservasApp:
    """
    Aqui se plantea toda la funcionalidad de gestion de reservas
    """
    def __init__(self, framePadre, restaurante):
        self.row_height = 200
        self.col_width = 200
        self.restaurante = restaurante
        self.frames_temporales = []
        self.framePadre = framePadre
        self.funcionalidad_gestionReservas = Frame(self.framePadre, bg='#c3c3c3', width=100, height=500)
        self.funcionalidad_gestionReservas.grid(row=0, column=0, sticky="nsew")
        self.options_frame = Frame(self.funcionalidad_gestionReservas, bg='#c3c3c3', width=120, height=500)
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
        btn_cancelar_reservas.grid(row=4, column=0, padx=0, pady=30)

        btn_asignar_mesas = Button(self.options_frame, text="confirmar\nreservas", font=('Bold', 15), fg='#158aff', bd = 0, bg ='#c3c3c3',command = lambda : self.indicador(self.function_frame_confirmar_R, self.indicate_confirmar))
        btn_asignar_mesas.grid(row=5, column=0, padx=0, pady=30)

        # Crear indicadores de opción seleccionada
        self.home_indicate = Label(self.options_frame, text="", bg='#c3c3c3')
        self.home_indicate.place(x=0, y=30, width=5, height=40, )

        self.indicate_reservas_NC = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_reservas_NC.place(x=0, y=135, width=5, height=40, )
        
        self.indicate_RESERVAS_C = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_RESERVAS_C.place(x=0, y=255, width=5, height=40, )
        
        self.indicate_anadir_reservas = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_anadir_reservas.place(x=0, y=375, width=5, height=40, )

        self.indicate_cancelar_reservas = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_cancelar_reservas.place(x=0, y=375, width=5, height=40, )

        self.indicate_confirmar = Label(self.options_frame, text="", bg='#c3c3c3')
        self.indicate_confirmar.place(x=0, y=375, width=5, height=40, )

        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.pack_propagate(False)
        self.framePadre.grid_rowconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(0, weight=1)
        self.framePadre.grid_columnconfigure(1, weight=1)

    def function_home_page(self):
        self.frame_home = Frame(self.main_frame, width=500, height=400)
        Label(self.frame_home, text="Bienvenido a la gestion de reservas", font=("Bold", 15)).place(x=150, y=30)
        descripcion_funcionalidad = Label(self.frame_home, text="Esta plataforma te permite consultar, cancelar, crear y confirmar las reservas de tus clientes", wraplength=400, justify="left")
        descripcion_funcionalidad.place(relx=0.5, rely=0.4, anchor="center")
        self.frame_home.grid(pady=5, padx=5)
        self.frame_home.pack_propagate(False)

    def function_frame_RNC(self):
        self.frame_RNC = Frame(self.main_frame, width=500, height=400)
        self.frame_RNC.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")
        Label(self.frame_RNC, text="Reservas sin mesa asignada", font=("Bold", 15)).grid(row=0, column=0, padx=10, pady=10)
        self.texto = scrolledtext.ScrolledText(self.frame_RNC, wrap="word", width=100, height=30)
        self.texto.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")     
        self.texto.insert(END, self.restaurante.imprimirReservas())

    def function_frame_RC(self):
        self.frame_RC = Frame(self.main_frame, width=500, height=400)
        self.frame_RC.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")
        Label(self.frame_RC, text="Reservas con mesa asignada", font=("Bold", 15)).grid(row=0, column=0, padx=10, pady=10)
        self.texto2 = scrolledtext.ScrolledText(self.frame_RC, wrap="word", width=100, height=30)
        self.texto2.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        self.texto2.insert(END, self.restaurante.imprimirReservas2())

    def function_frame_ANADIR_R(self):
        # Definir frame reservas
        self.frame_ANADIR_R = Frame(self.main_frame, width=500, height=400)
        self.frame_ANADIR_R.grid(pady=10,padx=10)
        # Frame de interacción
        self.frame_AR = Frame(self.frame_ANADIR_R, width=500, height=400)
        self.V_AR = FieldFrame(self.frame_AR, "información del reservista", ["cedula", "nombre", "numero de asistentes", "dia de la reserva"], "Ingresa la información", ["Ej: 1022142545", "", "", "En formato dia-mes-año"], [True, True, True, True])
        self.V_AR.nombre = "crear-reserva"
        self.V_AR.grid(row = 0, column=0, padx=10, pady=10)
        self.frame_ANADIR_R.grid(pady=5, padx=5)
        self.canvas = Canvas(self.frame_AR, width=500, height=400)
        self.canvas.grid(row = 1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_AR.grid(row=0, column=0, sticky="nsew")

    def function_frame_cancelar_R(self):
        self.frame_CANCELAR_R = Frame(self.main_frame, width=500, height=400)
        # Frame de interacción
        self.frame_CR = Frame(self.frame_CANCELAR_R, width=500, height=400)
        self.V_CR = FieldFrame(self.frame_CR, "información del reservista", ["cedula"], "Ingresa la información", ["Ej: 1022142545"], [True])
        self.V_CR.nombre = "cancelar-reserva"
        self.V_CR.grid(row = 0, column=0, padx=10, pady=10)
        self.frame_CANCELAR_R.grid(pady=5, padx=5)
        self.canvas2 = Canvas(self.frame_CR, width=500, height=400)
        self.canvas2.grid(row = 1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_CR.grid(row=0, column=0, sticky="nsew")

    def function_frame_confirmar_R(self):
        self.confirmar_R = Frame(self.main_frame, width=500, height=400)
        # Frame de interacción
        self.frame_re = Frame(self.confirmar_R, width=500, height=400)
        self.conf_R = FieldFrame(self.frame_re, "Información del reservista", ["cedula", "numero de mesa"], "Ingresa la información", [], [True, True])
        self.conf_R.nombre = "confirmar-reserva"
        self.conf_R.grid(row = 0, column=0, padx=10, pady=10)
        self.confirmar_R.grid(pady=5, padx=5)
        self.canvas3 = Canvas(self.frame_re, width=500, height=400)
        self.canvas3.grid(row = 1, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_re.grid(row=0, column=0, sticky="nsew")

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
        self.indicate_reservas_NC.config(bg='#c3c3c3')
        self.indicate_RESERVAS_C.config(bg='#c3c3c3')
        self.indicate_anadir_reservas.config(bg='#c3c3c3')
        self.indicate_cancelar_reservas.config(bg='#c3c3c3')
        self.indicate_confirmar.config(bg='#c3c3c3')

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

# res = Material("RES", 100, 100)
# especias = Material("ESPECIAS", 100, 50)
# aceites = Material("ACEITES", 100, 100)
# Muton = {res: 1, especias: 10, aceites: 1}
# mutonShot = Plato("Muton Shot",30000,"Costillas de Res con Salsa especial",30,Muton)
# menu = [mutonShot]

# framePedidos = Frame(ventanaPrincipal)
# framePedidos.pack(side="top", padx=10, pady=10)
# saludoPedidos = Label(framePedidos, text="Gestion de pedidos")
# saludoPedidos.grid(row=1, column=1)

# frameAñadirPedido = Frame(framePedidos)
# tituloPlato = Label(frameAñadirPedido, text="Plato")
# # Creacion para hacer un pedido
# tituloPedido = Label(frameAñadirPedido, text="Añadir pedido")
# ListboxPlatos = Listbox(frameAñadirPedido)
# tituloPedido.grid(row=0, column=0)
# tituloPlato.grid(row=0, column=1)

# for plato in menu:
#     ListboxPlatos.insert
#     (END,
#      f"{plato.getNombre()} - {plato.getPrecio()}"
#      f"- {plato.getDescripcion()} -"
#      f"{plato.getTiempoPreparacion()}"
#      f" - {plato.getIngredientes()} ")
#     ListboxPlatos.grid(row=1, column=0)

# consulta1 = FieldFrame("Platos" , ["platos"], "Platos deseados", [], [True])

menu2.add_command(label="Gestión de Reservas",command=gReserva)
menu2.add_command(label="Gestión de Pedidos",command=gestion_pedidos)
menu2.add_command(label="Gestión de Empleados",command=gEmpleado)
menu2.add_command(label="Gestión de Inventario",command=gInventario)
menu2.add_command(label="Gestión Financiera",command=gFinanciera)

menu3.add_command(label="Acerca de",command=ayuda)



# Ocultar ventana principal
ventanaPrincipal.withdraw()

# Configuracion de menu ayuda
ventanaInicio.mainloop()
