Autofactory - Sistema de Gestión Automotriz
Sistema de escritorio desarrollado en Python con Tkinter y MySQL para la gestión integral de procesos productivos en la industria automotriz "Motores Eficientes S.A."

📋 Descripción
Autofactory es una aplicación de gestión diseñada para controlar y administrar los procesos de producción de una fábrica de automóviles. El sistema permite gestionar modelos de vehículos, líneas de producción, componentes y partes, así como órdenes de producción, proporcionando una interfaz gráfica intuitiva y conexión con base de datos MySQL.

🚀 Características Principales
Interfaz gráfica con pestañas para organización modular

Gestión completa de 4 módulos principales:

Modelos de Vehículos

Líneas de Producción

Componentes y Partes

Órdenes de Producción

Conexión a MySQL con procedimientos almacenados

Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)

Datos de prueba incluidos para demostración

📁 Estructura del Proyecto
text
autofactory/
│
├── autofactory.py           # Archivo principal de la aplicación
├── database_config.py        # Configuración de conexión a MySQL (a crear)
├── README.md                 # Este archivo
│
└── sql/
    └── autofactory.sql       # Script SQL con estructura y datos de prueba
🔧 Requisitos Previos
Python 3.8 o superior

MySQL Server 5.7 o superior

Pip (gestor de paquetes de Python)

📦 Instalación de Dependencias
bash
pip install mysql-connector-python
🗄️ Configuración de la Base de Datos
Iniciar MySQL en tu sistema

Ejecutar el script SQL para crear la base de datos, tablas, procedimientos y datos de prueba:

bash
mysql -u root -p < sql/autofactory.sql
O si prefieres, copia y pega el contenido del archivo SQL en tu cliente MySQL (phpMyAdmin, MySQL Workbench, etc.)

Crear archivo database_config.py con la configuración de conexión:

python
import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    """Establece y retorna una conexión a la base de datos"""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Cambiar por tu contraseña
            database="autofactory"
        )
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None
🎯 Cómo Ejecutar la Aplicación
Clona o descarga este repositorio

Configura la base de datos según las instrucciones anteriores

Ejecuta la aplicación:

bash
python autofactory.py
🖥️ Módulos del Sistema
1. Modelos de Vehículos
Gestión de códigos únicos, nombres y categorías (sedan, SUV, pickup)

Configuración de versiones disponibles

Especificaciones técnicas y componentes requeridos

Tiempo estándar de ensamblaje

2. Líneas de Producción
Número de línea y tipo de vehículos que ensambla

Capacidad diaria y número de estaciones de trabajo

Supervisor responsable y turno activo

Estado operativo (activo, mantenimiento, parado)

3. Componentes y Partes
Catálogo con código único y descripción

Categorías (Motor, Transmisión, Suspensión, Eléctrico, Carrocería)

Proveedor principal y tiempo de entrega

Costo unitario y stock mínimo requerido

Gestión de inventario con cantidad disponible y calidad

4. Órdenes de Producción
Número único y fecha de emisión

Modelo de vehículo a fabricar

Cantidad a producir y fechas programadas

Prioridad (alta, media, baja) y estado actual

🗃️ Estructura de la Base de Datos
Tablas Principales
modelos_vehiculos - Catálogo de modelos

lineas_produccion - Líneas de ensamblaje

componentes_partes - Componentes y repuestos

inventario_componentes - Stock de componentes

ordenes_produccion - Órdenes de fabricación

Procedimientos Almacenados
sp_crear_modelo, sp_obtener_modelos, sp_actualizar_modelo

sp_crear_linea, sp_obtener_lineas, sp_cambiar_estado_linea

sp_crear_componente, sp_obtener_componentes, sp_obtener_inventario_completo

sp_crear_orden, sp_obtener_ordenes, sp_actualizar_estado_orden

📊 Datos de Prueba
El sistema incluye 10 registros de prueba por cada tabla principal:

10 modelos de vehículos (sedanes, SUVs y pickups)

10 líneas de producción con diferentes configuraciones

10 componentes con sus respectivos inventarios

10 órdenes de producción en distintos estados

🎨 Interfaz de Usuario
La interfaz está organizada en pestañas (Notebook) con:

Formularios de entrada para cada módulo

Botones de acción (Guardar, Actualizar, Eliminar, Limpiar)

Campos validados y comboboxes para selecciones predefinidas

Diseño limpio con códigos de colores para diferentes acciones

⚙️ Funcionalidades Implementadas
✅ Guardar nuevos registros en la base de datos

✅ Validación de campos obligatorios

✅ Limpieza de formularios

✅ Conexión a base de datos con manejo de errores

✅ Uso de procedimientos almacenados

✅ Mensajes de confirmación y error

🚧 Funcionalidades Pendientes
⬜ Carga de datos en Treeview para visualización

⬜ Actualización de registros existentes

⬜ Eliminación de registros

⬜ Búsqueda y filtrado de información

⬜ Reportes y estadísticas

📝 Notas Importantes
El archivo database_config.py debe ser creado por el usuario con sus credenciales de MySQL

Los procedimientos almacenados están optimizados para MySQL

La aplicación utiliza messagebox para mostrar mensajes al usuario

Los combobox tienen estado "readonly" para evitar entradas inválidas

🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

✨ Autor
Desarrollado como parte de un sistema de gestión para la industria automotriz.
