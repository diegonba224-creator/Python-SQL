# views/modelo_view.py
import tkinter as tk
from tkinter import ttk, messagebox

class ModeloView:
    def __init__(self, parent, controller):
        self.controller = controller
        self.frame = ttk.Frame(parent)
        self.selected_id = None
        
        self.create_form()
        self.create_buttons()
        self.create_table()
        self.cargar_datos()
        
    def create_form(self):
        """Crea el formulario de entrada"""
        form_frame = ttk.LabelFrame(self.frame, text="📝 Formulario de Modelos", padding=10)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        self.entries = {}
        campos = [
            ("Código Único:", "codigo_unico"),
            ("Nombre:", "nombre"),
            ("Categoría:", "categoria"),
            ("Versiones:", "versiones"),
            ("Especificaciones:", "especificaciones"),
            ("Componentes:", "componentes"),
            ("Tiempo (min):", "tiempo")
        ]
        
        for i, (label, key) in enumerate(campos):
            ttk.Label(form_frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=3)
            
            if key == "categoria":
                self.entries[key] = ttk.Combobox(form_frame, values=["sedan", "SUV", "pickup"], width=50)
                self.entries[key].grid(row=i, column=1, sticky="w", padx=5, pady=3)
            else:
                self.entries[key] = ttk.Entry(form_frame, width=60)
                self.entries[key].grid(row=i, column=1, sticky="w", padx=5, pady=3)
                
    def create_buttons(self):
        """Crea los botones de acción"""
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(pady=10)
        
        buttons = [
            ("💾 Guardar", self.controller.guardar, 'success'),
            ("🔄 Actualizar", self.controller.actualizar, 'primary'),
            ("🗑️ Eliminar", self.controller.eliminar, 'danger'),
            ("🧹 Limpiar", self.limpiar_campos, 'warning'),
            ("📋 Mostrar Todos", self.controller.mostrar_todos, 'info')
        ]
        
        for text, command, style in buttons:
            btn = ttk.Button(btn_frame, text=text, command=command)
            btn.pack(side="left", padx=5)
            
    def create_table(self):
        """Crea la tabla para mostrar datos"""
        table_frame = ttk.LabelFrame(self.frame, text="📊 Lista de Modelos", padding=10)
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        columns = ("ID", "Código", "Nombre", "Categoría", "Tiempo", "Versiones")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        
        column_widths = [50, 100, 200, 80, 80, 200]
        for col, width in zip(columns, column_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)
        
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.tree.bind('<<TreeviewSelect>>', self.on_select)
        
    def on_select(self, event):
        """Evento al seleccionar un elemento"""
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            self.selected_id = item['values'][0]
            self.controller.cargar_para_editar(self.selected_id)
            
    def cargar_datos(self, datos):
        """Carga los datos en la tabla"""
        # Limpiar tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Insertar nuevos datos
        for row in datos:
            valores = (
                row['id'],
                row['codigo_unico'],
                row['nombre'],
                row['categoria'].capitalize() if row['categoria'] else '',
                row['tiempo_estandar_ensamblaje'],
                (row['versiones'][:50] + '...') if row['versiones'] and len(row['versiones']) > 50 else row['versiones']
            )
            self.tree.insert("", "end", values=valores)
            
    def limpiar_campos(self):
        """Limpia todos los campos del formulario"""
        for entry in self.entries.values():
            if isinstance(entry, ttk.Entry) or isinstance(entry, ttk.Combobox):
                entry.delete(0, tk.END)
        self.selected_id = None
        