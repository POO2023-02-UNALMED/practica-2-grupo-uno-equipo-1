from tkinter import *
from tkinter import messagebox, font
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
from diseñoGráfico.GestionPedidosApp import GestionPedidosApp
from diseñoGráfico.GestionReservasApp import GestionReservasApp
from baseDatos.Serializacion import serializar,deserializar


restaurante=deserializar()
print(restaurante.getNombre())
for mesa in restaurante.getMesas():
    print(mesa)
for empleado in restaurante.getEmpleados():
    print(empleado)
#Crear un objeto Financia
financia = Financia(restaurante)
res = Material(Tipo.RES, 100, 100)
especias = Material(Tipo.ESPECIAS, 100, 50)
aceites = Material(Tipo.ACEITES, 100, 100)
pollos = Material(Tipo.POLLOS, 100, 200)
vinos = Material(Tipo.VINOS, 100, 300)
cebollas = Material(Tipo.CEBOLLAS, 100, 50)
champinones = Material(Tipo.CHAMPINONES, 500, 100)
ajos = Material(Tipo.AJOS, 100, 30)
tomates = Material(Tipo.TOMATES, 400, 200)
quesos = Material(Tipo.QUESOS, 300, 150)
cerdos = Material(Tipo.CERDOS, 100, 200)
atun = Material(Tipo.ATUN, 100, 250)
panes = Material(Tipo.PANES, 200, 50)
pescados = Material(Tipo.PESCADOS ,200 ,300 )
papas = Material(Tipo.PAPAS ,200 ,100 )
huevos = Material(Tipo.PAPAS ,200 ,100 )

# Crear ingredientes de cada plato
Muton = {res: 1, especias: 10, aceites: 1}
coq = {pollos: 1, vinos: 1, cebollas: 1, champinones: 5, ajos: 1}
ratatouille = {champinones: 5, tomates: 4, aceites: 1, ajos: 2}
boeuf = {res: 1, vinos: 1, cebollas: 1, champinones: 5, ajos: 1}
quiche = {huevos: 3, quesos: 3, cerdos: 1}
salade = {huevos: 3, tomates: 3, atun: 1, cebollas: 2, aceites: 1}
soupe = {cebollas: 5, panes: 2, quesos: 3}
croque = {panes: 2, cerdos: 1, quesos: 1}
bouilla = {pescados: 2, tomates: 2, ajos: 2, aceites: 1}
tartiflette = {papas: 2, cebollas: 2, cerdos: 1, quesos: 1}

# Crear menu de restaurante
menu = [
    Plato("Muton Shot", 30000, 30, "Costillas de Res con Salsa especial", Muton, ),
    Plato("Coq au Vin", 45000, 25,  "Guiso de Pollo cocido en Vino y Verduras", coq),
    Plato("Rat a Toulile", 15000, 20, "Verduras asadas en aceite de oliva", ratatouille),
    Plato("Boeuf Bourguignon", 60000,  30, "Guiso de Res cocido en Vino y Verduras",boeuf),
    Plato("Quiche Lorraine", 30000, 35, "Pastel salado con cerdo", quiche),
    Plato("Salade Nicoise", 15000, 10, "Ensalada con Huevo y Atun", salade),
    Plato("Soupe a l'oignon", 20000, 25, "Sopa espesa de Cebolla", soupe),
    Plato("Croque Monsieur", 15000, 25, "Sandwich con Cerdo y Queso", croque),
    Plato("Bouillabaisse", 20000, 25, "Sopa de Pescado tradicional", bouilla),
    Plato("Tartiflette", 40000, 20, "Gratinado de Papa y Cerdo", tartiflette)
    ]

#Crear turnos
turno1 = Turno(TipoTurno.SEMANA, 2.0, 50000)
turno2 = Turno(TipoTurno.SEMANA, 8.0, 60000)
turno3 = Turno(TipoTurno.SEMANA, 2.0, 70000)
turno4 = Turno(TipoTurno.DOMINGO, 8.0, 55000)
turno5 = Turno(TipoTurno.SEMANA, 2.0, 65000)
turno6 = Turno(TipoTurno.SEMANA, 8.0, 75000)
turno7 = Turno(TipoTurno.SEMANA, 2.0, 60000)
turno8 = Turno(TipoTurno.SEMANA, 8.0, 70000)
turno9 = Turno(TipoTurno.SEMANA, 2.0, 80000)
turno10 = Turno(TipoTurno.SEMANA, 8.0, 65000)
turno11 = Turno(TipoTurno.SEMANA, 3.0, 80000)
turno12 = Turno(TipoTurno.SABADO, 7.0, 50000)
turno13 = Turno(TipoTurno.SABADO, 3.0, 60000)
turno14 = Turno(TipoTurno.SEMANA, 7.0, 70000)
turno15 = Turno(TipoTurno.SEMANA, 2.0, 55000)
turno16 = Turno(TipoTurno.DOMINGO, 3.0, 55000)
turno17 = Turno(TipoTurno.SABADO, 2.0, 55000)

#Crear empleados
empleado1 = Mesero("Juan", 123456789, "mesero", restaurante, turno1)
empleado1.agregarTurno(turno2)
restaurante.contratarEmpleado(empleado1)
empleado2 = Cocinero("Fernando", 234567891, "cocinero", restaurante, turno2)
empleado2.agregarTurno(turno3)
restaurante.contratarEmpleado(empleado2)
empleado3 = Domiciliario("Santiago", 345678912, "domiciliario", restaurante, turno4)
empleado1.agregarTurno(turno5)
restaurante.contratarEmpleado(empleado3)
empleado4 = Mesero("Jhon", 123456789, "mesero", restaurante, turno6)
empleado1.agregarTurno(turno7)
restaurante.contratarEmpleado(empleado4)
empleado5 = Cocinero("Moises", 234567891, "cocinero", restaurante, turno8)
empleado2.agregarTurno(turno9)
restaurante.contratarEmpleado(empleado5)
empleado6 = Domiciliario("Rigo", 345678912, "domiciliario", restaurante, turno10)
empleado1.agregarTurno(turno11)
restaurante.contratarEmpleado(empleado6)
empleado7 = Mesero("Brayan", 123456789, "mesero", restaurante, turno12)
empleado1.agregarTurno(turno13)
restaurante.contratarEmpleado(empleado7)
empleado8 = Cocinero("Felipe", 234567891, "cocinero", restaurante, turno14)
empleado2.agregarTurno(turno15)
restaurante.contratarEmpleado(empleado8)
empleado9 = Domiciliario("Martin", 345678912, "domiciliario", restaurante, turno16)
empleado1.agregarTurno(turno17)
restaurante.contratarEmpleado(empleado9)
print(restaurante.getEmpleados())

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
    gestion_reserva = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    gestion_reservas_app = GestionReservasApp(gestion_reserva, restaurante)
    gestion_reserva.grid(row=1, column=0, sticky="nsew")
    gestion_reserva.pack_propagate(False)

def delete_frames_ventana_principal():
    for widget in ventanaPrincipal.winfo_children():
        if(isinstance(widget,Frame)):
            widget.destroy()

def gestion_pedidos():
    res = Material(Tipo.RES, 100, 100)
    especias = Material(Tipo.ESPECIAS, 100, 50)
    aceites = Material(Tipo.ACEITES, 100, 100)
    Muton = {res: 1, especias: 10, aceites: 1}
    mutonShot = Plato("Muton Shot",30000,15,"Costillas de Res con Salsa especial",Muton)
    menu = [mutonShot]
    delete_frames_ventana_principal()
    gestion_pedidos = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    gestion_pedidos_app = GestionPedidosApp(gestion_pedidos, menu, imagenes_recetas, restaurante)
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
    v4.tkraise()

def gFinanciera():
    v5 = Frame(ventanaPrincipal, padx=20, pady=20, bg="gray77")
    v5.grid(row=0, column=0, sticky="nsew")

# - - - - - - - - - - - - - - - -

    label1 = Label(v5, text="Gestión Financiera", font=("arial", 30), fg="blue", bg="gray77")
    botonPresupuesto = Button(v5, text="Presupuesto", width=30, height=10)
    botonGananciasBrutas = Button(v5, text="Ganancias Brutas", width=30, height=10)
    botonGananciasNetas = Button(v5, text="Ganancias Netas", width=30, height=10)
    botonGastosMateriales = Button(v5, text="Consultar Gastos del Inventario", width=30, height=10)
    botonGastosMaterialesEsp= Button(v5, text="Consultar Gasto Especifico de un Material", width=30, height=10)
    botonLiquidacion= Button(v5, text="Consultar Liquidación de un Empleado", width=30, height=10)
    botonPagoEmpleados= Button(v5, text="Consultar Pago total de los Empleados", width=30, height=10)
    botonPagoEmpleadosEsp= Button(v5, text="Consultar Pago total de un Empleado", width=30, height=10)
    botonCostoPromedio= Button(v5, text="Consultar el costo Promedio de realizar un plato", width=30, height=10)

    label1.grid(row=0, column=1, padx=10, pady=10)
    botonPresupuesto.grid(row=1, column=0, padx=20, pady=10)
    botonGananciasBrutas.grid(row=1, column=2, padx=10, pady=10)
    botonGananciasNetas.grid(row=2, column=1, padx=10, pady=10)
    botonGastosMateriales.grid(row=3, column=0, padx=20, pady=10)
    botonGastosMaterialesEsp.grid(row=3, column=2, padx=10, pady=10)

    for i in range(5):
        v5.grid_columnconfigure(i, weight=5)

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

imagen_sebastian1 = Image.open("src\imagenes\imagen_sebastian1.png")
imagen_sebastian2 = Image.open("src\imagenes\imagen_sebastian2.png")
imagen_sebastian3 = Image.open("src\imagenes\imagen_sebastian3.png")
imagen_sebastian4 = Image.open("src\imagenes\imagen_sebastian1.png")

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

# Creacion de ventana principal
ventanaPrincipal = Toplevel()
ventanaPrincipal.title("Gestion Administrativa Le Quasó")
ventanaPrincipal.geometry("1080x720")
ventanaPrincipal.resizable(False,False)

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

# Frame de gestion de inventario
v4 = Frame(ventanaPrincipal,padx=20,pady=20,bg="gray77")

v4.grid(row=0, column=0, sticky="nsew")

gestionInv=Label(v4,text="Gestión de Inventario", font=("arial",30),fg="blue",bg="gray77")

revisarInv=Button(v4,text="Consultar Inventario",width=30,height=10)
comprarMat=Button(v4,text="Comprar Materiales",width=30,height=10)
botarMat=Button(v4,text="Desechar Materiales",width=30,height=10)

gestionInv.grid(row=0,column=1,padx=10,pady=10)
revisarInv.grid(row=1,column=1,padx=20,pady=10)
comprarMat.grid(row=2,column=0,padx=10,pady=10)
botarMat.grid(row=2,column=2,padx=10,pady=10)

for i in range(3):
    v4.grid_columnconfigure(i,weight=1)
ancho_receta, alto_receta = 30, 30

# Ocultar ventana principal
ventanaPrincipal.withdraw()

# Configuracion de menu ayuda
ventanaInicio.mainloop()
