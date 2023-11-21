import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ErrorAplicacion(Exception):
    def __str__(self):
        return "Manejo de errores de la Aplicación:"

class ErroresEntry(ErrorAplicacion):
    pass

class ErroresTipo(ErrorAplicacion):
    pass

class CampoVacio(ErroresEntry):
    def __str__(self):
        return f"{super().__str__()} CampoVacio: El campo no puede estar vacío."

class SinEspacios(ErroresEntry):
    def __str__(self):
        return f"{super().__str__()} SinEspacios: No se permiten espacios en blanco en el campo."

class SoloLetras(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} SoloLetras: Solo se permiten letras en el campo."

class SoloNumeros(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} SoloNumeros: Solo se permiten números en el campo."

class NoUsarSimbolos(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoUsarSimbolos: No se permiten símbolos en el campo."

class NoUsarDecimales(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoUsarDecimales: No se permiten decimales en el campo."

class NoUsarNegativos(ErroresTipo):
  def __str__(self):
      return f"{super().__str__()} NoUsarNegativos: No se permiten números negativos en el campo."

class NoExisteObjeto(ErroresEntry):
    def __init__(self, indice, max_indice):
        self.indice = indice
        self.max_indice = max_indice

    def __str__(self):
        return f"{super().__str__()} NoExisteObjeto: El valor '{self.indice}' no es válido. Ingrese un número entre 0 y {self.max_indice}."

class NoFormatoFecha(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoFormatoFecha: El formato de fecha no es válido. Utilice DD-MM-AAAA."

def validar_num(entry_text):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio()

        # Verificar si hay espacios en blanco
        if ' ' in entry_text:
            raise SinEspacios()

        # Verificar si hay espacios en blanco
        if '.' in entry_text:
            raise NoUsarDecimales()

        # Verificar si hay símbolos, incluyendo comillas
        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos()

        # Verificar si el dato es un número
        numero = int(entry_text)

        # Verificar si el número es negativo
        if numero < 0:
            raise NoUsarNegativos()

        return True
    except ValueError:
        messagebox.showerror("Error", "Manejo de errores de la Aplicación:\nEl dato debe ser un número.")
        return False
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_lista(entry_text, max_indice):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio()

        # Verificar si hay espacios en blanco
        if ' ' in entry_text:
            raise SinEspacios()

        # Verificar si el dato es un número entero
        indice = int(entry_text)

        # Verificar si el índice es válido
        if not (0 <= indice <= max_indice):
            raise NoExisteObjeto(indice, max_indice)

        return True
    except ValueError:
        messagebox.showerror("Error", "Manejo de errores de la Aplicación:\nEl dato debe ser un número.")
        return False
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_string(entry_text):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio()

        # Verificar si hay espacios en blanco
        if ' ' in entry_text:
            raise SinEspacios()

        # Verificar si solo contiene letras
        if not entry_text.isalpha():
            raise SoloLetras()

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_fecha(entry_text):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio()

        # Verificar si hay espacios en blanco
        if ' ' in entry_text:
            raise SinEspacios()

        # Verificar el formato de fecha
        fecha_obj = datetime.strptime(entry_text, "%d-%m-%Y")

        return True
    except ValueError:
        messagebox.showerror("Error", "Manejo de errores de la Aplicación:\nFormato de fecha no válido. Utilice DD-MM-AAAA.")
        return False
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False
        
#Ejemplo para probar los errores
"""
def procesar_datos():
    nombre_text = entry_nombre.get()
    edad_text = entry_edad.get()
    objeto_text = entry_objeto.get()
    fecha_text = entry_fecha.get()

    if (
        validar_string(nombre_text) and
        validar_num(edad_text) and
        validar_lista(objeto_text, len(example_objects) - 1) and
        validar_fecha(fecha_text)
    ):
        mensaje = f"Nombre: {nombre_text}\nEdad: {edad_text}\nObjeto seleccionado: {example_objects[int(objeto_text)]}\nFecha: {fecha_text}"
        messagebox.showinfo("Datos Válidos", mensaje)

# Crear la ventana
root = tk.Tk()
root.title("Validación de Datos")

# Sección para validar Nombre
frame_nombre = tk.Frame(root)
frame_nombre.pack(pady=10)

label_nombre = tk.Label(frame_nombre, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)

entry_nombre = tk.Entry(frame_nombre)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# Sección para validar Edad
frame_edad = tk.Frame(root)
frame_edad.pack(pady=10)

label_edad = tk.Label(frame_edad, text="Edad:")
label_edad.grid(row=0, column=0, padx=5, pady=5)

entry_edad = tk.Entry(frame_edad)
entry_edad.grid(row=0, column=1, padx=5, pady=5)

# Sección para validar Objeto
frame_objeto = tk.Frame(root)
frame_objeto.pack(pady=10)

label_objeto = tk.Label(frame_objeto, text="Índice de Objeto:")
label_objeto.grid(row=0, column=0, padx=5, pady=5)

entry_objeto = tk.Entry(frame_objeto)
entry_objeto.grid(row=0, column=1, padx=5, pady=5)

# Sección para validar Fecha
frame_fecha = tk.Frame(root)
frame_fecha.pack(pady=10)

label_fecha = tk.Label(frame_fecha, text="Fecha (DD-MM-AAAA):")
label_fecha.grid(row=0, column=0, padx=5, pady=5)

entry_fecha = tk.Entry(frame_fecha)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

btn_aceptar = tk.Button(root, text="Aceptar", command=procesar_datos)
btn_aceptar.pack(pady=10)

# Example objects for testing
example_objects = ["Objeto1", "Objeto2", "Objeto3"]

# Ejecutar la aplicación
root.mainloop()
"""
