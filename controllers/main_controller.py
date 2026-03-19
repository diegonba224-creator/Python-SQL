# controllers/main_controller.py
from tkinter import messagebox
from models.database import Database
from controllers.modelo_controller import ModeloController
from controllers.linea_controller import LineaController
from controllers.componente_controller import ComponenteController
from controllers.orden_controller import OrdenController
from views.main_view import MainView
from config import Config

class MainController:
    def __init__(self):
        # Inicializar base de datos
        self.db = Database(Config.DB_CONFIG)
        if not self.db.connect():
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            return
        
        # Inicializar controladores de módulos
        self.modelo_controller = ModeloController(self)
        self.linea_controller = LineaController(self)
        self.componente_controller = ComponenteController(self)
        self.orden_controller = OrdenController(self)
        
        # Inicializar vista
        self.view = MainView(self)
        
    def run(self):
        """Inicia la aplicación"""
        self.view.run()
        
    def salir(self):
        """Cierra la aplicación"""
        if messagebox.askyesno("Confirmar", "¿Está seguro de salir?"):
            self.db.disconnect()
            self.view.root.quit()
            
    def abrir_configuracion(self):
        """Abre la ventana de configuración"""
        messagebox.showinfo("Configuración", "Funcionalidad en desarrollo")
        
    def acerca_de(self):
        """Muestra información sobre la aplicación"""
        messagebox.showinfo(
            "Acerca de Autofactory",
            "Autofactory - Sistema de Gestión Automotriz\n\n"
            "Versión 1.0\n"
            "Desarrollado con Python, Tkinter y MySQL\n\n"
            "© 2024 Todos los derechos reservados"
        )
        
    def update_status(self, message):
        """Actualiza la barra de estado"""
        self.view.update_status(message)
        