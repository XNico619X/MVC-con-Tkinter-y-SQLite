from model import Producto
from vista import registroVista
from controlador import ProductoControlador

if __name__ == "__main__":
    modelo = Producto()

    vista = registroVista(controlador=None)
    controlador = ProductoControlador(modelo, vista)
    
    controlador.ejecutar()
