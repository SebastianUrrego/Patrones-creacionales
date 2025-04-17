# -*- coding: utf-8 -*-
"""
Archivo principal que orquesta la ejecución de la aplicación del Gestor de Inventario.
"""

from singleton.inventario_singleton import GestorInventario
from controller.inventario_controlador import InventarioControlador
from view.inventario_vista_tkinter import InventarioVistaTk  # Interfaz gráfica (Tkinter)
# from view.inventario_vista import InventarioVista  # Vista de consola (opcional)

def main():
    # Instanciar el Singleton (gestor de inventario)
    gestor = GestorInventario()
    controlador = InventarioControlador(gestor)

    # Lanzar la interfaz gráfica
    InventarioVistaTk(controlador)

    # ----------------------------------------------
    # Vista de consola (desactivada por defecto)
    # Si desea probar la versión en consola con datos quemados,
    # descomente las siguientes líneas:
    # ----------------------------------------------

    """
    vista = InventarioVista()

    # Agregar productos quemados
    vista.mostrar_mensaje(controlador.agregar_nuevo_item("Palomitas", 100))
    vista.mostrar_mensaje(controlador.agregar_nuevo_item("Refrescos", 50))
    vista.mostrar_mensaje(controlador.agregar_nuevo_item("Dulces", 30))

    # Mostrar el estado actual del inventario
    vista.mostrar_mensaje("\nDespués de agregar productos:")
    vista.mostrar_items(controlador.listar_items())

    # Eliminar algunos productos
    vista.mostrar_mensaje(controlador.eliminar_item_existente("Palomitas", 40))

    # Mostrar el estado final del inventario
    vista.mostrar_mensaje("\nDespués de eliminar productos:")
    vista.mostrar_items(controlador.listar_items())
    """


if __name__ == "__main__":
    main()
