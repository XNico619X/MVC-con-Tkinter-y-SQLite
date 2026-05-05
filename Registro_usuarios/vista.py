import tkinter as tk
from tkinter import ttk, messagebox


class VistaRegistroUsuarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuarios")

        # Configuración del frame principal- formulario de registro
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Etiquetas y campos de entrada
        ttk.Label(self.frame, text="Nombre:").grid(
            row=0, column=0, sticky=tk.W)
        self.entry_nombre = ttk.Entry(self.frame, width=30)
        self.entry_nombre.grid(row=0, column=1)

        ttk.Label(self.frame, text="Email:").grid(row=1, column=0, sticky=tk.W)
        self.entry_email = ttk.Entry(self.frame, width=30)
        self.entry_email.grid(row=1, column=1)

        ttk.Label(self.frame, text="Contraseña:").grid(
            row=2, column=0, sticky=tk.W)
        self.entry_contraseña = ttk.Entry(self.frame, width=30, show="*")
        self.entry_contraseña.grid(row=2, column=1)

        # Botón para registrar usuario
        self.btn_registrar = ttk.Button(self.frame, text="Registrar Usuario")
        self.btn_registrar.grid(row=3, column=0, columnspan=2, pady=10)

        # tabla para mostrar usuarios registrados
        frame_tabla = ttk.Frame(self.root, padding="20")
        frame_tabla.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        frame_tabla.pack()
        self.tabla_usuarios = ttk.Treeview(frame_tabla, columns=(
            "ID", "Nombre", "Email"), show="headings")
        self.tabla_usuarios.heading("ID", text="ID")
        self.tabla_usuarios.heading("Nombre", text="Nombre")
        self.tabla_usuarios.heading("Email", text="Email")

        # Boton eliminar usuario
        self.btn_eliminar = ttk.Button(frame_tabla, text="Eliminar Usuario")
        self.btn_eliminar.pack(pady=10)

    def obtener_datos_usuario(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        contraseña = self.entry_contraseña.get().strip()
        return nombre, email, contraseña

    def mostrar_usuarios(self, usuarios):
        # Limpiar tabla antes de mostrar nuevos datos
        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)
        # Insertar usuarios en la tabla
        for usuario in usuarios:
            self.tabla_usuarios.insert("", "end", values=usuario)

    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
