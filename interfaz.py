from customtkinter import CTk, CTkLabel, CTkButton, CTkFrame, CTkEntry, CTkToplevel
from PIL import Image, ImageTk
import sys
import datetime
from main import Main
import threading  
from interface import Interface

c_negro = '#010101'
c_blanco = '#FFFFFF'
c_azul = '#87CEEB'
user_data_file = 'users.txt'

# Ruta del logo
logo = 'C:/Users/lenovo/Dropbox/Mi PC (LAPTOP-DL0G2Q4C)/Downloads/CORRECCION/imagenes/logo3.png'

root = CTk()
root.title('Programador De Tareas')
root.geometry("500x600+350+20")
root.minsize(400, 500)
root.config(bg=c_negro)

try:
    image = Image.open(logo)
    logo_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen del logo: {e}")
    sys.exit(1)

root.call('wm', 'iconphoto', root._w, logo_image)

frame = CTkFrame(root, fg_color=c_negro)
frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)
frame.columnconfigure([0, 1], weight=1)
frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Crear un label para mostrar el logo
CTkLabel(frame, text='', image=logo_image, fg_color=c_negro).grid(columnspan=2, row=0)

usuario_entry = CTkEntry(frame, font=('Arial', 12), placeholder_text="Usuario", border_color=c_azul, fg_color=c_negro, width=220, height=40)
usuario_entry.grid(columnspan=2, row=1, padx=4, pady=4)

contraseña_entry = CTkEntry(frame, font=('Arial', 12), placeholder_text="Contraseña", border_color=c_azul, fg_color=c_negro, width=220, height=40, show="*")
contraseña_entry.grid(columnspan=2, row=2, padx=4, pady=4)

main_instance = Main()
class ManejoInter(Interface):
    def __init__(self):
        pass
def iniciar_sesion():
    nombre_usuario = usuario_entry.get()
    contraseña_usuario = contraseña_entry.get()

    if main_instance.verificar_credenciales(nombre_usuario, contraseña_usuario):
        print("Inicio de sesión exitoso")
        mostrar_bienvenida(nombre_usuario)
    else:
        print("Usuario no encontrado. Registrando nuevo usuario.")
        main_instance.registrar_usuario(nombre_usuario, contraseña_usuario)
        if main_instance.verificar_credenciales(nombre_usuario, contraseña_usuario):
            print("Registro exitoso y sesión iniciada.")
            mostrar_bienvenida(nombre_usuario)
        else:
            print("Error: No se pudo registrar el usuario")

def mostrar_bienvenida(nombre_usuario):
    # Limpiar el frame actual
    for widget in frame.winfo_children():
        widget.destroy()
    
    bienvenida_label = CTkLabel(frame, text=f"Bienvenido, {nombre_usuario}!", font=('Arial', 40), fg_color=c_negro, bg_color=c_negro)
    bienvenida_label.grid(columnspan=2, row=1, padx=4, pady=4)
    
    # Usar un hilo para esperar 5 segundos antes de cambiar de ventana
    threading.Thread(target=esperar_y_cambiar_ventana, args=(nombre_usuario,)).start()

def esperar_y_cambiar_ventana(nombre_usuario):
    import time
    time.sleep(5)  # Esperar 5 segundos
    
    # Crear una nueva ventana y destruir la actual
    root.after(0, lambda: [root.destroy(), crear_nueva_ventana(nombre_usuario)])

def crear_nueva_ventana(nombre_usuario):
    nueva_ventana = CTk()
    nueva_ventana.title("Programador de Tareas")
    nueva_ventana.geometry('500x600+350+20')
    nueva_ventana.minsize(400, 500)
    nueva_ventana.config(bg=c_negro)

    # Crear el frame en la nueva ventana
    frame_botonera = CTkFrame(nueva_ventana, fg_color=c_negro)
    frame_botonera.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)
    frame_botonera.columnconfigure([0,1], weight= 1)  
    frame_botonera.rowconfigure([0, 1, 2, 3, 4, 5], weight=1) 
    nueva_ventana.columnconfigure(0, weight= 1)
    nueva_ventana.rowconfigure(0, weight= 1)

    mostrar_botones(frame_botonera, nueva_ventana)

    nueva_ventana.mainloop()

# Agregar los botones que permiten gestionar las tareas
def mostrar_botones(frame, root):
    botones_textos = [
        'Agregar Tarea',
        'Tachar Tarea como Hecha',
        'Mostrar Tareas',
        'Recordar Tarea Importante',
        'Salir'
    ]
    
    botones_comandos = [
        lambda: agregar_tarea(root),
        lambda: tachar_tarea(root),
        lambda: mostrar_tareas(root),
        lambda: recordar_tarea(root),
        sys.exit
    ]

    for i, (texto, comando) in enumerate(zip(botones_textos, botones_comandos)):
        btn = CTkButton(frame, text=texto, font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=comando)
        btn.grid(column=0, row=i, padx=4, pady=4, sticky="ew")

# Definir las funciones de cada acción
def agregar_tarea(root):
    ventana_tarea = CTkToplevel(root)
    ventana_tarea.title("Agregar Tarea")
    ventana_tarea.geometry("300x200")
    ventana_tarea.config(bg=c_negro)

    CTkLabel(ventana_tarea, text="Nombre de la Tarea:", fg_color=c_negro, bg_color=c_negro).pack(pady=5)
    tarea_entry = CTkEntry(ventana_tarea, placeholder_text="Escribe la tarea", width=200, fg_color=c_negro, bg_color=c_negro)
    tarea_entry.pack(pady=5)

    CTkLabel(ventana_tarea, text="Fecha (YYYY-MM-DD):", fg_color=c_negro, bg_color=c_negro).pack(pady=5)
    fecha_entry = CTkEntry(ventana_tarea, placeholder_text="Escribe la fecha", width=200, fg_color=c_negro, bg_color=c_negro)
    fecha_entry.pack(pady=5)

    agregar_btn = CTkButton(ventana_tarea, text="Agregar Tarea",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=lambda: confirmar_agregar_tarea(tarea_entry, fecha_entry, ventana_tarea))
    agregar_btn.pack(side='left', padx=10, pady=10)

    cancelar_btn = CTkButton(ventana_tarea, text="Cancelar",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=ventana_tarea.destroy)
    cancelar_btn.pack(side='right', padx=10, pady=10)

def confirmar_agregar_tarea(tarea_entry, fecha_entry, ventana_tarea):
    tarea = tarea_entry.get()
    fecha = fecha_entry.get()

    try:
        datetime.datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        print("Error: La fecha debe estar en formato YYYY-MM-DD.")
        return

    guardar_tarea(tarea, fecha)
    ventana_tarea.destroy()

def guardar_tarea(tarea, fecha):
    with open('tareas.txt', 'a') as file:
        file.write(f'{tarea} - {fecha}\n')
    print(f"Tarea guardada: {tarea} - {fecha}")

# Función para tachar una tarea como hecha
def tachar_tarea(root):
    ventana_tachar = CTkToplevel(root)
    ventana_tachar.title("Tachar Tarea")
    ventana_tachar.geometry("300x200")
    ventana_tachar.config(bg=c_negro)

    CTkLabel(ventana_tachar, text="Número de la Tarea:", fg_color=c_negro, bg_color=c_negro).pack(pady=5)
    tarea_num_entry = CTkEntry(ventana_tachar, placeholder_text="Escribe el número de la tarea", width=200, fg_color=c_negro, bg_color=c_negro)
    tarea_num_entry.pack(pady=5)

    tachar_btn = CTkButton(ventana_tachar, text="Tachar Tarea",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=lambda: confirmar_tachar_tarea(tarea_num_entry, ventana_tachar))
    tachar_btn.pack(side='left', padx=10, pady=10)

    cancelar_btn = CTkButton(ventana_tachar, text="Cancelar",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=ventana_tachar.destroy)
    cancelar_btn.pack(side='right', padx=10, pady=10)

def confirmar_tachar_tarea(tarea_num_entry, ventana_tachar):
    tarea_num = tarea_num_entry.get()

    if not tarea_num.isdigit():
        print("Error: El número de tarea debe ser un número entero.")
        return

    tarea_num = int(tarea_num) - 1  # Convertir a índice
    tareas = cargar_tareas()

    if 0 <= tarea_num < len(tareas):
        tarea = tareas[tarea_num]
        tareas[tarea_num] = f"{tarea.strip()} (Hecho)"
        guardar_tareas(tareas)
        print(f"Tarea {tarea_num + 1} marcada como hecha.")
    else:
        print("Error: Número de tarea no válido.")

    ventana_tachar.destroy()

def cargar_tareas():
    try:
        with open('tareas.txt', 'r') as file:
            tareas = file.readlines()
        return tareas
    except FileNotFoundError:
        print("No se encontró el archivo de tareas.")
        return []

def guardar_tareas(tareas):
    with open('tareas.txt', 'w') as file:
        file.writelines(tareas)

# Función para mostrar todas las tareas
def mostrar_tareas(root):
    ventana_mostrar = CTkToplevel(root)
    ventana_mostrar.title("Mostrar Tareas")
    ventana_mostrar.geometry("400x300")
    ventana_mostrar.config(bg=c_negro)

    tareas = cargar_tareas()

    if tareas:
        for i, tarea in enumerate(tareas):
            tarea_label = CTkLabel(ventana_mostrar, text=f"{i + 1}. {tarea.strip()}", fg_color=c_negro, bg_color=c_negro)
            tarea_label.pack(anchor='w', padx=10, pady=2)
    else:
        CTkLabel(ventana_mostrar, text="No hay tareas.", fg_color=c_negro, bg_color=c_negro).pack(pady=20)

    cerrar_btn = CTkButton(ventana_mostrar, text="Cerrar",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=ventana_mostrar.destroy)
    cerrar_btn.pack(pady=10)

# Función para recordar una tarea importante
def recordar_tarea(root):
    ventana_recordar = CTkToplevel(root)
    ventana_recordar.title("Recordar Tarea Importante")
    ventana_recordar.geometry("300x200")
    ventana_recordar.config(bg=c_negro)

    CTkLabel(ventana_recordar, text="Número de la Tarea:", fg_color=c_negro, bg_color=c_negro).pack(pady=5)
    tarea_num_entry = CTkEntry(ventana_recordar, placeholder_text="Escribe el número de la tarea", width=200, fg_color=c_negro, bg_color=c_negro)
    tarea_num_entry.pack(pady=5)

    recordar_btn = CTkButton(ventana_recordar, text="Recordar Tarea",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=lambda: confirmar_recordar_tarea(tarea_num_entry, ventana_recordar))
    recordar_btn.pack(side='left', padx=10, pady=10)

    cancelar_btn = CTkButton(ventana_recordar, text="Cancelar",font=('Arial', 12), border_color= c_azul, fg_color= c_negro, hover_color= c_azul, corner_radius=12, border_width=2, command=ventana_recordar.destroy)
    cancelar_btn.pack(side='right', padx=10, pady=10)

def confirmar_recordar_tarea(tarea_num_entry, ventana_recordar):
    tarea_num = tarea_num_entry.get()

    if not tarea_num.isdigit():
        print("Error: El número de tarea debe ser un número entero.")
        return

    tarea_num = int(tarea_num) - 1  # Convertir a índice
    tareas = cargar_tareas()

    if 0 <= tarea_num < len(tareas):
        tarea = tareas[tarea_num].strip()
        print(f"Recordatorio de la Tarea {tarea_num + 1}: {tarea}")
    else:
        print("Error: Número de tarea no válido.")

    ventana_recordar.destroy()

bt_iniciar = CTkButton(frame, font=('Arial', 12), border_color=c_azul, fg_color=c_negro, hover_color=c_azul, corner_radius=12, border_width=2, text="Iniciar Sesión", height=40, command=iniciar_sesion)
bt_iniciar.grid(columnspan=2, row=4, padx=4, pady=4)

root.mainloop()
