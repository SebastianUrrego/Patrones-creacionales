# model.py
import abc

class Ticket(abc.ABC):
    """
    Clase abstracta para representar un boleto.
    """
    @abc.abstractmethod
    def get_details(self):
        """
        Retorna una descripción o detalle del boleto.
        """
        pass

class TicketTradicional(Ticket):
    """
    Boleto Tradicional.
    """
    def get_details(self):
        return "Boleto Tradicional: Acceso estándar a la función."

class TicketMegaSala(Ticket):
    """
    Boleto para Mega Sala.
    """
    def get_details(self):
        return "Boleto Mega Sala: Función en sala extendida con mayor capacidad."

class TicketVip(Ticket):
    """
    Boleto VIP.
    """
    def get_details(self):
        return "Boleto VIP: Acceso a sala exclusiva con servicios especiales."

class Ticket3D(Ticket):
    """
    Boleto para función 3D.
    """
    def get_details(self):
        return "Boleto 3D: Experiencia inmersiva en 3D con tecnología de última generación."

class TicketFactory:
    """
    Fábrica para la creación de boletos según el tipo seleccionado.
    """
    @staticmethod
    def create_ticket(ticket_type: str) -> Ticket:
        ticket_type = ticket_type.lower()
        if ticket_type == "tradicional":
            return TicketTradicional()
        elif ticket_type == "mega sala" or ticket_type == "megásala":
            return TicketMegaSala()
        elif ticket_type == "vip":
            return TicketVip()
        elif ticket_type == "3d":
            return Ticket3D()
        else:
            raise ValueError("Tipo de boleto no válido.")
