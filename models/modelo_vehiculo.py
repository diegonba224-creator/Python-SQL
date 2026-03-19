# models/modelo.py
from models.database import Database

class Modelo:
    def __init__(self):
        self.db = Database()
        self.id = None
        self.codigo_unico = None
        self.nombre = None
        self.categoria = None
        self.versiones = None
        self.especificaciones = None
        self.componentes = None
        self.tiempo_estandar = None
    
    @staticmethod
    def obtener_todos():
        """Obtiene todos los modelos activos"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_modelos')
            return results[0] if results else []
        except Exception as e:
            print(f"Error al obtener modelos: {e}")
            return []
    
    @staticmethod
    def obtener_por_id(modelo_id):
        """Obtiene un modelo por su ID"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_modelo_por_id', [modelo_id])
            return results[0][0] if results and results[0] else None
        except Exception as e:
            print(f"Error al obtener modelo: {e}")
            return None
    
    def guardar(self):
        """Guarda un nuevo modelo"""
        try:
            params = [
                self.codigo_unico,
                self.nombre,
                self.categoria,
                self.versiones,
                self.especificaciones,
                self.componentes,
                self.tiempo_estandar
            ]
            results = self.db.execute_procedure('sp_crear_modelo', params)
            if results and results[0]:
                self.id = results[0][0]['id']
                return True
            return False
        except Exception as e:
            print(f"Error al guardar modelo: {e}")
            return False
    
    def actualizar(self):
        """Actualiza un modelo existente"""
        try:
            params = [
                self.id,
                self.codigo_unico,
                self.nombre,
                self.categoria,
                self.versiones,
                self.especificaciones,
                self.componentes,
                self.tiempo_estandar
            ]
            results = self.db.execute_procedure('sp_actualizar_modelo', params)
            return True
        except Exception as e:
            print(f"Error al actualizar modelo: {e}")
            return False
    
    def eliminar(self):
        """Elimina (desactiva) un modelo"""
        try:
            self.db.execute_procedure('sp_eliminar_modelo', [self.id])
            return True
        except Exception as e:
            print(f"Error al eliminar modelo: {e}")
            return False
    
    def to_dict(self):
        """Convierte el modelo a diccionario"""
        return {
            'id': self.id,
            'codigo_unico': self.codigo_unico,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'versiones': self.versiones,
            'especificaciones': self.especificaciones,
            'componentes': self.componentes,
            'tiempo_estandar': self.tiempo_estandar
        }
    
    @staticmethod
    def from_dict(data):
        """Crea un modelo desde un diccionario"""
        modelo = Modelo()
        modelo.id = data.get('id')
        modelo.codigo_unico = data.get('codigo_unico')
        modelo.nombre = data.get('nombre')
        modelo.categoria = data.get('categoria')
        modelo.versiones = data.get('versiones')
        modelo.especificaciones = data.get('especificaciones_tecnicas')
        modelo.componentes = data.get('componentes_requeridos')
        modelo.tiempo_estandar = data.get('tiempo_estandar_ensamblaje')
        return modelo
    