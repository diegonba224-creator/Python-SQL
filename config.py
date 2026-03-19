# config.py
class Config:
    # Configuración de la base de datos
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': '',  # Cambiar por tu contraseña
        'database': 'autofactory'
    }
    
    # Configuración de la ventana
    WINDOW_TITLE = "🏭 Autofactory - Sistema de Gestión Automotriz"
    WINDOW_GEOMETRY = "1200x700"
    
    # Colores para la interfaz
    COLORS = {
        'primary': '#2196F3',
        'success': '#4CAF50',
        'warning': '#FF9800',
        'danger': '#f44336',
        'dark': '#333333',
        'light': '#f5f5f5'
    }
    