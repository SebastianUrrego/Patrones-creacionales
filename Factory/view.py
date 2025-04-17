# view.py
import tkinter as tk
from tkinter import ttk, messagebox

class TicketView:
    """
    Vista: Interfaz gráfica avanzada para la creación de boletos.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Creación de Boletos - Patrón Factory (Interfaz Avanzada)")
        self.root.geometry("500x400")
        
        # Configuración de layout (grid)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Contenedor principal con padding
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        # Crear barra de menús
        self.create_menu()
        
        # Título de la aplicación
        self.title_label = ttk.Label(self.main_frame, text="Seleccione el tipo de boleto", font=("Helvetica", 16))
        self.title_label.grid(column=0, row=0, columnspan=2, pady=10)
        
        # Variable para almacenar la selección del boleto
        self.choice = tk.StringVar(value="tradicional")
        
        # Marco para opciones (radio buttons)
        self.radio_frame = ttk.LabelFrame(self.main_frame, text="Tipo de Boleto", padding="10 10 10 10")
        self.radio_frame.grid(column=0, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Radio buttons para cada tipo de boleto
        ttk.Radiobutton(
            self.radio_frame,
            text="Boleto Tradicional",
            variable=self.choice,
            value="tradicional"
        ).grid(column=0, row=0, sticky=tk.W, pady=2)
        
        ttk.Radiobutton(
            self.radio_frame,
            text="Boleto Mega Sala",
            variable=self.choice,
            value="mega sala"
        ).grid(column=0, row=1, sticky=tk.W, pady=2)
        
        ttk.Radiobutton(
            self.radio_frame,
            text="Boleto VIP",
            variable=self.choice,
            value="vip"
        ).grid(column=0, row=2, sticky=tk.W, pady=2)
        
        ttk.Radiobutton(
            self.radio_frame,
            text="Boleto 3D",
            variable=self.choice,
            value="3d"
        ).grid(column=0, row=3, sticky=tk.W, pady=2)
        
        # Botón para crear el boleto
        self.create_button = ttk.Button(self.main_frame, text="Crear Boleto")
        self.create_button.grid(column=0, row=2, pady=10)
        
        # Marco para mostrar el detalle del boleto
        self.output_frame = ttk.LabelFrame(self.main_frame, text="Detalle del Boleto", padding="10 10 10 10")
        self.output_frame.grid(column=0, row=3, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        self.output_text = tk.Text(self.output_frame, height=5, wrap="word")
        self.output_text.grid(column=0, row=0, sticky=(tk.W, tk.E))
        self.output_text.config(state=tk.DISABLED)
        
        # Ajuste de padding para todos los widgets
        for child in self.main_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def create_menu(self):
        """
        Crea la barra de menús con las opciones 'Archivo' y 'Ayuda'.
        """
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # Menú Archivo
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Salir", command=self.root.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=file_menu)
        
        # Menú Ayuda
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        self.menu_bar.add_cascade(label="Ayuda", menu=help_menu)
    
    def show_about(self):
        """
        Muestra información acerca de la aplicación.
        """
        messagebox.showinfo("Acerca de", "Aplicación de Creación de Boletos\nPatrón Factory - Interfaz Avanzada\nVersión 1.0")
    
    def set_create_callback(self, callback):
        """
        Asigna una función callback al botón 'Crear Boleto'.
        """
        self.create_button.config(command=callback)
    
    def get_selected_type(self) -> str:
        """
        Retorna el tipo de boleto seleccionado.
        """
        return self.choice.get()
    
    def display_ticket(self, ticket_details: str):
        """
        Muestra el detalle del boleto en el área de salida.
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, ticket_details)
        self.output_text.config(state=tk.DISABLED)
    
    def start(self):
        """
        Inicia el ciclo principal de la interfaz gráfica.
        """
        self.root.mainloop()
