import mysql.connector # Importa el módulo mysql.connector para manejar la conexión a MySQL/MariaDB
from mysql.connector import Error # Importa la clase Error para manejar errores específicos de MySQL/MariaDB

def obtener_conexion(): # Define una función para obtener una conexión a la base de datos
    """
    Crea y retorna una conexión a la base de datos MySQL/MariaDB
    """
    try:
        conexion = mysql.connector.connect( # Intenta establecer una conexión con los parámetros especificados
            host='localhost',        # Servidor (normalmente localhost) 
            user='root',              # Tu usuario de MySQL 
            password='',              # Tu contraseña (déjalo vacío si no tiene)
            database='autofactory',   # Nombre de la base de datos
            port='3306'                # Puerto por defecto de MySQL
        )
        
        if conexion.is_connected(): # Verifica si la conexión fue exitosa
            print("✅ Conexión exitosa a la base de datos") # Imprime un mensaje de éxito
            return conexion # Retorna la conexión para usarla en otras partes del programa
            
    except Error as e: # Captura cualquier error que ocurra durante la conexión
        print(f"❌ Error al conectar a MySQL: {e}") # Imprime el error para ayudar a diagnosticar el problema
        return None # Retorna None si la conexión falla

def probar_conexion():
    """
    Función para probar si la conexión funciona
    """
    conexion = obtener_conexion() # Intenta obtener una conexión a la base de datos 
    if conexion: # Si la conexión fue exitosa, realiza una consulta simple para verificar que todo esté funcionando
        cursor = conexion.cursor() # Crea un cursor para ejecutar consultas SQL
        cursor.execute("SELECT DATABASE()") # Ejecuta una consulta para obtener el nombre de la base de datos actual
        db_name = cursor.fetchone() # Obtiene el resultado de la consulta (el nombre de la base de datos)
        print(f"📊 Conectado a la base de datos: {db_name[0]}") # Imprime el nombre de la base de datos
        cursor.close() # Cierra el cursor después de usarlo
        conexion.close() # Cierra la conexión después de la prueba
        return True # Retorna True si la conexión y la consulta fueron exitosas
    return False # Retorna False si la conexión no fue exitosa o si hubo un error durante la consulta

# Si ejecutas este archivo directamente, prueba la conexión
if __name__ == "__main__": # Esto asegura que la prueba solo se ejecute si este archivo es el programa principal
    probar_conexion() # Llama a la función para probar la conexión a la base de datos