# models/componente.py
from models.database import Database

class Componente:
    def __init__(self):
        self.db = Database()
        self.id = None
        self.codigo_unico = None
        self.descripcion = None
        self.categoria = None
        self.especificaciones = None
        self.proveedor = None
        self.tiempo_entrega = None
        self.costo_unitario = None
        self.stock_minimo = None
    
    @staticmethod
    def obtener_todos():
        """Obtiene todos los componentes"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_componentes')
            return results[0] if results else []
        except Exception as e:
            print(f"Error al obtener componentes: {e}")
            return []
    
    @staticmethod
    def obtener_por_id(componente_id):
        """Obtiene un componente por su ID"""
        db = Database()
        try:
            results = db.execute_procedure('sp_obtener_componente_por_id', [componente_id])
            return results[0][0] if results and results[0] else None
        except Exception as e:
            print(f"Error al obtener componente: {e}")
            return None
    
    def guardar(self):
        """Guarda un nuevo componente"""
        try:
            params = [
                self.codigo_unico,
                self.descripcion,
                self.categoria,
                self.especificaciones,
                self.proveedor,
                self.tiempo_entrega,
                self.costo_unitario,
                self.stock_minimo
            ]
            results = self.db.execute_procedure('sp_crear_componente', params)
            if results and results[0]:
                self.id = results[0][0]['id']
                return True
            return False
        except Exception as e:
            print(f"Error al guardar componente: {e}")
            return False
    
    def actualizar(self):
        """Actualiza un componente existente"""
        try:
            params = [
                self.id,
                self.codigo_unico,
                self.descripcion,
                self.categoria,
                self.especificaciones,
                self.proveedor,
                self.tiempo_entrega,
                self.costo_unitario,
                self.stock_minimo
            ]
            self.db.execute_procedure('sp_actualizar_componente', params)
            return True
        except Exception as e:
            print(f"Error al actualizar componente: {e}")
            return False
    
    def to_dict(self):
        """Convierte el componente a diccionario"""
        return {
            'id': self.id,
            'codigo_unico': self.codigo_unico,
            'descripcion': self.descripcion,
            'categoria': self.categoria,
            'especificaciones': self.especificaciones,
            'proveedor': self.proveedor,
            'tiempo_entrega': self.tiempo_entrega,
            'costo_unitario': self.costo_unitario,
            'stock_minimo': self.stock_minimo
        }
    
    @staticmethod
    def from_dict(data):
        """Crea un componente desde un diccionario"""
        comp = Componente()
        comp.id = data.get('id')
        comp.codigo_unico = data.get('codigo_unico')
        comp.descripcion = data.get('descripcion')
        comp.categoria = data.get('categoria')
        comp.especificaciones = data.get('especificaciones_tecnicas')
        comp.proveedor = data.get('proveedor_principal')
        comp.tiempo_entrega = data.get('tiempo_entrega_promedio')
        comp.costo_unitario = data.get('costo_unitario')
        comp.stock_minimo = data.get('stock_minimo_requerido')
        return comp
    