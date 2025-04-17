# view.py
import tkinter as tk
from tkinter import ttk

class MovieFunctionView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clonación de Configuraciones de Funciones de Películas - Prototype Pattern")
        self.root.geometry("600x500")
        
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título de la aplicación
        self.title_label = ttk.Label(self.main_frame, text="Clonación de Funciones de Películas", font=("Helvetica", 16))
        self.title_label.pack(pady=(0, 10))
        
        # Sección para seleccionar la función base
        self.select_frame = ttk.LabelFrame(self.main_frame, text="Seleccionar Función Base", padding="10")
        self.select_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.base_label = ttk.Label(self.select_frame, text="Función Base:")
        self.base_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.base_var = tk.StringVar()
        self.base_combobox = ttk.Combobox(self.select_frame, textvariable=self.base_var, state="readonly")
        self.base_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Sección para editar datos de la función clonada (opcional)
        self.edit_frame = ttk.LabelFrame(self.main_frame, text="Editar Detalles (Opcional)", padding="10")
        self.edit_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Campo para Película
        self.label_movie = ttk.Label(self.edit_frame, text="Película:")
        self.label_movie.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_movie = ttk.Entry(self.edit_frame, width=40)
        self.entry_movie.grid(row=0, column=1, padx=5, pady=5)
        
        # Campo para Sala
        self.label_room = ttk.Label(self.edit_frame, text="Sala:")
        self.label_room.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_room = ttk.Entry(self.edit_frame, width=40)
        self.entry_room.grid(row=1, column=1, padx=5, pady=5)
        
        # Campo para Formato
        self.label_format = ttk.Label(self.edit_frame, text="Formato:")
        self.label_format.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_format = ttk.Entry(self.edit_frame, width=40)
        self.entry_format.grid(row=2, column=1, padx=5, pady=5)
        
        # Campo para Horarios
        self.label_schedule = ttk.Label(self.edit_frame, text="Horarios (separados por coma):")
        self.label_schedule.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_schedule = ttk.Entry(self.edit_frame, width=40)
        self.entry_schedule.grid(row=3, column=1, padx=5, pady=5)
        
        # Botón para clonar la función
        self.clone_button = ttk.Button(self.main_frame, text="Clonar Función")
        self.clone_button.pack(pady=10)
        
        # Área para mostrar el resultado de la función clonada
        self.result_frame = ttk.LabelFrame(self.main_frame, text="Detalles de la Función Clonada", padding="10")
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.result_text = tk.Text(self.result_frame, height=10, wrap="word")
        self.result_text.pack(fill=tk.BOTH, expand=True)
        self.result_text.config(state=tk.DISABLED)
    
    def set_clone_callback(self, callback):
        """
        Asigna la función callback al botón "Clonar Función".
        """
        self.clone_button.config(command=callback)
        
    def set_prototype_options(self, options):
        """
        Establece las opciones del combobox de función base.
        'options' es una lista de strings.
        """
        self.base_combobox['values'] = options
        if options:
            self.base_combobox.current(0)
    
    def get_selected_prototype(self):
        """
        Retorna el nombre del prototipo seleccionado.
        """
        return self.base_var.get()
    
    def get_edit_details(self):
        """
        Retorna un diccionario con los detalles ingresados en los campos de edición.
        """
        movie = self.entry_movie.get().strip()
        room = self.entry_room.get().strip()
        formato = self.entry_format.get().strip()
        schedule_str = self.entry_schedule.get().strip()
        schedule = [s.strip() for s in schedule_str.split(",")] if schedule_str else []
        return {
            "pelicula": movie,
            "sala": room,
            "formato": formato,
            "horarios": schedule
        }
    
    def display_cloned_function(self, details):
        """
        Muestra los detalles de la función clonada en el área de resultado.
        """
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, details)
        self.result_text.config(state=tk.DISABLED)
    
    def start(self):
        """
        Inicia el ciclo principal de la interfaz gráfica.
        """
        self.root.mainloop()
