from model import modeloUsuario
from vista import VistaRegistroUsuarios


class ControladorUsuarios:
    def __init__(self, root):
        self.modelo = modeloUsuario()
        self.vista = VistaRegistroUsuarios(root)

        # Conectar botón con función
        self.vista.btn_registrar.config(command=self.registrar_usuario)

        # Mostrar usuarios al iniciar
        self.actualizar_tabla()

        # Cerrar conexión al salir
        root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def registrar_usuario(self):
        nombre, email, contraseña = self.vista.obtener_datos_usuario()

        # Validación básica
        if not nombre or not email or not contraseña:
            self.vista.mostrar_mensaje(
                "Error", "Todos los campos son obligatorios."
            )
            return

        # Verificar si email ya existe
        if self.modelo.email_existe(email):
            self.vista.mostrar_mensaje(
                "Error", "El email ya está registrado."
            )
            return

        # Agregar usuario
        exito, resultado = self.modelo.agregar_usuario(
            nombre, email, contraseña
        )

        if exito:
            self.vista.mostrar_mensaje(
                "Éxito", f"Usuario registrado con ID: {resultado}"
            )
            self.actualizar_tabla()
        else:
            self.vista.mostrar_mensaje("Error", str(resultado))

    def actualizar_tabla(self):
        usuarios = self.modelo.obtener_usuarios()
        self.vista.mostrar_usuarios(usuarios)

    def cerrar_aplicacion(self):
        self.modelo.cerrar_conexion()
        self.vista.root.destroy()
