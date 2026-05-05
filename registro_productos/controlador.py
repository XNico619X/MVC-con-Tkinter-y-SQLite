from model import Producto
from vista import registroVista

class ProductoControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            
            if opcion == '1':
                nombre, cantidad, precio = self.vista.agregar_producto()
                self.modelo.agregar_producto(nombre, cantidad, precio)
                self.vista.mostrar_mensaje("¡Producto agregado con éxito!")
            
            elif opcion == '2':
                productos = self.modelo.listar()
                productos_formateados = [
                    {'id': p[0], 'nombre': p[1], 'cantidad': p[2], 'precio': p[3]} 
                    for p in productos
                ]
                self.vista.mostrar_productos(productos_formateados)
            
            elif opcion == '3':
                id_prod = self.vista.eliminar_producto()
                self.modelo.eliminar_producto(id_prod)
                self.vista.mostrar_mensaje(f"Producto con ID {id_prod} eliminado.")
            
            elif opcion == '4':
                self.vista.mostrar_mensaje("Saliendo del sistema...")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida, intente de nuevo.")
