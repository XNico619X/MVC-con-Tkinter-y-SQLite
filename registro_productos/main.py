if __name__ == "__main__":
    modelo = Producto()

    vista = registroVista(controlador=None)
    controlador = ProductoControlador(modelo, vista)
    
    controlador.ejecutar()
