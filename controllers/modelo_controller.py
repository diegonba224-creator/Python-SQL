# controllers/modelo_controller.py
from tkinter import messagebox
from models.modelo import Modelo

class ModeloController:
    def __init__(self, main_controller):
        self.main = main_controller
        self.view = None
        
    def set_view(self, view):
        """Establece la vista asociada"""
        self.view = view
        
    def guardar(self):
        """Guarda un nuevo modelo"""
        if not self.view:
            return
            
        try:
            # Crear objeto modelo
            modelo = Modelo()
            modelo.codigo_unico = self.view.entries['codigo_unico'].get()
            modelo.nombre = self.view.entries['nombre'].get()
            modelo.categoria = self.view.entries['categoria'].get()
            modelo.versiones = self.view.entries['versiones'].get()
            modelo.especificaciones = self.view.entries['especificaciones'].get()
            modelo.componentes = self.view.entries['componentes'].get()
            modelo.tiempo_estandar = self.view.entries['tiempo'].get() or None
            
            # Validar campos obligatorios
            if not modelo.codigo_unico or not modelo.nombre or not modelo.categoria:
                messagebox.showwarning("Advertencia", "Código, Nombre y Categoría son obligatorios")
                return
            
            # Guardar en BD
            if modelo.guardar():
                messagebox.showinfo("Éxito", f"Modelo guardado con ID: {modelo.id}")
                self.view.limpiar_campos()
                self.mostrar_todos()
                self.main.update_status(f"Modelo {modelo.codigo_unico} guardado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo guardar el modelo")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {str(e)}")
            
    def actualizar(self):
        """Actualiza un modelo existente"""
        if not self.view or not self.view.selected_id:
            messagebox.showwarning("Advertencia", "Seleccione un modelo para actualizar")
            return
            
        try:
            modelo = Modelo()
            modelo.id = self.view.selected_id
            modelo.codigo_unico = self.view.entries['codigo_unico'].get()
            modelo.nombre = self.view.entries['nombre'].get()
            modelo.categoria = self.view.entries['categoria'].get()
            modelo.versiones = self.view.entries['versiones'].get()
            modelo.especificaciones = self.view.entries['especificaciones'].get()
            modelo.componentes = self.view.entries['componentes'].get()
            modelo.tiempo_estandar = self.view.entries['tiempo'].get() or None
            
            if modelo.actualizar():
                messagebox.showinfo("Éxito", "Modelo actualizado correctamente")
                self.view.limpiar_campos()
                self.mostrar_todos()
                self.main.update_status(f"Modelo {modelo.codigo_unico} actualizado")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el modelo")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al actualizar: {str(e)}")
            
    def eliminar(self):
        """Elimina un modelo"""
        if not self.view or not self.view.selected_id:
            messagebox.showwarning("Advertencia", "Seleccione un modelo para eliminar")
            return
            
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este modelo?"):
            try:
                modelo = Modelo()
                modelo.id = self.view.selected_id
                
                if modelo.eliminar():
                    messagebox.showinfo("Éxito", "Modelo eliminado correctamente")
                    self.view.limpiar_campos()
                    self.mostrar_todos()
                    self.main.update_status("Modelo eliminado")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el modelo")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error al eliminar: {str(e)}")
                
    def mostrar_todos(self):
        """Muestra todos los modelos"""
        try:
            datos = Modelo.obtener_todos()
            if datos:
                self.view.cargar_datos(datos)
                self.main.update_status(f"Mostrando {len(datos)} modelos")
            else:
                self.view.cargar_datos([])
                self.main.update_status("No hay modelos para mostrar")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos: {str(e)}")
            
    def cargar_para_editar(self, modelo_id):
        """Carga los datos de un modelo en el formulario para editar"""
        try:
            datos = Modelo.obtener_por_id(modelo_id)
            if datos:
                # Limpiar campos
                self.view.limpiar_campos()
                
                # Cargar datos
                self.view.entries['codigo_unico'].insert(0, datos['codigo_unico'] or '')
                self.view.entries['nombre'].insert(0, datos['nombre'] or '')
                self.view.entries['categoria'].insert(0, datos['categoria'] or '')
                self.view.entries['versiones'].insert(0, datos['versiones'] or '')
                self.view.entries['especificaciones'].insert(0, datos['especificaciones_tecnicas'] or '')
                self.view.entries['componentes'].insert(0, datos['componentes_requeridos'] or '')
                if datos['tiempo_estandar_ensamblaje']:
                    self.view.entries['tiempo'].insert(0, str(datos['tiempo_estandar_ensamblaje']))
                    
                self.main.update_status(f"Editando modelo: {datos['codigo_unico']}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar datos para editar: {str(e)}")
            