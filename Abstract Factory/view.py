# view.py
import tkinter as tk
from tkinter import ttk

class RoleUIView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Configuración de Interfaz por Rol - Abstract Factory")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Etiqueta para indicar la selección de rol
        self.label_role = ttk.Label(self.main_frame, text="Seleccione el rol de usuario:")
        self.label_role.pack(pady=(0, 10))
        
        # Combobox para selección del rol
        self.role_var = tk.StringVar()
        self.role_combo = ttk.Combobox(self.main_frame, textvariable=self.role_var, state='readonly')
        self.role_combo['values'] = ("Cajero", "Gerente")
        self.role_combo.current(0)
        self.role_combo.pack(pady=(0, 20))
        
        # Botón para generar la interfaz
        self.generate_button = ttk.Button(self.main_frame, text="Generar UI")
        self.generate_button.pack(pady=(0, 20))
        
        # Marco para mostrar los detalles de los componentes generados
        self.output_frame = ttk.LabelFrame(self.main_frame, text="Componentes de la UI", padding="10")
        self.output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_text = tk.Text(self.output_frame, height=10, wrap="word")
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.output_text.config(state=tk.DISABLED)
    
    def set_generate_callback(self, callback):
        """
        Asigna la función callback al botón para generar la UI.
        """
        self.generate_button.config(command=callback)
        
    def get_selected_role(self) -> str:
        """
        Retorna el rol seleccionado por el usuario.
        """
        return self.role_var.get()
    
    def display_ui_components(self, menu_details: str, access_details: str, report_details: str):
        """
        Muestra los detalles de los componentes generados en el área de salida.
        """
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        text = (
            f"{menu_details}\n\n"
            f"{access_details}\n\n"
            f"{report_details}"
        )
        self.output_text.insert(tk.END, text)
        self.output_text.config(state=tk.DISABLED)
    
    def start(self):
        """
        Inicia el ciclo principal de la interfaz gráfica.
        """
        self.root.mainloop()
