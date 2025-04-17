# -*- coding: utf-8 -*-
"""
Módulo que implementa el patrón Singleton para el Gestor de Inventario.
"""

from model.inventario_modelo import Inventario


class GestorInventario:
    """
    Clase que implementa el patrón Singleton para el manejo del inventario.

    Se asegura de que solo exista una única instancia de GestorInventario.
    """

    __instancia = None

    def __new__(cls, *args, **kwargs):
        """
        Crea una nueva instancia de GestorInventario si aún no existe,
        de lo contrario retorna la instancia existente.
        """
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            cls.__instancia.inventario = Inventario()
        return cls.__instancia

    def agregar_item(self, item, cantidad):
        """
        Agrega un producto al inventario.

        Args:
            item (str): Nombre del producto.
            cantidad (int): Cantidad a agregar.
        """
        self.inventario.agregar_item(item, cantidad)

    def eliminar_item(self, item, cantidad):
        """
        Elimina una cantidad de un producto del inventario.

        Args:
            item (str): Nombre del producto.
            cantidad (int): Cantidad a eliminaar.
        """
        self.inventario.eliminar_item(item, cantidad)

    def obtener_items(self):
        """
        Obtiene el diccionario de productos y cantidades del inventario.

        Returns:
            dict: Diccionario con los productos y sus cantidades.
        """
        return self.inventario.obtener_items()


    def modificar_item(self, item, nueva_cantidad):
        """
        Modifica la cantidad de un producto existente.

        Args:
            item (str): Nombre del producto.
            nueva_cantidad (int): Nueva cantidad.
        """
        self.inventario.modificar_item(item, nueva_cantidad)
