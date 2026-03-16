import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    """
    Crea y retorna una conexión a la base de datos MySQL/MariaDB
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',        # Servidor (normalmente localhost)
            user='root',              # Tu usuario de MySQL
            password='',              # Tu contraseña (déjalo vacío si no tiene)
            database='autofactory',   # Nombre de la base de datos
            port='3306'                # Puerto por defecto de MySQL
        )
        
        if conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            return conexion
            
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

def probar_conexion():
    """
    Función para probar si la conexión funciona
    """
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        print(f"📊 Conectado a la base de datos: {db_name[0]}")
        cursor.close()
        conexion.close()
        return True
    return False

# Si ejecutas este archivo directamente, prueba la conexión
if __name__ == "__main__":
    probar_conexion()