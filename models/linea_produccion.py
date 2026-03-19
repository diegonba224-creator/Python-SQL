# models/linea.py
from models.database import Database

class LineaProduccion:
    def __init__(self):
        self.db = Database()
        self.id = None
        self.numero_linea = None
        self.tipo_vehiculos = None
        self.capacidad_diaria = None
        self.numero_estaciones = None
        self.supervisor = None
        self.turno_activo = None
        self.estado_operativo = 'activo'
    
    @staticmethod
    def obtener_todas():
        """Obtiene todas las líneas de producción"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_lineas')
            return results[0] if results else []
        except Exception as e:
            print(f"Error al obtener líneas: {e}")
            return []
    
    @staticmethod
    def obtener_por_id(linea_id):
        """Obtiene una línea por su ID"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_linea_por_id', [linea_id])
            return results[0][0] if results and results[0] else None
        except Exception as e:
            print(f"Error al obtener línea: {e}")
            return None
    
    def guardar(self):
        """Guarda una nueva línea"""
        try:
            params = [
                self.numero_linea,
                self.tipo_vehiculos,
                self.capacidad_diaria,
                self.numero_estaciones,
                self.supervisor,
                self.turno_activo,
                self.estado_operativo
            ]
            results = self.db.execute_procedure('sp_crear_linea', params)
            if results and results[0]:
                self.id = results[0][0]['id']
                return True
            return False
        except Exception as e:
            print(f"Error al guardar línea: {e}")
            return False
    
    def actualizar(self):
        """Actualiza una línea existente"""
        try:
            params = [
                self.id,
                self.numero_linea,
                self.tipo_vehiculos,
                self.capacidad_diaria,
                self.numero_estaciones,
                self.supervisor,
                self.turno_activo,
                self.estado_operativo
            ]
            self.db.execute_procedure('sp_actualizar_linea', params)
            return True
        except Exception as e:
            print(f"Error al actualizar línea: {e}")
            return False
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado de la línea"""
        try:
            self.db.execute_procedure('sp_cambiar_estado_linea', [self.id, nuevo_estado])
            self.estado_operativo = nuevo_estado
            return True
        except Exception as e:
            print(f"Error al cambiar estado: {e}")
            return False
    
    def to_dict(self):
        """Convierte la línea a diccionario"""
        return {
            'id': self.id,
            'numero_linea': self.numero_linea,
            'tipo_vehiculos': self.tipo_vehiculos,
            'capacidad_diaria': self.capacidad_diaria,
            'numero_estaciones': self.numero_estaciones,
            'supervisor': self.supervisor,
            'turno_activo': self.turno_activo,
            'estado_operativo': self.estado_operativo
        }
    
    @staticmethod
    def from_dict(data):
        """Crea una línea desde un diccionario"""
        linea = LineaProduccion()
        linea.id = data.get('id')
        linea.numero_linea = data.get('numero_linea')
        linea.tipo_vehiculos = data.get('tipo_vehiculos_ensambla')
        linea.capacidad_diaria = data.get('capacidad_diaria')
        linea.numero_estaciones = data.get('numero_estaciones_trabajo')
        linea.supervisor = data.get('supervisor_responsable')
        linea.turno_activo = data.get('turno_activo')
        linea.estado_operativo = data.get('estado_operativo')
        return linea
    