# models/orden.py
from models.database import Database

class OrdenProduccion:
    def __init__(self):
        self.db = Database()
        self.id = None
        self.numero_unico = None
        self.fecha_emision = None
        self.modelo_id = None
        self.cantidad = None
        self.fecha_inicio = None
        self.fecha_fin = None
        self.prioridad = 'normal'
        self.estado = 'pendiente'
    
    @staticmethod
    def obtener_todas():
        """Obtiene todas las órdenes"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_ordenes')
            return results[0] if results else []
        except Exception as e:
            print(f"Error al obtener órdenes: {e}")
            return []
    
    @staticmethod
    def obtener_por_id(orden_id):
        """Obtiene una orden por su ID"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_orden_por_id', [orden_id])
            return results[0][0] if results and results[0] else None
        except Exception as e:
            print(f"Error al obtener orden: {e}")
            return None
    
    @staticmethod
    def obtener_por_estado(estado):
        """Obtiene órdenes por estado"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_ordenes_por_estado', [estado])
            return results[0] if results else []
        except Exception as e:
            print(f"Error al obtener órdenes por estado: {e}")
            return []
    
    def guardar(self):
        """Guarda una nueva orden"""
        try:
            params = [
                self.numero_unico,
                self.fecha_emision,
                self.modelo_id,
                self.cantidad,
                self.fecha_inicio,
                self.fecha_fin,
                self.prioridad
            ]
            results = self.db.execute_procedure('sp_crear_orden', params)
            if results and results[0]:
                self.id = results[0][0]['id']
                return True
            return False
        except Exception as e:
            print(f"Error al guardar orden: {e}")
            return False
    
    def actualizar_estado(self, nuevo_estado):
        """Actualiza el estado de la orden"""
        try:
            self.db.execute_procedure('sp_actualizar_estado_orden', [self.id, nuevo_estado])
            self.estado = nuevo_estado
            return True
        except Exception as e:
            print(f"Error al actualizar estado: {e}")
            return False
    
    def to_dict(self):
        """Convierte la orden a diccionario"""
        return {
            'id': self.id,
            'numero_unico': self.numero_unico,
            'fecha_emision': self.fecha_emision,
            'modelo_id': self.modelo_id,
            'cantidad': self.cantidad,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'prioridad': self.prioridad,
            'estado': self.estado
        }
    
    @staticmethod
    def from_dict(data):
        """Crea una orden desde un diccionario"""
        orden = OrdenProduccion()
        orden.id = data.get('id')
        orden.numero_unico = data.get('numero_unico')
        orden.fecha_emision = data.get('fecha_emision')
        orden.modelo_id = data.get('modelo_vehiculo_id')
        orden.cantidad = data.get('cantidad_producir')
        orden.fecha_inicio = data.get('fecha_inicio_programada')
        orden.fecha_fin = data.get('fecha_finalizacion_estimada')
        orden.prioridad = data.get('prioridad')
        orden.estado = data.get('estado_actual')
        return orden
    