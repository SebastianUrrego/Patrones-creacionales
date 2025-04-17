# model.py
import abc

# --- Definición de los productos (componentes de la UI) ---

class Menu(abc.ABC):
    """
    Interfaz abstracta para un menú en la UI.
    """
    @abc.abstractmethod
    def get_details(self) -> str:
        pass

class AccessComponent(abc.ABC):
    """
    Interfaz abstracta para un componente de acceso o botones de acción.
    """
    @abc.abstractmethod
    def get_details(self) -> str:
        pass

class Report(abc.ABC):
    """
    Interfaz abstracta para un reporte o sección informativa en la UI.
    """
    @abc.abstractmethod
    def get_details(self) -> str:
        pass

# --- Implementaciones concretas para el rol "Cajero" ---

class CashierMenu(Menu):
    def get_details(self) -> str:
        return "Menú Cajero: [Vender Boletos, Consultar Ventas, Cerrar Caja]"

class CashierAccessComponent(AccessComponent):
    def get_details(self) -> str:
        return "Acceso Cajero: Botón de Transacción Rápida"

class CashierReport(Report):
    def get_details(self) -> str:
        return "Reporte Cajero: [Resumen de Ventas del Día]"

# --- Implementaciones concretas para el rol "Gerente" ---

class ManagerMenu(Menu):
    def get_details(self) -> str:
        return "Menú Gerente: [Reportes Financieros, Gestión de Personal, Análisis de Rendimiento]"

class ManagerAccessComponent(AccessComponent):
    def get_details(self) -> str:
        return "Acceso Gerente: Botón de Ajustes Estratégicos"

class ManagerReport(Report):
    def get_details(self) -> str:
        return "Reporte Gerente: [Informe Integral de Operación del Cine]"

# --- Definición del Abstract Factory ---

class RoleUIFactory(abc.ABC):
    """
    Interfaz Abstract Factory para generar familias de componentes de UI.
    """
    @abc.abstractmethod
    def create_menu(self) -> Menu:
        pass
    
    @abc.abstractmethod
    def create_access_component(self) -> AccessComponent:
        pass
    
    @abc.abstractmethod
    def create_report(self) -> Report:
        pass

# --- Factorías concretas para cada rol ---

class CashierUIFactory(RoleUIFactory):
    def create_menu(self) -> Menu:
        return CashierMenu()
    
    def create_access_component(self) -> AccessComponent:
        return CashierAccessComponent()
    
    def create_report(self) -> Report:
        return CashierReport()

class ManagerUIFactory(RoleUIFactory):
    def create_menu(self) -> Menu:
        return ManagerMenu()
    
    def create_access_component(self) -> AccessComponent:
        return ManagerAccessComponent()
    
    def create_report(self) -> Report:
        return ManagerReport()
