import sys
import datetime
from tkinter import Listbox, Tk, messagebox
from customtkinter import CTkButton, CTkFrame, CTkEntry, CTkLabel, CTkToplevel

class BotonesBase:
    def __init__(self, root):
        self.root = root
        self.frame = CTkFrame(root, width=480, height=500, bg_color='#010101')  # Fondo negro
        self.frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure([0, 1, 2, 3, 4], weight=1)

        self.mostrar_botones()

    def mostrar_botones(self):
        botones_textos = [
            'Agregar Tarea',
            'Tachar Tarea como Hecha',
            'Mostrar Tareas',
            'Recordar Tarea Importante',
            'Salir'
        ]
        
        botones_comandos = [
            self.agregar_tarea,
            self.tachar_tarea,
            self.mostrar_tareas,
            self.recordar_tarea,
            self.salir
        ]

        for i, (texto, comando) in enumerate(zip(botones_textos, botones_comandos)):
            btn = CTkButton(self.frame, text=texto, font=('Arial', 12), border_color='#FFFFFF', fg_color='#010101', hover_color='#FFFFFF', corner_radius=12, border_width=2, command=comando)
            btn.grid(column=0, row=i, padx=4, pady=4, sticky="ew")

    def agregar_tarea(self):
        ventana_tarea = CTkToplevel(self.root)
        ventana_tarea.title("Agregar Tarea")
        ventana_tarea.geometry("300x200")
        ventana_tarea.config(bg='#010101')  # Fondo negro

        CTkLabel(ventana_tarea, text="Nombre de la Tarea:", bg_color='#010101', fg_color='#010101').pack(pady=5)
        tarea_entry = CTkEntry(ventana_tarea, placeholder_text="Escribe la tarea", width=200, fg_color='#010101', bg_color='#010101')  # Fondo negro, texto blanco
        tarea_entry.pack(pady=5)

        CTkLabel(ventana_tarea, text="Fecha (YYYY-MM-DD):", bg_color='#010101', fg_color='#010101').pack(pady=5)
        fecha_entry = CTkEntry(ventana_tarea, placeholder_text="Escribe la fecha", width=200, fg_color='#010101', bg_color='#010101')  # Fondo negro, texto blanco
        fecha_entry.pack(pady=5)

        agregar_btn = CTkButton(ventana_tarea, text="Agregar Tarea", command=lambda: self.confirmar_agregar_tarea(tarea_entry, fecha_entry, ventana_tarea))
        agregar_btn.pack(side='left', padx=10, pady=10)

        cancelar_btn = CTkButton(ventana_tarea, text="Cancelar", command=ventana_tarea.destroy)
        cancelar_btn.pack(side='right', padx=10, pady=10)

    def confirmar_agregar_tarea(self, tarea_entry, fecha_entry, ventana_tarea):
        tarea = tarea_entry.get()
        fecha = fecha_entry.get()

        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "La fecha debe estar en formato YYYY-MM-DD.")
            return

        self.guardar_tarea(tarea, fecha)
        ventana_tarea.destroy()
        self.mostrar_opciones_adicionales()

    def guardar_tarea(self, tarea, fecha):
        with open('tareas.txt', 'a') as file:
            file.write(f'{tarea} - {fecha}\n')
        print(f"Tarea guardada: {tarea} - {fecha}")

    def mostrar_opciones_adicionales(self):
        ventana_opciones = CTkToplevel(self.root)
        ventana_opciones.title("Opciones")
        ventana_opciones.geometry("300x150")
        ventana_opciones.config(bg='#010101')  # Fondo negro

        CTkLabel(ventana_opciones, text="¿Deseas agregar otra tarea?", bg_color='#010101', fg_color='#010101').pack(pady=10)

        agregar_btn = CTkButton(ventana_opciones, text="Agregar Nueva Tarea", command=lambda: [ventana_opciones.destroy(), self.agregar_tarea()])
        agregar_btn.pack(side='left', padx=10, pady=10)

        salir_btn = CTkButton(ventana_opciones, text="Salir", command=ventana_opciones.destroy)
        salir_btn.pack(side='right', padx=10, pady=10)

    def tachar_tarea(self):
        ventana_tareas = CTkToplevel(self.root)
        ventana_tareas.title("Tachar Tarea")
        ventana_tareas.geometry("400x300")
        ventana_tareas.config(bg='#010101')  # Fondo negro

        tareas = self.cargar_tareas()
        
        if not tareas:
            CTkLabel(ventana_tareas, text="No hay tareas para mostrar", bg_color='#010101', fg_color='#FFFFFF').pack(pady=10)
            return

        self.lista_tareas = Listbox(ventana_tareas, selectmode='multiple', bg='#010101', fg='#FFFFFF')  # Fondo negro, texto blanco
        for tarea in tareas:
            self.lista_tareas.insert('end', tarea.strip())
        self.lista_tareas.pack(pady=10)

        tachar_btn = CTkButton(ventana_tareas, text="Tachar Seleccionadas", command=self.confirmar_tachar_tarea)
        tachar_btn.pack(pady=10)

        cerrar_btn = CTkButton(ventana_tareas, text="Cerrar", command=ventana_tareas.destroy)
        cerrar_btn.pack(pady=10)

    def confirmar_tachar_tarea(self):
        tareas_seleccionadas = self.lista_tareas.curselection()
        if not tareas_seleccionadas:
            messagebox.showwarning("Advertencia", "Selecciona al menos una tarea para tachar.")
            return

        tareas = self.cargar_tareas()
        tareas_actualizadas = [tarea for i, tarea in enumerate(tareas) if i not in tareas_seleccionadas]

        with open('tareas.txt', 'w') as file:
            file.writelines(tareas_actualizadas)
        
        messagebox.showinfo("Éxito", "Tareas seleccionadas tachadas exitosamente.")
        self.lista_tareas.delete(0, 'end')

    def cargar_tareas(self):
        try:
            with open('tareas.txt', 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def mostrar_tareas(self):
        ventana_tareas = CTkToplevel(self.root)
        ventana_tareas.title("Mostrar Tareas")
        ventana_tareas.geometry("400x300")
        ventana_tareas.config(bg='#010101')  # Fondo negro

        tareas = self.cargar_tareas()
        
        if not tareas:
            CTkLabel(ventana_tareas, text="No hay tareas para mostrar", bg_color='#010101', fg_color='#FFFFFF').pack(pady=10)
            return

        tareas_ordenadas = sorted(tareas, key=lambda x: datetime.datetime.strptime(x.split(' - ')[1].strip(), '%Y-%m-%d'))

        tareas_texto = "\n".join([tarea.strip() for tarea in tareas_ordenadas])
        CTkLabel(ventana_tareas, text="Tareas:", bg_color='#010101', fg_color='#010101').pack(pady=5)
        CTkLabel(ventana_tareas, text=tareas_texto, bg_color='#010101', fg_color='#010101').pack(pady=5)

        cerrar_btn = CTkButton(ventana_tareas, text="Cerrar", command=ventana_tareas.destroy)
        cerrar_btn.pack(pady=10)

    def recordar_tarea(self):
        ventana_tareas = CTkToplevel(self.root)
        ventana_tareas.title("Recordar Tarea")
        ventana_tareas.geometry("400x300")
        ventana_tareas.config(bg='#010101') 

        tareas = self.cargar_tareas()
        
        if not tareas:
            CTkLabel(ventana_tareas, text="No hay tareas para mostrar", bg_color='#010101', fg_color='#FFFFFF').pack(pady=10)
            return

        self.lista_tareas = Listbox(ventana_tareas, selectmode='single', bg='#010101', fg='#FFFFFF')  # Fondo negro, texto blanco
        for tarea in tareas:
            self.lista_tareas.insert('end', tarea.strip())
        self.lista_tareas.pack(pady=10)

        recordar_btn = CTkButton(ventana_tareas, text="Recordar Tarea Seleccionada", command=self.confirmar_recordar_tarea)
        recordar_btn.pack(pady=10)

        cerrar_btn = CTkButton(ventana_tareas, text="Cerrar", command=ventana_tareas.destroy)
        cerrar_btn.pack(pady=10)

    def confirmar_recordar_tarea(self):
        tarea_seleccionada = self.lista_tareas.curselection()
        if not tarea_seleccionada:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para recordar.")
            return

        tarea = self.lista_tareas.get(tarea_seleccionada[0])
        self.guardar_tarea_recordar(tarea)
        messagebox.showinfo("Éxito", "Tarea a recordar guardada exitosamente.")
        self.lista_tareas.delete(0, 'end')

    def guardar_tarea_recordar(self, tarea):
        with open('tarea_recordar.txt', 'w') as file:
            file.write(tarea)
        print(f"Tarea para recordar guardada: {tarea}")

    def salir(self):
        sys.exit()

if __name__ == "__main__":
    root = Tk()
    root.title("Gestor de Tareas")
    root.geometry("300x290")
    root.config(bg='#010101') 

    app = BotonesBase(root)
    
    root.mainloop()
