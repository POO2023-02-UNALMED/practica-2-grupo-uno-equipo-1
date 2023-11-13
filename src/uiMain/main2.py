import tkinter as tk

def nada():
    pass

def infoApp():
    pass

def salir():
    pass

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
    pass

ventana=tk.Tk()
ventana.title("Gestion Administrativa Le Quasó")
ventana.geometry("1080x720")


frame1=tk.Frame(ventana,bg="gray89",height=720)


menuBar=tk.Menu(ventana)
ventana.config(menu=menuBar)
menu1=tk.Menu(menuBar)
menu2=tk.Menu(menuBar)
menu3=tk.Menu(menuBar)


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

ventana.mainloop()