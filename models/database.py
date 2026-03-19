# models/database.py
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

class Database:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config):
        if not hasattr(self, 'initialized'):
            self.config = config
            self.connection = None
            self.cursor = None
            self.initialized = True
    
    def connect(self):
        """Establece la conexión con la base de datos"""
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor(dictionary=True)
            print("✅ Conexión establecida a la base de datos")
            return True
        except Error as e:
            print(f"❌ Error al conectar: {e}")
            return False
    
    def disconnect(self):
        """Cierra la conexión con la base de datos"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("🔌 Conexión cerrada")
    
    def execute_procedure(self, procedure_name, params=None):
        """Ejecuta un procedimiento almacenado"""
        try:
            if params:
                self.cursor.callproc(procedure_name, params)
            else:
                self.cursor.callproc(procedure_name)
            
            results = []
            for result in self.cursor.stored_results():
                rows = result.fetchall()
                if rows:
                    results.append(rows)
            
            self.connection.commit()
            return results if results else []
            
        except Error as e:
            self.connection.rollback()
            print(f"❌ Error en {procedure_name}: {e}")
            raise e
    
    def execute_query(self, query, params=None):
        """Ejecuta una consulta SQL directa"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            
            if query.strip().upper().startswith('SELECT'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor.rowcount
                
        except Error as e:
            self.connection.rollback()
            print(f"❌ Error en consulta: {e}")
            raise e
        