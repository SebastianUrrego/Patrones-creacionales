# -*- coding: utf-8 -*-
"""
Módulo que define el controlador para gestionar la comunicación entre la vista y el modelo.
"""
class InventarioControlador:
    """
    Controlador que orquesta la interacción entre la vista y el modelo del inventario.
    """

    def __init__(self, gestor):
        self.gestor = gestor

    def agregar_nuevo_item(self, item, cantidad):
        try:
            self.gestor.agregar_item(item, cantidad)
            return f"Agregado: {cantidad} de '{item}'."
        except Exception as e:
            return f"Error al agregar '{item}': {str(e)}"

    def eliminar_item_existente(self, item, cantidad):
        try:
            self.gestor.eliminar_item(item, cantidad)
            return f"Eliminado: {cantidad} de '{item}'."
        except Exception as e:
            return f"Error al eliminar '{item}': {str(e)}"

    def listar_items(self):
        return self.gestor.obtener_items()

    def modificar_item_existente(self, nombre_antiguo, nuevo_nombre, nueva_cantidad):
        """
        Modifica un producto existente cambiando su nombre y/o cantidad.

        Args:
            nombre_antiguo (str): Nombre actual del producto.
            nuevo_nombre (str): Nuevo nombre a asignar.
            nueva_cantidad (int): Nueva cantidad del producto.

        Returns:
            str: Mensaje de confirmación o error.
        """
        try:
            items = self.gestor.obtener_items()

            if nombre_antiguo not in items:
                return f"Error: El producto '{nombre_antiguo}' no existe."

            if nueva_cantidad < 0:
                return "Error: La cantidad no puede ser negativa."

            if nuevo_nombre != nombre_antiguo:
                # Cambia nombre y cantidad
                del items[nombre_antiguo]
                items[nuevo_nombre] = nueva_cantidad
                return f"Producto renombrado a '{nuevo_nombre}' con {nueva_cantidad} unidades."
            else:
                # Solo cambia cantidad
                items[nombre_antiguo] = nueva_cantidad
                return f"Cantidad actualizada de '{nombre_antiguo}' a {nueva_cantidad} unidades."
        except Exception as e:
            return f"Error al modificar producto: {str(e)}"
