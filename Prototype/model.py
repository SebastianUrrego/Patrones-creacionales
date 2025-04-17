import copy

class MovieFunction:
    """
    Representa la configuración de una función de película.
    
    Atributos:
      - pelicula: Título de la película.
      - sala: Sala o número de sala.
      - formato: Formato de la función (ej. 2D, 3D, IMAX).
      - horarios: Lista de horarios en los que se proyecta.
    """
    def __init__(self, pelicula: str, sala: str, formato: str, horarios: list):
        self.pelicula = pelicula
        self.sala = sala
        self.formato = formato
        self.horarios = horarios

    def clone(self):
        """
        Realiza una copia profunda de la instancia para obtener un clon independiente.
        """
        return copy.deepcopy(self)

    def update_details(self, pelicula=None, sala=None, formato=None, horarios=None):
        """
        Actualiza los atributos de la configuración con los valores proporcionados.
        Solo se actualizan los campos en los que se ingrese valor.
        """
        if pelicula is not None and pelicula.strip() != "":
            self.pelicula = pelicula
        if sala is not None and sala.strip() != "":
            self.sala = sala
        if formato is not None and formato.strip() != "":
            self.formato = formato
        if horarios is not None and isinstance(horarios, list) and horarios:
            self.horarios = horarios

    def get_details(self):
        """
        Retorna una cadena formateada con los detalles de la función.
        """
        horarios_str = ", ".join(self.horarios) if self.horarios else "No definidos"
        return (
            f"Pelicula: {self.pelicula}\n"
            f"Sala: {self.sala}\n"
            f"Formato: {self.formato}\n"
            f"Horarios: {horarios_str}\n"
        )