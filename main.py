# main.py
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.main_controller import MainController

def main():
    """Función principal de la aplicación"""
    try:
        # Crear y ejecutar el controlador principal
        app = MainController()
        app.run()
    except KeyboardInterrupt:
        print("\n👋 Aplicación terminada por el usuario")
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()
        input("Presione Enter para salir...")

if __name__ == "__main__":
    main()
    