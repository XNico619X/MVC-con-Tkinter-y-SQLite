class registroVista:
    def __init__(self, controlador):
        self.controlador = controlador

    def mostrar_menu(self):
        while True:
            print("\n--- Registro de Productos ---")
            print("1. Agregar Producto")
            print("2. Mostrar Productos")
            print("3. Eliminar Producto")
            print("4. Salir")
            return input("Seleccione una opción: ")
    
    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        return nombre, cantidad, precio
    
    def mostrar_productos(self, productos):
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\n--- Lista de Productos ---")
            for producto in productos:
                print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")

    def eliminar_producto(self):
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        return id_producto
    
    def mostrar_mensaje(self, mensaje):
        print(mensaje) 