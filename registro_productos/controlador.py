from model import Producto
from vista import registroVista

class ProductoControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu(self.vista)
            
            if opcion == '1':
                nombre, cantidad, precio = self.vista.agregar_producto(self.vista)
                self.modelo.agregar_producto(nombre, cantidad, precio)
                self.vista.mostrar_mensaje(self.vista, "¡Producto agregado con éxito!")
            
            elif opcion == '2':
                productos = self.modelo.listar()
                productos_formateados = [
                    {'id': p[0], 'nombre': p[1], 'cantidad': p[2], 'precio': p[3]} 
                    for p in productos
                ]
                self.vista.mostrar_productos(self.vista, productos_formateados)
            
            elif opcion == '3':
                id_prod = self.vista.eliminar_producto(self.vista)
                self.modelo.eliminar_producto(id_prod)
                self.vista.mostrar_mensaje(self.vista, f"Producto con ID {id_prod} eliminado.")
            
            elif opcion == '4':
                self.vista.mostrar_mensaje(self.vista, "Saliendo del sistema...")
                break
            else:
                self.vista.mostrar_mensaje(self.vista, "Opción no válida, intente de nuevo.")
