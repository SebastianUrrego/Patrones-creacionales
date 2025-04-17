# model.py
import abc

class Combo:
    """
    Producto final que representa un combo de cine.
    Contiene una lista de items (bebidas, perros, nachos, crispetas, etc.).
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        """
        Devuelve una cadena con la descripción de los ítems del combo.
        """
        if not self.items:
            return "El combo está vacío."
        return "Combo incluye:\n" + "\n".join(f"- {item}" for item in self.items)

class ComboBuilder(abc.ABC):
    """
    Builder abstracto que define la interfaz para construir un Combo.
    """
    def __init__(self):
        self.combo = Combo()

    @abc.abstractmethod
    def build_items(self):
        """
        Método para agregar los ítems específicos de cada combo.
        """
        pass

    def get_combo(self):
        """
        Retorna el combo construido.
        """
        return self.combo

# ---- Builders concretos para cada tipo de combo ----

class ComboProParaDosBuilder(ComboBuilder):
    """
    Combo Pro para dos:
    - Crispeta mediana de sal 120 g
    - 2 Gaseosas medianas 960 ml
    - 2 Perros calientes o sándwiches
    """
    def build_items(self):
        self.combo.items.append("Crispeta mediana de sal (120 g)")
        self.combo.items.append("Gaseosa mediana (960 ml)")
        self.combo.items.append("Gaseosa mediana (960 ml)")
        self.combo.items.append("Perro caliente / Sándwich")
        self.combo.items.append("Perro caliente / Sándwich")

class ComboFanParaDosBuilder(ComboBuilder):
    """
    Combo Fan para dos:
    - Crispeta grande de sal 150 g
    - 2 Gaseosas medianas 960 ml
    """
    def build_items(self):
        self.combo.items.append("Crispeta grande de sal (150 g)")
        self.combo.items.append("Gaseosa mediana (960 ml)")
        self.combo.items.append("Gaseosa mediana (960 ml)")

class ComboProBuilder(ComboBuilder):
    """
    Combo Pro:
    - Crispeta grande de sal 100 g
    - 1 Gaseosa mediana 960 ml
    - 1 Perro caliente o sándwich
    """
    def build_items(self):
        self.combo.items.append("Crispeta grande de sal (100 g)")
        self.combo.items.append("Gaseosa mediana (960 ml)")
        self.combo.items.append("Perro caliente / Sándwich")

class ComboFanBuilder(ComboBuilder):
    """
    Combo Fan:
    - 1 Crispeta mediana de sal 100 g
    - 1 Gaseosa pequeña 640 ml
    """
    def build_items(self):
        self.combo.items.append("Crispeta mediana de sal (100 g)")
        self.combo.items.append("Gaseosa pequeña (640 ml)")

class ComboFanJuniorBuilder(ComboBuilder):
    """
    Combo Fan Junior:
    - 1 Caja de crispetas de sal 55 g
    - 1 Gaseosa pequeña 640 ml
    """
    def build_items(self):
        self.combo.items.append("Caja crispetas de sal (55 g)")
        self.combo.items.append("Gaseosa pequeña (640 ml)")

class ComboPersonalizadoBuilder(ComboBuilder):
    """
    Builder para un combo personalizado según las opciones seleccionadas por el usuario.
    """
    def __init__(self, items_seleccionados):
        super().__init__()
        self.items_seleccionados = items_seleccionados

    def build_items(self):
        """
        Agrega únicamente los ítems que el usuario haya marcado.
        """
        # Mapear nombres más descriptivos si es necesario
        item_descriptions = {
            "bebida": "Gaseosa mediana (960 ml)",
            "perro": "Perro caliente / Sándwich",
            "nachos": "Nachos con queso",
            "crispetas": "Crispetas de sal (medianas)"
        }
        for key in self.items_seleccionados:
            if key in item_descriptions:
                self.combo.items.append(item_descriptions[key])
            else:
                self.combo.items.append(key)  # Por si hay otras opciones futuras

# ---- Director ----

class ComboDirector:
    """
    Director que coordina la secuencia de construcción del combo.
    """
    def __init__(self, builder: ComboBuilder):
        self.builder = builder

    def construct_combo(self):
        """
        Llama al builder para agregar ítems específicos del combo.
        """
        self.builder.build_items()
        return self.builder.get_combo()
