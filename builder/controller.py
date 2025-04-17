# controller.py
from view import ComboView
from model import (
    ComboDirector,
    ComboProParaDosBuilder,
    ComboFanParaDosBuilder,
    ComboProBuilder,
    ComboFanBuilder,
    ComboFanJuniorBuilder,
    ComboPersonalizadoBuilder
)

class ComboController:
    def __init__(self, view: ComboView):
        self.view = view
        
        # Definir las opciones de combos disponibles
        self.combo_options = [
            "Combo Pro para dos",
            "Combo Fan para dos",
            "Combo Pro",
            "Combo Fan",
            "Combo Fan Junior",
            "Personalizado"
        ]
        
        # Configurar la vista
        self.view.set_combo_options(self.combo_options)
        self.view.set_build_callback(self.on_build_combo)
    
    def on_build_combo(self):
        """
        Construye el combo según la selección del usuario.
        """
        selected_combo = self.view.get_selected_combo()
        
        if selected_combo.lower() == "combo pro para dos":
            builder = ComboProParaDosBuilder()
        elif selected_combo.lower() == "combo fan para dos":
            builder = ComboFanParaDosBuilder()
        elif selected_combo.lower() == "combo pro":
            builder = ComboProBuilder()
        elif selected_combo.lower() == "combo fan":
            builder = ComboFanBuilder()
        elif selected_combo.lower() == "combo fan junior":
            builder = ComboFanJuniorBuilder()
        elif selected_combo.lower() == "personalizado":
            # Recoger selección de checkboxes
            custom_items = self.view.get_custom_selections()
            builder = ComboPersonalizadoBuilder(custom_items)
        else:
            # Por si no coincide ninguna opción
            self.view.display_combo("Opción de combo no válida.")
            return
        
        # Usar Director para construir el combo
        director = ComboDirector(builder)
        combo = director.construct_combo()
        
        # Mostrar resultado
        self.view.display_combo(str(combo))

def main():
    view = ComboView()
    controller = ComboController(view)
    view.start()

if __name__ == "__main__":
    main()
