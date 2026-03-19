# views/main_view.py
import tkinter as tk
from tkinter import ttk, messagebox
from config import Config
from views.modelo_view import ModeloView
from views.linea_view import LineaView
from views.componente_view import ComponenteView
from views.orden_view import OrdenView

class MainView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title(Config.WINDOW_TITLE)
        self.root.geometry(Config.WINDOW_GEOMETRY)
        self.root.state('zoomed')
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        """Configura los estilos de la interfaz"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurar colores
        colors = Config.COLORS
        self.style.configure('Success.TButton', background=colors['success'])
        self.style.configure('Warning.TButton', background=colors['warning'])
        self.style.configure('Danger.TButton', background=colors['danger'])
        
    def create_widgets(self):
        """Crea los widgets de la ventana principal"""
        # Barra de menú
        self.create_menu()
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Crear vistas de cada módulo
        self.modelo_view = ModeloView(self.notebook, self.controller.modelo_controller)
        self.linea_view = LineaView(self.notebook, self.controller.linea_controller)
        self.componente_view = ComponenteView(self.notebook, self.controller.componente_controller)
        self.orden_view = OrdenView(self.notebook, self.controller.orden_controller)
        
        # Agregar pestañas
        self.notebook.add(self.modelo_view.frame, text="🚗 MODELOS")
        self.notebook.add(self.linea_view.frame, text="🏭 LÍNEAS")
        self.notebook.add(self.componente_view.frame, text="⚙️ COMPONENTES")
        self.notebook.add(self.orden_view.frame, text="📋 ÓRDENES")
        
        # Barra de estado
        self.create_status_bar()
        
    def create_menu(self):
        """Crea la barra de menú"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Configuración", command=self.controller.abrir_configuracion)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.controller.salir)
        
        # Menú Módulos
        modules_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Módulos", menu=modules_menu)
        modules_menu.add_command(label="Modelos", command=lambda: self.notebook.select(0))
        modules_menu.add_command(label="Líneas", command=lambda: self.notebook.select(1))
        modules_menu.add_command(label="Componentes", command=lambda: self.notebook.select(2))
        modules_menu.add_command(label="Órdenes", command=lambda: self.notebook.select(3))
        
        # Menú Ayuda
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.controller.acerca_de)
        
    def create_status_bar(self):
        """Crea la barra de estado"""
        self.status_bar = ttk.Label(self.root, text="Listo", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def update_status(self, message):
        """Actualiza el mensaje de la barra de estado"""
        self.status_bar.config(text=message)
        
    def run(self):
        """Inicia el bucle principal de la aplicación"""
        self.root.mainloop()
        