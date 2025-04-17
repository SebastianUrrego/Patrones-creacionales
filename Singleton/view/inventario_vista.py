# -*- coding: utf-8 -*-

""""""
"""
Módulo que define la vista para la interacción con el usuario.
"""

class InventarioVista:
    """
    Vista que se encarga de mostrar los datos y mensajes del inventario.
    """

    @staticmethod
    def mostrar_items(items):
        """
        Muestra en consola el listado de productos del inventario.

        Args:
            items (dict): Diccionario con los productos y sus cantidades.
        """
        if not items:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for item, cantidad in items.items():
                print(f"- {item}: {cantidad}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        """
        Imprime un mensaje en consola.

        Args:
            mensaje (str): Texto a mostrar.
        """
        print(mensaje)

#####