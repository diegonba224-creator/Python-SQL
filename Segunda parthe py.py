import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from tabulate import tabulate
from tkcalendar import DateEntry
from datetime import datetime

# =====================================================
# CLASE PARA CONEXIÓN A BASE DE DATOS
# =====================================================
class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("✅ Conexión establecida a la base de datos")
        except mysql.connector.Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            messagebox.showerror("Error de conexión", f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("🔌 Conexión cerrada")

    def execute_procedure(self, procedure_name, *args):
        try:
            self.cursor.callproc(procedure_name, args)
            results = []
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    headers = [i[0] for i in result.description]
                    results.append((headers, rows))
            self.connection.commit()
            return results
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"❌ Error al ejecutar el procedimiento {procedure_name}: {e}")
            messagebox.showerror("Error", f"Error al ejecutar el procedimiento {procedure_name}: {e}")
            return None

    def execute_procedure_single(self, procedure_name, *args):
        """Ejecuta procedimiento y retorna solo el primer resultado"""
        try:
            self.cursor.callproc(procedure_name, args)
            result = None
            for stored_result in self.cursor.stored_results():
                result = stored_result.fetchone()
                break
            self.connection.commit()
            return result
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"❌ Error al ejecutar el procedimiento {procedure_name}: {e}")
            messagebox.showerror("Error", f"Error al ejecutar el procedimiento {procedure_name}: {e}")
            return None


# =====================================================
# CLASE PRINCIPAL DE LA APLICACIÓN
# =====================================================
class AutoFactoryApp(tk.Tk):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector
        self.title("AutoFactory - Sistema de Gestión Automotriz")
        self.geometry("1100x700")
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Crear el notebook (pestañas)
        self.create_notebook()
        
        # Inicializar datos
        self.cargar_datos_iniciales()

    def create_notebook(self):
        """Crea las pestañas de la aplicación"""
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Crear las pestañas
        self.tab_modelos = ttk.Frame(self.notebook)
        self.tab_lineas = ttk.Frame(self.notebook)
        self.tab_componentes = ttk.Frame(self.notebook)
        self.tab_ordenes = ttk.Frame(self.notebook)

        # Añadir pestañas al notebook
        self.notebook.add(self.tab_modelos, text="🚗 Modelos de Vehículos")
        self.notebook.add(self.tab_lineas, text="🏭 Líneas Producción")
        self.notebook.add(self.tab_componentes, text="🔧 Componentes")
        self.notebook.add(self.tab_ordenes, text="📋 Órdenes Producción")

        # Configurar cada pestaña
        self.setup_tab_modelos()
        self.setup_tab_lineas()
        self.setup_tab_componentes()
        self.setup_tab_ordenes()

    def cargar_datos_iniciales(self):
        """Carga los datos iniciales en los comboboxes"""
        self.cargar_modelos_combobox()
        self.cargar_lineas_combobox()

    def cargar_modelos_combobox(self):
        """Carga los modelos en los comboboxes"""
        results = self.db_connector.execute_procedure('sp_obtener_modelos')
        if results:
            for headers, rows in results:
                modelos = [f"{row[0]} - {row[2]}" for row in rows]  # ID - Nombre
                if hasattr(self, 'modelo_orden'):
                    self.modelo_orden['values'] = modelos

    def cargar_lineas_combobox(self):
        """Carga las líneas en los comboboxes"""
        results = self.db_connector.execute_procedure('sp_obtener_lineas')
        if results:
            for headers, rows in results:
                lineas = [f"{row[0]} - Línea {row[1]}" for row in rows]
                if hasattr(self, 'linea_prod'):
                    self.linea_prod['values'] = lineas


    # =====================================================
    # PESTAÑA 1: MODELOS DE VEHÍCULOS
    # =====================================================
    def setup_tab_modelos(self):
        """Configura la pestaña de modelos de vehículos"""
        # Título
        titulo = tk.Label(self.tab_modelos, text="GESTIÓN DE MODELOS DE VEHÍCULOS", 
                         font=("Arial", 16, "bold"), fg="#2c3e50")
        titulo.pack(pady=10)

        # Frame para el formulario
        form_frame = ttk.LabelFrame(self.tab_modelos, text="Datos del Modelo", padding=10)
        form_frame.pack(fill="x", padx=20, pady=10)

        # Campos del formulario
        self.modelo_fields = {}
        campos = [
            ("Código Único:", "codigo_unico", 0),
            ("Nombre:", "nombre", 1),
            ("Categoría:", "categoria", 2),
            ("Versiones:", "versiones", 3),
            ("Especificaciones Técnicas:", "especificaciones", 4),
            ("Componentes Requeridos:", "componentes", 5),
            ("Tiempo Estándar (min):", "tiempo", 6)
        ]

        for i, (label, key, row) in enumerate(campos):
            tk.Label(form_frame, text=label, font=("Arial", 11)).grid(row=row, column=0, sticky="w", padx=5, pady=8)
            
            if key == "categoria":
                entry = ttk.Combobox(form_frame, values=["sedan", "SUV", "pickup"], 
                                   width=40, font=("Arial", 11), state="readonly")
            else:
                entry = tk.Entry(form_frame, width=50, font=("Arial", 11), relief="solid", bd=1)
            
            entry.grid(row=row, column=1, sticky="w", padx=5, pady=8)
            self.modelo_fields[key] = entry

        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Guardar", command=self.guardar_modelo,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.buscar_modelo,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.actualizar_modelo,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Eliminar", command=self.eliminar_modelo,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=lambda: self.limpiar_campos(self.modelo_fields),
                  width=15).pack(side=tk.LEFT, padx=5)

        # ID oculto para actualizaciones
        self.modelo_id = None

        # Área de resultados
        self.result_frame1 = ttk.LabelFrame(self.tab_modelos, text="Resultados", padding=10)
        self.result_frame1.pack(fill="both", expand=True, padx=20, pady=10)

        self.result_text1 = tk.Text(self.result_frame1, height=15, width=100, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(self.result_frame1, orient="vertical", command=self.result_text1.yview)
        self.result_text1.configure(yscrollcommand=scrollbar.set)
        
        self.result_text1.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

    def guardar_modelo(self):
        """Guarda un nuevo modelo"""
        # Validar campos obligatorios
        codigo = self.modelo_fields["codigo_unico"].get()
        nombre = self.modelo_fields["nombre"].get()
        categoria = self.modelo_fields["categoria"].get()

        if not codigo or not nombre or not categoria:
            messagebox.showerror("Error", "Código, Nombre y Categoría son obligatorios")
            return

        # Preparar parámetros
        params = [
            codigo,
            nombre,
            categoria,
            self.modelo_fields["versiones"].get() or None,
            self.modelo_fields["especificaciones"].get() or None,
            self.modelo_fields["componentes"].get() or None,
            int(self.modelo_fields["tiempo"].get()) if self.modelo_fields["tiempo"].get() else None
        ]

        # Ejecutar procedimiento
        result = self.db_connector.execute_procedure_single('sp_crear_modelo', *params)
        
        if result:
            messagebox.showinfo("Éxito", f"Modelo guardado correctamente con ID: {result[0]}")
            self.limpiar_campos(self.modelo_fields)
            self.mostrar_todos_modelos()

    def buscar_modelo(self):
        """Busca un modelo por código"""
        codigo = self.modelo_fields["codigo_unico"].get()
        if not codigo:
            messagebox.showwarning("Advertencia", "Ingrese un código para buscar")
            return

        # Buscar por código (usando el procedimiento de obtener todos y filtrar)
        results = self.db_connector.execute_procedure('sp_obtener_modelos')
        if results:
            for headers, rows in results:
                for row in rows:
                    if row[1] == codigo:  # código_unico está en índice 1
                        self.modelo_id = row[0]
                        self.modelo_fields["codigo_unico"].delete(0, tk.END)
                        self.modelo_fields["codigo_unico"].insert(0, row[1])
                        self.modelo_fields["nombre"].delete(0, tk.END)
                        self.modelo_fields["nombre"].insert(0, row[2])
                        self.modelo_fields["categoria"].set(row[3])
                        self.modelo_fields["versiones"].delete(0, tk.END)
                        self.modelo_fields["versiones"].insert(0, row[4] or "")
                        self.modelo_fields["especificaciones"].delete(0, tk.END)
                        self.modelo_fields["especificaciones"].insert(0, row[5] or "")
                        self.modelo_fields["componentes"].delete(0, tk.END)
                        self.modelo_fields["componentes"].insert(0, row[6] or "")
                        self.modelo_fields["tiempo"].delete(0, tk.END)
                        self.modelo_fields["tiempo"].insert(0, row[7] or "")
                        
                        self.display_results(self.result_text1, [(headers, [row])])
                        return
            
            messagebox.showinfo("Información", "No se encontró el modelo")

    def actualizar_modelo(self):
        """Actualiza un modelo existente"""
        if not self.modelo_id:
            messagebox.showwarning("Advertencia", "Primero busque un modelo para actualizar")
            return

        params = [
            self.modelo_id,
            self.modelo_fields["codigo_unico"].get(),
            self.modelo_fields["nombre"].get(),
            self.modelo_fields["categoria"].get(),
            self.modelo_fields["versiones"].get() or None,
            self.modelo_fields["especificaciones"].get() or None,
            self.modelo_fields["componentes"].get() or None,
            int(self.modelo_fields["tiempo"].get()) if self.modelo_fields["tiempo"].get() else None
        ]

        result = self.db_connector.execute_procedure_single('sp_actualizar_modelo', *params)
        
        if result and result[0] > 0:
            messagebox.showinfo("Éxito", "Modelo actualizado correctamente")
            self.mostrar_todos_modelos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el modelo")

    def eliminar_modelo(self):
        """Elimina (lógicamente) un modelo"""
        if not self.modelo_id:
            messagebox.showwarning("Advertencia", "Primero busque un modelo para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este modelo?"):
            result = self.db_connector.execute_procedure_single('sp_eliminar_modelo', self.modelo_id)
            
            if result and result[0] > 0:
                messagebox.showinfo("Éxito", "Modelo eliminado correctamente")
                self.limpiar_campos(self.modelo_fields)
                self.modelo_id = None
                self.mostrar_todos_modelos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el modelo")

    def mostrar_todos_modelos(self):
        """Muestra todos los modelos"""
        results = self.db_connector.execute_procedure('sp_obtener_modelos')
        if results:
            self.display_results(self.result_text1, results)


    # =====================================================
    # PESTAÑA 2: LÍNEAS DE PRODUCCIÓN
    # =====================================================
    def setup_tab_lineas(self):
        """Configura la pestaña de líneas de producción"""
        # Título
        titulo = tk.Label(self.tab_lineas, text="GESTIÓN DE LÍNEAS DE PRODUCCIÓN", 
                         font=("Arial", 16, "bold"), fg="#27ae60")
        titulo.pack(pady=10)

        # Frame para el formulario
        form_frame = ttk.LabelFrame(self.tab_lineas, text="Datos de la Línea", padding=10)
        form_frame.pack(fill="x", padx=20, pady=10)

        # Campos del formulario
        self.linea_fields = {}
        campos = [
            ("Número de Línea:", "numero_linea", 0),
            ("Tipo Vehículos:", "tipo_vehiculos", 1),
            ("Capacidad Diaria:", "capacidad", 2),
            ("Estaciones Trabajo:", "estaciones", 3),
            ("Supervisor:", "supervisor", 4),
            ("Turno Activo:", "turno", 5),
            ("Estado Operativo:", "estado", 6)
        ]

        for i, (label, key, row) in enumerate(campos):
            tk.Label(form_frame, text=label, font=("Arial", 11)).grid(row=row, column=0, sticky="w", padx=5, pady=8)
            
            if key == "tipo_vehiculos":
                entry = ttk.Combobox(form_frame, values=["Sedan", "SUV", "Pickup", "Mixto"], 
                                   width=40, font=("Arial", 11), state="readonly")
            elif key == "turno":
                entry = ttk.Combobox(form_frame, values=["mañana", "tarde", "noche"], 
                                   width=40, font=("Arial", 11), state="readonly")
            elif key == "estado":
                entry = ttk.Combobox(form_frame, values=["activo", "mantenimiento", "parado"], 
                                   width=40, font=("Arial", 11), state="readonly")
            else:
                entry = tk.Entry(form_frame, width=50, font=("Arial", 11), relief="solid", bd=1)
            
            entry.grid(row=row, column=1, sticky="w", padx=5, pady=8)
            self.linea_fields[key] = entry

        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Guardar", command=self.guardar_linea,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.buscar_linea,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.actualizar_linea,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cambiar Estado", command=self.cambiar_estado_linea,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=lambda: self.limpiar_campos(self.linea_fields),
                  width=15).pack(side=tk.LEFT, padx=5)

        self.linea_id = None

        # Área de resultados
        self.result_frame2 = ttk.LabelFrame(self.tab_lineas, text="Resultados", padding=10)
        self.result_frame2.pack(fill="both", expand=True, padx=20, pady=10)

        self.result_text2 = tk.Text(self.result_frame2, height=15, width=100, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(self.result_frame2, orient="vertical", command=self.result_text2.yview)
        self.result_text2.configure(yscrollcommand=scrollbar.set)
        
        self.result_text2.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

    def guardar_linea(self):
        """Guarda una nueva línea de producción"""
        numero = self.linea_fields["numero_linea"].get()
        tipo = self.linea_fields["tipo_vehiculos"].get()
        turno = self.linea_fields["turno"].get()
        estado = self.linea_fields["estado"].get()

        if not numero or not tipo or not turno or not estado:
            messagebox.showerror("Error", "Número, Tipo, Turno y Estado son obligatorios")
            return

        params = [
            numero,
            tipo,
            int(self.linea_fields["capacidad"].get()) if self.linea_fields["capacidad"].get() else None,
            int(self.linea_fields["estaciones"].get()) if self.linea_fields["estaciones"].get() else None,
            self.linea_fields["supervisor"].get() or None,
            turno,
            estado
        ]

        result = self.db_connector.execute_procedure_single('sp_crear_linea', *params)
        
        if result:
            messagebox.showinfo("Éxito", f"Línea guardada correctamente con ID: {result[0]}")
            self.limpiar_campos(self.linea_fields)
            self.mostrar_todos_lineas()
            self.cargar_lineas_combobox()

    def buscar_linea(self):
        """Busca una línea por número"""
        numero = self.linea_fields["numero_linea"].get()
        if not numero:
            messagebox.showwarning("Advertencia", "Ingrese un número de línea para buscar")
            return

        results = self.db_connector.execute_procedure('sp_obtener_lineas')
        if results:
            for headers, rows in results:
                for row in rows:
                    if row[1] == numero:  # numero_linea está en índice 1
                        self.linea_id = row[0]
                        self.linea_fields["numero_linea"].delete(0, tk.END)
                        self.linea_fields["numero_linea"].insert(0, row[1])
                        self.linea_fields["tipo_vehiculos"].set(row[2] or "")
                        self.linea_fields["capacidad"].delete(0, tk.END)
                        self.linea_fields["capacidad"].insert(0, row[3] or "")
                        self.linea_fields["estaciones"].delete(0, tk.END)
                        self.linea_fields["estaciones"].insert(0, row[4] or "")
                        self.linea_fields["supervisor"].delete(0, tk.END)
                        self.linea_fields["supervisor"].insert(0, row[5] or "")
                        self.linea_fields["turno"].set(row[6])
                        self.linea_fields["estado"].set(row[7])
                        
                        self.display_results(self.result_text2, [(headers, [row])])
                        return
            
            messagebox.showinfo("Información", "No se encontró la línea")

    def actualizar_linea(self):
        """Actualiza una línea existente"""
        if not self.linea_id:
            messagebox.showwarning("Advertencia", "Primero busque una línea para actualizar")
            return

        params = [
            self.linea_id,
            self.linea_fields["numero_linea"].get(),
            self.linea_fields["tipo_vehiculos"].get(),
            int(self.linea_fields["capacidad"].get()) if self.linea_fields["capacidad"].get() else None,
            int(self.linea_fields["estaciones"].get()) if self.linea_fields["estaciones"].get() else None,
            self.linea_fields["supervisor"].get() or None,
            self.linea_fields["turno"].get(),
            self.linea_fields["estado"].get()
        ]

        result = self.db_connector.execute_procedure_single('sp_actualizar_linea', *params)
        
        if result and result[0] > 0:
            messagebox.showinfo("Éxito", "Línea actualizada correctamente")
            self.mostrar_todos_lineas()
            self.cargar_lineas_combobox()
        else:
            messagebox.showerror("Error", "No se pudo actualizar la línea")

    def cambiar_estado_linea(self):
        """Cambia el estado de una línea"""
        if not self.linea_id:
            messagebox.showwarning("Advertencia", "Primero busque una línea")
            return

        estado = self.linea_fields["estado"].get()
        if not estado:
            messagebox.showwarning("Advertencia", "Seleccione un estado")
            return

        result = self.db_connector.execute_procedure_single('sp_cambiar_estado_linea', self.linea_id, estado)
        
        if result and result[0] > 0:
            messagebox.showinfo("Éxito", "Estado de línea actualizado correctamente")
            self.mostrar_todos_lineas()
        else:
            messagebox.showerror("Error", "No se pudo cambiar el estado")

    def mostrar_todos_lineas(self):
        """Muestra todas las líneas"""
        results = self.db_connector.execute_procedure('sp_obtener_lineas')
        if results:
            self.display_results(self.result_text2, results)


    # =====================================================
    # PESTAÑA 3: COMPONENTES Y PARTES
    # =====================================================
    def setup_tab_componentes(self):
        """Configura la pestaña de componentes"""
        # Título
        titulo = tk.Label(self.tab_componentes, text="GESTIÓN DE COMPONENTES", 
                         font=("Arial", 16, "bold"), fg="#e67e22")
        titulo.pack(pady=10)

        # Frame para el formulario
        form_frame = ttk.LabelFrame(self.tab_componentes, text="Datos del Componente", padding=10)
        form_frame.pack(fill="x", padx=20, pady=10)

        # Campos del formulario
        self.componente_fields = {}
        campos = [
            ("Código Único:", "codigo", 0),
            ("Descripción:", "descripcion", 1),
            ("Categoría:", "categoria", 2),
            ("Especificaciones:", "especificaciones", 3),
            ("Proveedor:", "proveedor", 4),
            ("Tiempo Entrega (días):", "tiempo", 5),
            ("Costo Unitario:", "costo", 6),
            ("Stock Mínimo:", "stock_minimo", 7)
        ]

        for i, (label, key, row) in enumerate(campos):
            tk.Label(form_frame, text=label, font=("Arial", 11)).grid(row=row, column=0, sticky="w", padx=5, pady=8)
            
            if key == "categoria":
                entry = ttk.Combobox(form_frame, values=["Motor", "Transmisión", "Suspensión", "Eléctrico", "Carrocería", "Interior", "Frenos", "Ruedas"], 
                                   width=40, font=("Arial", 11), state="readonly")
            else:
                entry = tk.Entry(form_frame, width=50, font=("Arial", 11), relief="solid", bd=1)
            
            entry.grid(row=row, column=1, sticky="w", padx=5, pady=8)
            self.componente_fields[key] = entry

        # Frame para inventario
        inv_frame = ttk.LabelFrame(self.tab_componentes, text="Datos de Inventario", padding=10)
        inv_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(inv_frame, text="Cantidad Disponible:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=5, pady=8)
        self.cantidad_inv = tk.Entry(inv_frame, width=30, font=("Arial", 11), relief="solid", bd=1)
        self.cantidad_inv.grid(row=0, column=1, sticky="w", padx=5, pady=8)

        tk.Label(inv_frame, text="Ubicación:", font=("Arial", 11)).grid(row=0, column=2, sticky="w", padx=20, pady=8)
        self.ubicacion_inv = tk.Entry(inv_frame, width=30, font=("Arial", 11), relief="solid", bd=1)
        self.ubicacion_inv.grid(row=0, column=3, sticky="w", padx=5, pady=8)

        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Guardar Componente", command=self.guardar_componente,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.buscar_componente,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Ver Inventario", command=self.mostrar_inventario,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Actualizar", command=self.actualizar_componente,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.limpiar_componentes,
                  width=15).pack(side=tk.LEFT, padx=5)

        self.componente_id = None

        # Área de resultados
        self.result_frame3 = ttk.LabelFrame(self.tab_componentes, text="Resultados", padding=10)
        self.result_frame3.pack(fill="both", expand=True, padx=20, pady=10)

        self.result_text3 = tk.Text(self.result_frame3, height=15, width=100, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(self.result_frame3, orient="vertical", command=self.result_text3.yview)
        self.result_text3.configure(yscrollcommand=scrollbar.set)
        
        self.result_text3.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

    def guardar_componente(self):
        """Guarda un nuevo componente"""
        codigo = self.componente_fields["codigo"].get()
        descripcion = self.componente_fields["descripcion"].get()

        if not codigo or not descripcion:
            messagebox.showerror("Error", "Código y Descripción son obligatorios")
            return

        params = [
            codigo,
            descripcion,
            self.componente_fields["categoria"].get() or None,
            self.componente_fields["especificaciones"].get() or None,
            self.componente_fields["proveedor"].get() or None,
            int(self.componente_fields["tiempo"].get()) if self.componente_fields["tiempo"].get() else None,
            float(self.componente_fields["costo"].get()) if self.componente_fields["costo"].get() else None,
            int(self.componente_fields["stock_minimo"].get()) if self.componente_fields["stock_minimo"].get() else None
        ]

        result = self.db_connector.execute_procedure_single('sp_crear_componente', *params)
        
        if result:
            componente_id = result[0]
            
            # Si hay datos de inventario, insertarlos
            if self.cantidad_inv.get() and self.ubicacion_inv.get():
                # Nota: Deberías tener un procedimiento para insertar inventario
                # Por simplicidad, solo mostramos mensaje
                messagebox.showinfo("Éxito", f"Componente guardado con ID: {componente_id}\nRecuerde actualizar inventario")
            else:
                messagebox.showinfo("Éxito", f"Componente guardado correctamente con ID: {componente_id}")
            
            self.limpiar_componentes()
            self.mostrar_inventario()

    def buscar_componente(self):
        """Busca un componente por código"""
        codigo = self.componente_fields["codigo"].get()
        if not codigo:
            messagebox.showwarning("Advertencia", "Ingrese un código para buscar")
            return

        results = self.db_connector.execute_procedure('sp_obtener_componentes')
        if results:
            for headers, rows in results:
                for row in rows:
                    if row[1] == codigo:  # código_unico está en índice 1
                        self.componente_id = row[0]
                        self.componente_fields["codigo"].delete(0, tk.END)
                        self.componente_fields["codigo"].insert(0, row[1])
                        self.componente_fields["descripcion"].delete(0, tk.END)
                        self.componente_fields["descripcion"].insert(0, row[2])
                        self.componente_fields["categoria"].set(row[3] or "")
                        self.componente_fields["especificaciones"].delete(0, tk.END)
                        self.componente_fields["especificaciones"].insert(0, row[4] or "")
                        self.componente_fields["proveedor"].delete(0, tk.END)
                        self.componente_fields["proveedor"].insert(0, row[5] or "")
                        self.componente_fields["tiempo"].delete(0, tk.END)
                        self.componente_fields["tiempo"].insert(0, row[6] or "")
                        self.componente_fields["costo"].delete(0, tk.END)
                        self.componente_fields["costo"].insert(0, row[7] or "")
                        self.componente_fields["stock_minimo"].delete(0, tk.END)
                        self.componente_fields["stock_minimo"].insert(0, row[8] or "")
                        
                        self.display_results(self.result_text3, [(headers, [row])])
                        return
            
            messagebox.showinfo("Información", "No se encontró el componente")

    def actualizar_componente(self):
        """Actualiza un componente existente"""
        if not self.componente_id:
            messagebox.showwarning("Advertencia", "Primero busque un componente para actualizar")
            return

        params = [
            self.componente_id,
            self.componente_fields["codigo"].get(),
            self.componente_fields["descripcion"].get(),
            self.componente_fields["categoria"].get() or None,
            self.componente_fields["especificaciones"].get() or None,
            self.componente_fields["proveedor"].get() or None,
            int(self.componente_fields["tiempo"].get()) if self.componente_fields["tiempo"].get() else None,
            float(self.componente_fields["costo"].get()) if self.componente_fields["costo"].get() else None,
            int(self.componente_fields["stock_minimo"].get()) if self.componente_fields["stock_minimo"].get() else None
        ]

        result = self.db_connector.execute_procedure_single('sp_actualizar_componente', *params)
        
        if result and result[0] > 0:
            messagebox.showinfo("Éxito", "Componente actualizado correctamente")
            self.mostrar_inventario()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el componente")

    def mostrar_inventario(self):
        """Muestra el inventario completo"""
        results = self.db_connector.execute_procedure('sp_obtener_inventario_completo')
        if results:
            self.display_results(self.result_text3, results)

    def limpiar_componentes(self):
        """Limpia los campos de componentes"""
        self.limpiar_campos(self.componente_fields)
        self.cantidad_inv.delete(0, tk.END)
        self.ubicacion_inv.delete(0, tk.END)
        self.componente_id = None


    # =====================================================
    # PESTAÑA 4: ÓRDENES DE PRODUCCIÓN
    # =====================================================
    def setup_tab_ordenes(self):
        """Configura la pestaña de órdenes de producción"""
        # Título
        titulo = tk.Label(self.tab_ordenes, text="GESTIÓN DE ÓRDENES DE PRODUCCIÓN", 
                         font=("Arial", 16, "bold"), fg="#8e44ad")
        titulo.pack(pady=10)

        # Frame para el formulario
        form_frame = ttk.LabelFrame(self.tab_ordenes, text="Datos de la Orden", padding=10)
        form_frame.pack(fill="x", padx=20, pady=10)

        # Campos del formulario
        self.orden_fields = {}
        campos = [
            ("Número Único:", "numero", 0),
            ("Fecha Emisión:", "fecha_emision", 1),
            ("Modelo:", "modelo", 2),
            ("Cantidad:", "cantidad", 3),
            ("Fecha Inicio:", "fecha_inicio", 4),
            ("Fecha Fin Estimada:", "fecha_fin", 5),
            ("Prioridad:", "prioridad", 6),
            ("Estado:", "estado", 7)
        ]

        for i, (label, key, row) in enumerate(campos):
            tk.Label(form_frame, text=label, font=("Arial", 11)).grid(row=row, column=0, sticky="w", padx=5, pady=8)
            
            if key in ["fecha_emision", "fecha_inicio", "fecha_fin"]:
                entry = DateEntry(form_frame, width=40, font=("Arial", 11), 
                                background='darkblue', foreground='white', borderwidth=2,
                                date_pattern='yyyy-mm-dd')
            elif key == "modelo":
                entry = ttk.Combobox(form_frame, width=40, font=("Arial", 11), state="readonly")
                self.cargar_modelos_combobox()
                self.modelo_orden = entry
            elif key == "prioridad":
                entry = ttk.Combobox(form_frame, values=["baja", "normal", "alta", "urgente"], 
                                   width=40, font=("Arial", 11), state="readonly")
            elif key == "estado":
                entry = ttk.Combobox(form_frame, values=["pendiente", "en_proceso", "completada", "cancelada"], 
                                   width=40, font=("Arial", 11), state="readonly")
            else:
                entry = tk.Entry(form_frame, width=50, font=("Arial", 11), relief="solid", bd=1)
            
            entry.grid(row=row, column=1, sticky="w", padx=5, pady=8)
            self.orden_fields[key] = entry

        # Botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Guardar Orden", command=self.guardar_orden,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Buscar", command=self.buscar_orden,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cambiar Estado", command=self.cambiar_estado_orden,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Ver Pendientes", command=self.ver_ordenes_pendientes,
                  width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=lambda: self.limpiar_campos(self.orden_fields),
                  width=15).pack(side=tk.LEFT, padx=5)

        self.orden_id = None

        # Área de resultados
        self.result_frame4 = ttk.LabelFrame(self.tab_ordenes, text="Resultados", padding=10)
        self.result_frame4.pack(fill="both", expand=True, padx=20, pady=10)

        self.result_text4 = tk.Text(self.result_frame4, height=15, width=100, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(self.result_frame4, orient="vertical", command=self.result_text4.yview)
        self.result_text4.configure(yscrollcommand=scrollbar.set)
        
        self.result_text4.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

    def guardar_orden(self):
        """Guarda una nueva orden de producción"""
        numero = self.orden_fields["numero"].get()
        modelo = self.orden_fields["modelo"].get()
        cantidad = self.orden_fields["cantidad"].get()

        if not numero or not modelo or not cantidad:
            messagebox.showerror("Error", "Número, Modelo y Cantidad son obligatorios")
            return

        # Extraer ID del modelo del combobox (formato: "ID - Nombre")
        modelo_id = int(modelo.split(" - ")[0])

        params = [
            numero,
            self.orden_fields["fecha_emision"].get(),
            modelo_id,
            int(cantidad),
            self.orden_fields["fecha_inicio"].get() or None,
            self.orden_fields["fecha_fin"].get() or None,
            self.orden_fields["prioridad"].get() or "normal"
        ]

        result = self.db_connector.execute_procedure_single('sp_crear_orden', *params)
        
        if result:
            messagebox.showinfo("Éxito", f"Orden guardada correctamente con ID: {result[0]}")
            self.limpiar_campos(self.orden_fields)
            self.mostrar_todas_ordenes()

    def buscar_orden(self):
        """Busca una orden por número"""
        numero = self.orden_fields["numero"].get()
        if not numero:
            messagebox.showwarning("Advertencia", "Ingrese un número de orden para buscar")
            return

        results = self.db_connector.execute_procedure('sp_obtener_ordenes')
        if results:
            for headers, rows in results:
                for row in rows:
                    if row[1] == numero:  # numero_unico está en índice 1
                        self.orden_id = row[0]
                        self.orden_fields["numero"].delete(0, tk.END)
                        self.orden_fields["numero"].insert(0, row[1])
                        self.orden_fields["fecha_emision"].delete(0, tk.END)
                        self.orden_fields["fecha_emision"].insert(0, row[2])
                        
                        # Buscar el nombre del modelo para el combobox
                        modelo_text = f"{row[3]} - {row[9]}"
                        self.orden_fields["modelo"].set(modelo_text)
                        
                        self.orden_fields["cantidad"].delete(0, tk.END)
                        self.orden_fields["cantidad"].insert(0, row[4])
                        self.orden_fields["fecha_inicio"].delete(0, tk.END)
                        self.orden_fields["fecha_inicio"].insert(0, row[5] or "")
                        self.orden_fields["fecha_fin"].delete(0, tk.END)
                        self.orden_fields["fecha_fin"].insert(0, row[6] or "")
                        self.orden_fields["prioridad"].set(row[7])
                        self.orden_fields["estado"].set(row[8])
                        
                        self.display_results(self.result_text4, [(headers, [row])])
                        return
            
            messagebox.showinfo("Información", "No se encontró la orden")

    def cambiar_estado_orden(self):
        """Cambia el estado de una orden"""
        if not self.orden_id:
            messagebox.showwarning("Advertencia", "Primero busque una orden")
            return

        estado = self.orden_fields["estado"].get()
        if not estado:
            messagebox.showwarning("Advertencia", "Seleccione un estado")
            return

        result = self.db_connector.execute_procedure_single('sp_actualizar_estado_orden', self.orden_id, estado)
        
        if result and result[0] > 0:
            messagebox.showinfo("Éxito", "Estado de orden actualizado correctamente")
            self.mostrar_todas_ordenes()
        else:
            messagebox.showerror("Error", "No se pudo cambiar el estado")

    def ver_ordenes_pendientes(self):
        """Muestra las órdenes pendientes"""
        results = self.db_connector.execute_procedure('sp_obtener_ordenes_por_estado', 'pendiente')
        if results:
            self.display_results(self.result_text4, results)

    def mostrar_todas_ordenes(self):
        """Muestra todas las órdenes"""
        results = self.db_connector.execute_procedure('sp_obtener_ordenes')
        if results:
            self.display_results(self.result_text4, results)


    # =====================================================
    # FUNCIONES AUXILIARES
    # =====================================================
    def limpiar_campos(self, fields_dict):
        """Limpia los campos de un diccionario"""
        for key, entry in fields_dict.items():
            if isinstance(entry, (tk.Entry, ttk.Combobox)):
                if isinstance(entry, ttk.Combobox):
                    entry.set('')
                else:
                    entry.delete(0, tk.END)

    def display_results(self, text_widget, results):
        """Muestra los resultados en el widget de texto"""
        text_widget.delete(1.0, tk.END)
        for headers, rows in results:
            table = tabulate(rows, headers=headers, tablefmt="grid", maxcolwidths=30)
            text_widget.insert(tk.END, table + "\n\n")


# =====================================================
# CONFIGURACIÓN Y EJECUCIÓN
# =====================================================
if __name__ == "__main__":
    # Configuración de la base de datos
    user = 'root'
    password = ''  # Cambiar según tu configuración
    host = 'localhost'
    database = 'autofactory'

    # Crear y conectar a la base de datos
    db_connector = DatabaseConnector(host, user, password, database)
    db_connector.connect()

    # Crear y ejecutar la aplicación
    app = AutoFactoryApp(db_connector)
    app.mainloop()

    # Cerrar la conexión a la base de datos
    db_connector.disconnect()