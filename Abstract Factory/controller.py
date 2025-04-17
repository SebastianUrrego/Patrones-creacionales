# controller.py
from view import RoleUIView
from model import CashierUIFactory, ManagerUIFactory

class RoleUIController:
    def __init__(self, view: RoleUIView):
        self.view = view
        self.view.set_generate_callback(self.generate_ui)
    
    def generate_ui(self):
        """
        Según el rol seleccionado, utiliza la factoría correspondiente para 
        generar los componentes de la UI y los muestra en la vista.
        """
        selected_role = self.view.get_selected_role()
        if selected_role.lower() == "cajero":
            factory = CashierUIFactory()
        elif selected_role.lower() == "gerente":
            factory = ManagerUIFactory()
        else:
            # Por defecto se usa la factoría de Cajero
            factory = CashierUIFactory()
        
        # Crear la familia de productos
        menu_component = factory.create_menu()
        access_component = factory.create_access_component()
        report_component = factory.create_report()
        
        # Pasar los detalles a la vista para mostrar
        self.view.display_ui_components(
            menu_component.get_details(),
            access_component.get_details(),
            report_component.get_details()
        )

def main():
    view = RoleUIView()
    controller = RoleUIController(view)
    view.start()

if __name__ == "__main__":
    main()
