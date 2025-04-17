# controller.py
from view import MovieFunctionView
from model import MovieFunction

class MovieFunctionController:
    def __init__(self, view: MovieFunctionView):
        self.view = view
        self.view.set_clone_callback(self.clone_function)
        
        # Definir prototipos predefinidos (configuraciones base)
        self.prototypes = {
            "Función 1": MovieFunction("Avatar", "Sala 1", "3D", ["18:00", "21:00"]),
            "Función 2": MovieFunction("Titanic", "Sala 2", "2D", ["17:00", "20:00"]),
            "Función 3": MovieFunction("Inception", "Sala 3", "IMAX", ["19:00", "22:00"]),
        }
        # Configurar las opciones del combobox en la vista
        self.view.set_prototype_options(list(self.prototypes.keys()))
    
    def clone_function(self):
        # Obtener el nombre del prototipo seleccionado
        selected_key = self.view.get_selected_prototype()
        if selected_key not in self.prototypes:
            self.view.display_cloned_function("Función base no encontrada.")
            return
        
        # Clonar la función base
        cloned_function = self.prototypes[selected_key].clone()
        
        # Obtener detalles opcionales ingresados por el usuario
        details = self.view.get_edit_details()
        cloned_function.update_details(
            pelicula=details["pelicula"],
            sala=details["sala"],
            formato=details["formato"],
            horarios=details["horarios"] if details["horarios"] else None
        )
        
        # Mostrar la configuración clonada en la interfaz
        self.view.display_cloned_function(cloned_function.get_details())

def main():
    view = MovieFunctionView()
    controller = MovieFunctionController(view)
    view.start()

if __name__ == "__main__":
    main()
