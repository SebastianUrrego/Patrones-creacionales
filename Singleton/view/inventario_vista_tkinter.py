import tkinter as tk
from tkinter import messagebox


class InventarioVistaTk:
    """
    Clase que representa la interfaz gráfica del gestor de inventario
    para Cine Colombia usando la biblioteca Tkinter.
    """

    def __init__(self, controlador):
        """
        Inicializa la ventana principal y todos los componentes de la interfaz gráfica.

        Args:
            controlador: Instancia del controlador que maneja la lógica del inventario.
        """
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Gestor de Inventario - Cine Colombia")

        # --- Entradas ---
        self.label_producto = tk.Label(self.ventana, text="Producto:")
        self.label_producto.grid(row=0, column=0)
        self.entrada_producto = tk.Entry(self.ventana)
        self.entrada_producto.grid(row=0, column=1)

        self.label_cantidad = tk.Label(self.ventana, text="Cantidad:")
        self.label_cantidad.grid(row=1, column=0)
        self.entrada_cantidad = tk.Entry(self.ventana)
        self.entrada_cantidad.grid(row=1, column=1)

        self.label_nuevo_nombre = tk.Label(self.ventana, text="Nuevo nombre de Producto:")
        self.label_nuevo_nombre.grid(row=2, column=2)
        self.entrada_nuevo_nombre = tk.Entry(self.ventana)
        self.entrada_nuevo_nombre.grid(row=2, column=3)

        # --- Botones ---
        self.boton_agregar = tk.Button(
            self.ventana, text="Agregar", command=self.agregar_producto
        )
        self.boton_agregar.grid(row=2, column=0, pady=5)

        self.boton_eliminar = tk.Button(
            self.ventana, text="Eliminar", command=self.eliminar_producto
        )
        self.boton_eliminar.grid(row=2, column=1)

        self.boton_mostrar = tk.Button(
            self.ventana, text="Mostrar Inventario", command=self.mostrar_inventario
        )
        self.boton_mostrar.grid(row=3, column=0, columnspan=2, pady=5)

        self.btn_modificar = tk.Button(
            self.ventana, text="Modificar", command=self.modificar_item
        )
        self.btn_modificar.grid(row=3, column=2, padx=10, pady=5)

        # --- Área de salida ---
        self.texto_salida = tk.Text(self.ventana, height=10, width=60)
        self.texto_salida.grid(row=4, column=0, columnspan=4)

        self.ventana.mainloop()

    def agregar_producto(self):
        """
        Obtiene el producto y cantidad desde las entradas y solicita
        al controlador que agregue el producto al inventario.
        """
        item = self.entrada_producto.get()
        try:
            cantidad = int(self.entrada_cantidad.get())
            mensaje = self.controlador.agregar_nuevo_item(item, cantidad)
            messagebox.showinfo("Agregado", mensaje)
            self.texto_salida.insert(tk.END, f"{mensaje}\n")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida")

    def eliminar_producto(self):
        """
        Obtiene el producto y cantidad desde las entradas y solicita
        al controlador que elimine el producto del inventario.
        """
        item = self.entrada_producto.get()
        try:
            cantidad = int(self.entrada_cantidad.get())
            mensaje = self.controlador.eliminar_item_existente(item, cantidad)
            messagebox.showinfo("Eliminado", mensaje)
            self.texto_salida.insert(tk.END, f"{mensaje}\n")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida")

    def mostrar_inventario(self):
        """
        Solicita al controlador la lista de productos en el inventario
        y los muestra en el área de salida.
        """
        self.texto_salida.delete("1.0", tk.END)
        items = self.controlador.listar_items()
        if not items:
            self.texto_salida.insert(tk.END, "Inventario vacío.\n")
        else:
            for item, cantidad in items.items():
                self.texto_salida.insert(tk.END, f"{item}: {cantidad}\n")

    def modificar_item(self):
        """
        Modifica el nombre y/o cantidad de un producto existente en el inventario.
        """
        nombre_antiguo = self.entrada_producto.get()
        nuevo_nombre = self.entrada_nuevo_nombre.get()
        try:
            nueva_cantidad = int(self.entrada_cantidad.get())

            if not nuevo_nombre.strip():
                nuevo_nombre = nombre_antiguo

            mensaje = self.controlador.modificar_item_existente(
                nombre_antiguo, nuevo_nombre, nueva_cantidad
            )
            self.texto_salida.insert(tk.END, mensaje + "\n")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero.")

    def limpiar_campos(self):
        """
        Limpia los campos de entrada de la interfaz gráfica.
        """
        self.entrada_producto.delete(0, tk.END)
        self.entrada_cantidad.delete(0, tk.END)
        self.entrada_nuevo_nombre.delete(0, tk.END)
