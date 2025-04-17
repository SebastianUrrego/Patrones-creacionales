# -*- coding: utf-8 -*-
"""
Módulo que define el modelo del inventario.
"""

class Inventario:
    """
    Clase que representa el modelo de los datos del inventario.
    
    Atributos:
        items (dict): Diccionario que almacena los productos y sus cantidades.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de Inventario con un diccionario vacío.
        """
        self.items = {}

    def agregar_item(self, item, cantidad):
        """
        Agrega o incrementa la cantidad de un producto en el inventario.

        Args:
            item (str): Nombre del producto.
            cantidad (int): Cantidad a agregar.
        """
        if item in self.items:
            self.items[item] += cantidad
        else:
            self.items[item] = cantidad

    def eliminar_item(self, item, cantidad):
        """
        Elimina una cantidad determinada de un producto del inventario.
        Si la cantidad llega a 0, elimina el producto del inventario.

        Args:
            item (str): Nombre del producto.
            cantidad (int): Cantidad a eliminar.

        Raises:
            ValueError: Si el producto no existe o la cantidad es insuficiente.
        """
        if item in self.items and self.items[item] >= cantidad:
            self.items[item] -= cantidad
            if self.items[item] == 0:
                del self.items[item]
        else:
            raise ValueError("No existe el producto o la cantidad es insuficiente para eliminar.")

    def obtener_items(self):
        """
        Retorna el diccionario de productos y sus cantidades.

        Returns:
            dict: Diccionario con los items del inventario.
        """
        return self.items
    
    def modificar_item(self, item, nueva_cantidad):
        """
        Modifica directamente la cantidad de un producto.

        Args:
            item (str): Nombre del producto.
            nueva_cantidad (int): Nueva cantidad a asignar.

        Raises:
            ValueError: Si el producto no existe o la cantidad es inválida.
        """
        if item not in self.items:
            raise ValueError("El producto no existe en el inventario.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.items[item] = nueva_cantidad

