# controller.py
from view import TicketView
from model import TicketFactory

class TicketController:
    """
    Controlador que coordina la creación de boletos entre la Vista (interfaz gráfica)
    y el Modelo (fábrica y clases de boletos).
    """
    def __init__(self, view: TicketView):
        self.view = view
        self.view.set_create_callback(self.create_ticket)
    
    def create_ticket(self):
        """
        Obtiene la opción seleccionada, utiliza la fábrica para crear el boleto y
        muestra los detalles en la interfaz.
        """
        ticket_type = self.view.get_selected_type()
        try:
            ticket = TicketFactory.create_ticket(ticket_type)
            self.view.display_ticket(ticket.get_details())
        except ValueError as e:
            self.view.display_ticket(str(e))

def main():
    view = TicketView()
    controller = TicketController(view)
    view.start()

if __name__ == "__main__":
    main()
