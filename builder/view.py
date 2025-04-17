# view.py
import tkinter as tk
from tkinter import ttk

class ComboView:
    """
    Vista para la creación de combos usando el Patrón Builder.
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Armar Combos - Patrón Builder")
        self.root.geometry("550x400")
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label de título
        self.label_title = ttk.Label(self.main_frame, text="Seleccione el tipo de combo:", font=("Arial", 14))
        self.label_title.pack(pady=5)
        
        # Combobox para la selección de combo
        self.combo_var = tk.StringVar()
        self.combos_box = ttk.Combobox(self.main_frame, textvariable=self.combo_var, state="readonly")
        self.combos_box.pack(pady=5)
        
        # Frame para la sección de "combo personalizado"
        self.custom_frame = ttk.LabelFrame(self.main_frame, text="Personalizar combo")
        
        # Checkboxes
        self.var_bebida = tk.BooleanVar()
        self.var_perro = tk.BooleanVar()
        self.var_nachos = tk.BooleanVar()
        self.var_crispetas = tk.BooleanVar()
        
        self.check_bebida = ttk.Checkbutton(self.custom_frame, text="Bebida", variable=self.var_bebida)
        self.check_perro = ttk.Checkbutton(self.custom_frame, text="Perro", variable=self.var_perro)
        self.check_nachos = ttk.Checkbutton(self.custom_frame, text="Nachos", variable=self.var_nachos)
        self.check_crispetas = ttk.Checkbutton(self.custom_frame, text="Crispetas", variable=self.var_crispetas)
        
        self.check_bebida.pack(anchor="w", pady=2)
        self.check_perro.pack(anchor="w", pady=2)
        self.check_nachos.pack(anchor="w", pady=2)
        self.check_crispetas.pack(anchor="w", pady=2)
        
        # Por defecto, el frame no se muestra
        self.custom_frame.pack_forget()
        
        # Botón para construir combo
        self.build_button = ttk.Button(self.main_frame, text="Construir Combo")
        self.build_button.pack(pady=10)
        
        # Text area para mostrar el resultado
        self.output_area = tk.Text(self.main_frame, height=8, wrap="word")
        self.output_area.pack(fill=tk.BOTH, expand=True, pady=(0,10))
        self.output_area.config(state=tk.DISABLED)
        
        # Vincular evento para cuando cambie la selección del ComboBox
        self.combos_box.bind("<<ComboboxSelected>>", self.on_combobox_change)
    
    def on_combobox_change(self, event):
        """
        Se ejecuta cuando el usuario selecciona un combo.
        Muestra u oculta las opciones de personalización.
        """
        selected = self.combo_var.get()
        if selected.lower() == "personalizado":
            self.custom_frame.pack(fill=tk.X, pady=5)
        else:
            self.custom_frame.pack_forget()
    
    def set_combo_options(self, options):
        """
        Define las opciones disponibles en el ComboBox.
        """
        self.combos_box['values'] = options
        if options:
            self.combos_box.current(0)  # Selecciona la primera por defecto
    
    def set_build_callback(self, callback):
        """
        Asigna la función callback al botón "Construir Combo".
        """
        self.build_button.config(command=callback)
    
    def get_selected_combo(self):
        """
        Retorna la opción de combo seleccionada en el ComboBox.
        """
        return self.combo_var.get()
    
    def get_custom_selections(self):
        """
        Retorna un listado de los ítems seleccionados en el combo personalizado.
        """
        selected_items = []
        if self.var_bebida.get():
            selected_items.append("bebida")
        if self.var_perro.get():
            selected_items.append("perro")
        if self.var_nachos.get():
            selected_items.append("nachos")
        if self.var_crispetas.get():
            selected_items.append("crispetas")
        return selected_items
    
    def display_combo(self, combo_str):
        """
        Muestra la descripción del combo en el área de texto.
        """
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, combo_str)
        self.output_area.config(state=tk.DISABLED)
    
    def start(self):
        self.root.mainloop()
