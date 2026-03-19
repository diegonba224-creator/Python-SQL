import os    # Se importa la libreria os
def limpiar_terminal():    # Se crea la funcion limpar_terminal
        os.system("cls")    # Ejecuto el comando cls
limpiar_terminal()       # Llamo la funcion creada


import tkinter as tk # Se importa la librería tkinter con el alias tk para facilitar su uso en el código. Tkinter es una biblioteca de Python que se utiliza para crear interfaces gráficas de usuario (GUI). Al importar tkinter como tk, se pueden acceder a sus funciones y clases utilizando el prefijo tk., lo que hace que el código sea más legible y organizado.
from tkinter import messagebox # Se importa el módulo messagebox de la biblioteca tkinter. El módulo messagebox proporciona funciones para mostrar cuadros de diálogo emergentes que pueden contener mensajes, advertencias, errores o preguntas al usuario. Al importar messagebox, se pueden utilizar sus funciones para mostrar mensajes informativos o solicitar confirmación al usuario en la interfaz gráfica creada con tkinter.
from tkinter import ttk # Se importa el módulo ttk de la biblioteca tkinter. El módulo ttk proporciona una colección de widgets mejorados y estilos para crear interfaces gráficas más modernas y atractivas. Al importar ttk, se pueden utilizar sus widgets y estilos específicos para mejorar la apariencia y funcionalidad de la interfaz gráfica creada con tkinter.
import mysql.connector


# Conexión a la base de datos MySQL

def get_connection():
    """Establece y retorna una conexión a la base de datos"""
    try:
        conexion = mysql.connector.connect( # Se intenta establecer una conexión a la base de datos MySQL utilizando el módulo mysql.connector. Se pasan los parámetros necesarios para la conexión, como el host, usuario, contraseña y nombre de la base de datos. Si la conexión es exitosa, se retorna el objeto de conexión.
            host="localhost",
            user="root",
            password="",
            database="autofactory"
        )
        if conexion.is_connected(): # Se verifica si la conexión se ha establecido correctamente utilizando el método is_connected() del objeto de conexión. Si la conexión es exitosa, se imprime un mensaje de éxito en la consola y se retorna el objeto de conexión para su uso posterior en el programa.
            print("✅ Conexión exitosa a MySQL") # Se imprime un mensaje de éxito en la consola indicando que la conexión a MySQL se ha establecido correctamente.
            return conexion # Se retorna el objeto de conexión para su uso posterior en el programa.
    except mysql.connector.Error as e: # Se captura cualquier excepción de tipo mysql.connector.Error que pueda ocurrir durante el intento de conexión a la base de datos. Si ocurre un error, se imprime un mensaje de error en la consola y se muestra un cuadro de diálogo emergente utilizando messagebox.showerror() para informar al usuario sobre el problema de conexión.
        print(f"❌ Error de conexión: {e}") # Se imprime un mensaje de error en la consola indicando que ha ocurrido un error de conexión, junto con el mensaje de error específico (e) que proporciona detalles sobre lo que salió mal durante el intento de conexión a la base de datos.
        messagebox.showerror("Error de Conexión",  #    Se muestra un cuadro de diálogo emergente utilizando messagebox.showerror() para informar al usuario sobre el problema de conexión a la base de datos. El cuadro de diálogo tiene el título "Error de Conexión" y el mensaje que se muestra incluye el texto "No se pudo conectar a la base de datos:" seguido del mensaje de error específico (e) que proporciona detalles sobre lo que salió mal durante el intento de conexión.
                            f"No se pudo conectar a la base de datos:\n{e}") # Se muestra un cuadro de diálogo emergente utilizando messagebox.showerror() para informar al usuario sobre el problema de conexión a la base de datos. El cuadro de diálogo tiene el título "Error de Conexión" y el mensaje que se muestra incluye el texto "No se pudo conectar a la base de datos:" seguido del mensaje de error específico (e) que proporciona detalles sobre lo que salió mal durante el intento de conexión.
        return None

# Elimina la función get_conection() anterior y usa esta

# Crear la ventana principal
root = tk.Tk()  #     Se crea la ventana principal de la aplicación utilizando Tkinter. Esta ventana servirá como contenedor para todos los widgets y elementos de la interfaz gráfica.
root.geometry('850x500') # Se establece el tamaño de la ventana principal a 850 píxeles de ancho y 500 píxeles de alto. Esto define el espacio disponible para colocar los widgets y organizar la interfaz.
root.title("Autofactory - Sistema de Gestión Automotriz") # Se asigna un título a la ventana principal, que se mostrará en la barra de título de la ventana. En este caso, el título es "Autofactory - Sistema de Gestión Automotriz", lo que indica el propósito de la aplicación.

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root) # Se crea un widget Notebook utilizando el módulo ttk de Tkinter. El Notebook es un contenedor que permite organizar la interfaz en pestañas, lo que facilita la navegación y organización de diferentes secciones de la aplicación. Al crear el Notebook, se le pasa como argumento la ventana principal (root) para que se integre dentro de ella. Esto permitirá agregar diferentes frames o páginas al Notebook, cada una representando una pestaña con su propio contenido y funcionalidad.

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)  # Modelos de Vehículos 
tab2 = ttk.Frame(notebook)  # Líneas Producción
tab3 = ttk.Frame(notebook)  # Componentes
tab4 = ttk.Frame(notebook)  # Órdenes Producción

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Modelos") # Se añade el frame tab1 al widget notebook y se le asigna el texto "Modelos" que aparecerá en la pestaña correspondiente. Esto permite organizar la interfaz en diferentes secciones, cada una con su propio contenido y funcionalidad.
notebook.add(tab2, text="Líneas Producción")
notebook.add(tab3, text="Componentes")
notebook.add(tab4, text="Órdenes Producción")

# Empaquetar el Notebook para que se muestre en la ventana
notebook.pack(expand=True, fill="both") # Se empaqueta el widget notebook para que se expanda y llene todo el espacio disponible en la ventana principal. Esto asegura que las pestañas y su contenido se ajusten al tamaño de la ventana y se muestren correctamente.

# ==================== PESTAÑA 1: MODELOS DE VEHÍCULOS ====================
titulo1 = tk.Label(tab1, # Se crea un widget Label para mostrar el título "FORMULARIO DE MODELOS" en la pestaña 1 (tab1). El texto se muestra con una fuente Arial de tamaño 16, en negrita, y con color azul. El método pack() se utiliza para colocar el widget en la interfaz, con un espacio vertical de 20 píxeles (pady=20) para separar el título del resto del contenido.
                  text="FORMULARIO DE MODELOS",
                  font=("Arial", 16, "bold"),
                  fg="blue")
titulo1.pack(pady=20) 

# Frame para contener el formulario
form_frame1 = tk.Frame(tab1) # Se crea un widget Frame dentro de la pestaña 1 (tab1) para contener el formulario de entrada de datos. Este frame servirá como contenedor para organizar los widgets relacionados con el formulario, como etiquetas y campos de entrada. El frame se empaqueta con un espacio vertical de 20 píxeles (pady=20), alineado a la izquierda (anchor="w") y con un margen horizontal de 50 píxeles (padx=50) para separar el formulario del borde de la ventana.
form_frame1.pack(pady=20, anchor="w", padx=50) # Se empaqueta el frame form_frame1 para que se muestre en la pestaña 1 (tab1). El método pack() se utiliza para colocar el frame en la interfaz, con un espacio vertical de 20 píxeles (pady=20), alineado a la izquierda (anchor="w") y con un margen horizontal de 50 píxeles (padx=50) para separar el formulario del borde de la ventana. Esto asegura que el formulario esté bien organizado y visualmente separado del borde de la ventana.

# Fila 1: Código único
tk.Label(form_frame1, text="Código:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10) # Se crea un widget Label para mostrar el texto "Código:" en la primera fila del formulario dentro del frame form_frame1. El texto se muestra con una fuente Arial de tamaño 12. El método grid() se utiliza para colocar el widget en la cuadrícula del frame, en la fila 1 (row=1) y columna 0 (column=0). El argumento sticky="w" alinea el texto a la izquierda, padx=(0, 10) agrega un espacio horizontal de 10 píxeles a la derecha del widget, y pady=10 agrega un espacio vertical de 10 píxeles para separar el widget de los demás elementos del formulario.
codigo = tk.Entry(form_frame1, width=25, font=("Arial", 12), relief="solid", bd=1) # Se crea un widget Entry para permitir al usuario ingresar el código único del modelo de vehículo. El widget se coloca en la primera fila (row=1) y segunda columna (column=1) del frame form_frame1 utilizando el método grid(). El widget tiene un ancho de 25 caracteres, utiliza una fuente Arial de tamaño 12, tiene un borde sólido (relief="solid") y un grosor de borde de 1 píxel (bd=1). Esto proporciona un campo de entrada visualmente definido para que el usuario pueda ingresar el código del modelo.
codigo.grid(row=1, column=1, sticky="w", pady=10) # Se coloca el widget Entry para el código en la primera fila (row=1) y segunda columna (column=1) del frame form_frame1 utilizando el método grid(). El argumento sticky="w" alinea el widget a la izquierda, y pady=10 agrega un espacio vertical de 10 píxeles para separar el widget de los demás elementos del formulario. Esto asegura que el campo de entrada para el código esté bien posicionado y visualmente separado de otros campos en la interfaz.

# Fila 2: Nombre
tk.Label(form_frame1, text="Nombre:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
nombre = tk.Entry(form_frame1, width=25, font=("Arial", 12), relief="solid", bd=1)
nombre.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Categoría (sedan, SUV, pickup)
tk.Label(form_frame1, text="Categoría:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
categoria = ttk.Combobox(form_frame1, values=["Sedan", "SUV", "Pickup"], width=23, font=("Arial", 12), state="readonly") # Se crea un widget Combobox para permitir al usuario seleccionar la categoría del modelo de vehículo (sedan, SUV o pickup). El widget se coloca en la tercera fila (row=3) y segunda columna (column=1) del frame form_frame1 utilizando el método grid(). El Combobox tiene un ancho de 23 caracteres, utiliza una fuente Arial de tamaño 12, y su estado es "readonly", lo que significa que el usuario solo puede seleccionar una opción de la lista desplegable y no puede ingresar texto manualmente. Esto proporciona una forma controlada de seleccionar la categoría del modelo.
categoria.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Versiones disponibles
tk.Label(form_frame1, text="Versiones:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
versiones = tk.Entry(form_frame1, width=25, font=("Arial", 12), relief="solid", bd=1)
versiones.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Tiempo estándar ensamblaje
tk.Label(form_frame1, text="Tiempo ensamblaje:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
tiempo = tk.Entry(form_frame1, width=25, font=("Arial", 12), relief="solid", bd=1)
tiempo.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Componentes requeridos
tk.Label(form_frame1, text="Componentes req:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
componentes = tk.Entry(form_frame1, width=25, font=("Arial", 12), relief="solid", bd=1)
componentes.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Especificaciones técnicas
tk.Label(form_frame1, text="Especificaciones:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
especificaciones = tk.Entry(form_frame1, width=25, font=("Arial", 12), relief="solid", bd=1)
especificaciones.grid(row=7, column=1, sticky="w", pady=10)

# Frame para botones
button_frame1 = tk.Frame(tab1) # Se crea un widget Frame dentro de la pestaña 1 (tab1) para contener los botones de acción relacionados con el formulario de modelos de vehículos. Este frame servirá como contenedor para organizar los botones de guardar, actualizar, eliminar y limpiar. El frame se empaqueta con un espacio vertical de 20 píxeles (pady=20) para separar los botones del formulario y mejorar la apariencia visual de la interfaz.
button_frame1.pack(pady=20) # Se empaqueta el frame button_frame1 para que se muestre en la pestaña 1 (tab1). El método pack() se utiliza para colocar el frame en la interfaz, con un espacio vertical de 20 píxeles (pady=20) para separar los botones del formulario y mejorar la apariencia visual de la interfaz. Esto asegura que los botones estén bien organizados y visualmente separados del formulario de entrada de datos.

btn_save1 = tk.Button(button_frame1, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10) # Se crea un widget Button para el botón "Guardar" dentro del frame button_frame1. El botón tiene el texto "Guardar", utiliza una fuente Arial de tamaño 12, tiene un fondo verde (#4CAF50), texto en color blanco, y un ancho de 10 caracteres. Este botón se utilizará para guardar la información ingresada en el formulario de modelos de vehículos.
btn_save1.pack(side=tk.LEFT, padx=5)

btn_update1 = tk.Button(button_frame1, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10) 

btn_delete1 = tk.Button(button_frame1, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete1.pack(side=tk.LEFT, padx=5)

btn_clear1 = tk.Button(button_frame1, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear1.pack(side=tk.LEFT, padx=5)

# ==================== FUNCIONES PARA MODELOS DE VEHÍCULOS ====================
def guardar_modelo():
    """Función para guardar un nuevo modelo en la base de datos""" 
    
    # 1. Obtener los datos del formulario
    cod = codigo.get() # Se obtiene el valor ingresado en el campo de entrada para el código del modelo utilizando el método get() del widget Entry llamado codigo. Este valor se almacena en la variable cod para su posterior uso en la función de guardado.
    nom = nombre.get() # Se obtiene el valor ingresado en el campo de entrada para el nombre del modelo utilizando el método get() del widget Entry llamado nombre. Este valor se almacena en la variable nom para su posterior uso en la función de guardado.
    cat = categoria.get() 
    ver = versiones.get()
    tiem = tiempo.get()
    comp = componentes.get()
    esp = especificaciones.get()
    
    # 2. Validar que los campos obligatorios no estén vacíos
    if not cod or not nom or not cat: # Se verifica si las variables cod, nom o cat están vacías (es decir, si el usuario no ingresó un valor en alguno de estos campos). Si alguna de estas variables está vacía, se muestra un mensaje de error utilizando messagebox.showerror() con el título "Error" y el mensaje "Código, Nombre y Categoría son obligatorios". Luego, la función retorna sin continuar con el proceso de guardado, lo que evita que se intente guardar un modelo sin la información mínima requerida.
        messagebox.showerror("Error", "Código, Nombre y Categoría son obligatorios")
        return # Se retorna para salir de la función si los campos obligatorios no están completos.
    
    # 3. Conectar a la base de datos y ejecutar el procedimiento almacenado
    conexion = database_config.obtener_conexion() # Se llama a la función obtener_conexion() del módulo database_config para establecer una conexión con la base de datos. Esta función devuelve un objeto de conexión que se almacena en la variable conexion. Si la conexión es exitosa, se puede utilizar esta variable para ejecutar consultas y procedimientos almacenados en la base de datos.
    if conexion: # Se verifica si la conexión a la base de datos fue exitosa (es decir, si la variable conexion no es None). Si la conexión es exitosa, se procede a ejecutar el bloque de código dentro del if para guardar el modelo en la base de datos. Si la conexión no fue exitosa, no se ejecutará este bloque y no se intentará guardar el modelo.
        try: # Se inicia un bloque try para manejar posibles errores que puedan ocurrir durante la ejecución del código relacionado con la base de datos. Esto permite capturar y manejar cualquier excepción que pueda surgir, como errores de conexión o errores al ejecutar el procedimiento almacenado.
            cursor = conexion.cursor() # Se crea un cursor a partir de la conexión a la base de datos utilizando el método cursor() del objeto conexion. El cursor se utiliza para ejecutar consultas SQL y procedimientos almacenados en la base de datos. Este cursor se almacena en la variable cursor para su posterior uso en la ejecución del procedimiento almacenado.
            
            # Llamar al procedimiento almacenado sp_crear_modelo
            cursor.callproc('sp_crear_modelo', [
                cod,           # p_codigo_unico
                nom,           # p_nombre
                cat.lower(),   # p_categoria (convertimos a minúsculas)
                ver,           # p_versiones
                esp,           # p_especificaciones_tecnicas
                comp,          # p_componentes_requeridos
                int(tiem) if tiem else None  # p_tiempo_estandar_ensamblaje
            ])
            
            # Obtener el resultado (el ID generado)
            for result in cursor.stored_results(): # Se itera sobre los resultados devueltos por el procedimiento almacenado utilizando un bucle for. El método stored_results() del cursor devuelve un generador que produce los resultados de las consultas ejecutadas dentro del procedimiento almacenado. En este caso, se espera que el procedimiento sp_crear_modelo devuelva un resultado que contenga el ID generado para el nuevo modelo insertado en la base de datos.
                id_generado = result.fetchone()[0] # Se obtiene el primer resultado del procedimiento almacenado utilizando el método fetchone() del resultado actual. Este método devuelve una tupla con los valores de la fila resultante. Se accede al primer elemento de la tupla (index 0) para obtener el ID generado para el nuevo modelo insertado en la base de datos, y se almacena en la variable id_generado.
            
            conexion.commit()
            messagebox.showinfo("Éxito", f"Modelo guardado correctamente con ID: {id_generado}") # Se muestra un mensaje de información utilizando messagebox.showinfo() con el título "Éxito" y un mensaje que indica que el modelo se guardó correctamente, incluyendo el ID generado para el nuevo modelo. Esto proporciona retroalimentación al usuario sobre el resultado de la operación de guardado.
            limpiar_campos_modelo() # Se llama a la función limpiar_campos_modelo() para limpiar los campos del formulario después de guardar el modelo en la base de datos. Esta función se encarga de borrar el contenido de los campos de entrada, restablecer las selecciones y dejar el formulario listo para ingresar un nuevo modelo si el usuario lo desea.
            
        except Error as e:
            messagebox.showerror("Error de BD", f"No se pudo guardar: {e}") # Se captura cualquier excepción de tipo Error que ocurra durante la ejecución del bloque try. Si ocurre un error relacionado con la base de datos, se muestra un mensaje de error utilizando messagebox.showerror() con el título "Error de BD" y un mensaje que indica que no se pudo guardar el modelo, incluyendo el mensaje de error específico (e) para proporcionar detalles sobre lo que salió mal.
        finally:
            cursor.close() # Se cierra el cursor utilizando el método close() del objeto cursor para liberar los recursos asociados con el cursor. Esto es importante para evitar fugas de memoria y asegurar que los recursos de la base de datos se gestionen adecuadamente.
            conexion.close() # Se cierra la conexión a la base de datos utilizando el método close() del objeto conexion para liberar los recursos asociados con la conexión. Esto es importante para evitar fugas de memoria y asegurar que los recursos de la base de datos se gestionen adecuadamente.

# ==================== FUNCIONES PARA CARGAR MODELOS ====================
def cargar_modelos():
    """Carga los modelos desde la BD al Treeview""" # Se define una función llamada cargar_modelos() que se encargará de cargar los modelos de vehículos desde la base de datos y mostrarlos en un widget Treeview. Esta función se puede llamar para actualizar la lista de modelos cada vez que se realice una operación de guardado, actualización o eliminación, asegurando que la información mostrada en la interfaz esté siempre actualizada con los datos almacenados en la base de datos.
    # Limpiar treeview
    for row in tree_modelos.get_children(): # Se itera sobre todas las filas actualmente presentes en el widget Treeview llamado tree_modelos utilizando un bucle for. El método get_children() del Treeview devuelve una lista de identificadores de las filas presentes en el Treeview. Para cada identificador de fila (row) obtenido, se llama al método delete() del Treeview para eliminar esa fila del Treeview. Esto se hace para limpiar el Treeview antes de cargar los nuevos datos desde la base de datos, asegurando que no haya información duplicada o desactualizada en la interfaz.
        tree_modelos.delete(row) # Se elimina la fila actual del Treeview utilizando el método delete() del widget tree_modelos, pasando como argumento el identificador de la fila (row) que se desea eliminar. Esto se hace para limpiar el Treeview antes de cargar los nuevos datos desde la base de datos, asegurando que no haya información duplicada o desactualizada en la interfaz.
    
    conexion = get_connection() # Se llama a la función get_connection() para establecer una conexión con la base de datos. Esta función devuelve un objeto de conexión que se almacena en la variable conexion. Si la conexión es exitosa, se puede utilizar esta variable para ejecutar consultas y procedimientos almacenados en la base de datos.
    if conexion: 
        try:
            cursor = conexion.cursor(dictionary=True) # Se crea un cursor a partir de la conexión a la base de datos utilizando el método cursor() del objeto conexion. El argumento dictionary=True se pasa para que los resultados devueltos por el cursor sean en forma de diccionario, lo que facilita el acceso a los valores por nombre de columna en lugar de por índice. Este cursor se almacena en la variable cursor para su posterior uso en la ejecución del procedimiento almacenado.
            cursor.callproc('sp_obtener_modelos') # Se llama al procedimiento almacenado sp_obtener_modelos utilizando el método callproc() del cursor. Este procedimiento almacenado se encarga de obtener la lista de modelos de vehículos desde la base de datos. Al llamar a este procedimiento, se ejecuta la lógica definida en el procedimiento almacenado y se obtienen los resultados correspondientes, que luego se pueden procesar para mostrar en la interfaz.
            
            for result in cursor.stored_results(): # Se itera sobre los resultados devueltos por el procedimiento almacenado utilizando un bucle for. El método stored_results() del cursor devuelve un generador que produce los resultados de las consultas ejecutadas dentro del procedimiento almacenado. En este caso, se espera que el procedimiento sp_obtener_modelos devuelva un conjunto de resultados que contengan la información de los modelos de vehículos almacenados en la base de datos.
                for row in result.fetchall(): # Se itera sobre cada fila del resultado actual utilizando un bucle for. El método fetchall() del resultado devuelve una lista de filas, donde cada fila es un diccionario (debido a dictionary=True al crear el cursor) que contiene los datos de un modelo de vehículo. Para cada fila obtenida, se accede a los valores de las columnas utilizando los nombres de las columnas como claves del diccionario (por ejemplo, row['id'], row['codigo_unico'], etc.) para obtener la información correspondiente a cada modelo.
                    tree_modelos.insert("", tk.END, values=( # Se inserta una nueva fila en el widget Treeview llamado tree_modelos utilizando el método insert(). El primer argumento "" indica que la nueva fila se insertará al nivel raíz del Treeview, el segundo argumento tk.END indica que la nueva fila se agregará al final de la lista de filas existentes, y el argumento values=() se utiliza para especificar los valores que se mostrarán en las columnas de la nueva fila. En este caso, se pasan los valores obtenidos de la fila actual del resultado del procedimiento almacenado, como el ID, código único, nombre, categoría (con la primera letra en mayúscula), tiempo estándar de ensamblaje y versiones disponibles (limitando a 50 caracteres si es necesario). Esto permite mostrar la información de cada modelo de vehículo en la interfaz de manera organizada y legible.
                        row['id'],
                        row['codigo_unico'],
                        row['nombre'],
                        row['categoria'].capitalize(),
                        row['tiempo_estandar_ensamblaje'],
                        (row['versiones'][:50] + "...") if row['versiones'] and len(row['versiones']) > 50 else row['versiones']
                    ))
        except mysql.connector.Error as e: # Se captura cualquier excepción de tipo mysql.connector.Error que ocurra durante la ejecución del bloque try. Si ocurre un error relacionado con la base de datos, se muestra un mensaje de error utilizando messagebox.showerror() con el título "Error" y un mensaje que indica que hubo un error al cargar los modelos, incluyendo el mensaje de error específico (e) para proporcionar detalles sobre lo que salió mal durante la operación de carga de modelos desde la base de datos.
            messagebox.showerror("Error", f"Error al cargar modelos: {e}") # Se muestra un mensaje de error utilizando messagebox.showerror() con el título "Error" y un mensaje que indica que hubo un error al cargar los modelos, incluyendo el mensaje de error específico (e) para proporcionar detalles sobre lo que salió mal durante la operación de carga de modelos desde la base de datos.
        finally:
            cursor.close()
            conexion.close()

def limpiar_campos_modelo():
    """Limpia todos los campos del formulario de modelos"""
    codigo.delete(0, tk.END) # Se borra el contenido del campo de entrada para el código del modelo utilizando el método delete() del widget Entry llamado codigo. El primer argumento 0 indica que se debe comenzar a borrar desde el primer carácter, y tk.END indica que se debe borrar hasta el final del contenido del campo. Esto limpia completamente el campo de entrada para que el usuario pueda ingresar un nuevo código sin tener que eliminar manualmente el contenido anterior.
    nombre.delete(0, tk.END) # Se borra el contenido del campo de entrada para el nombre del modelo utilizando el método delete() del widget Entry llamado nombre. El primer argumento 0 indica que se debe comenzar a borrar desde el primer carácter, y tk.END indica que se debe borrar hasta el final del contenido del campo. Esto limpia completamente el campo de entrada para que el usuario pueda ingresar un nuevo nombre sin tener que eliminar manualmente el contenido anterior.
    categoria.set('') # Se restablece la selección del Combobox para la categoría utilizando el método set() del widget Combobox llamado categoria. Al pasar una cadena vacía ('') como argumento, se borra cualquier selección previa y se deja el Combobox sin una opción seleccionada. Esto permite que el usuario pueda seleccionar una nueva categoría para el modelo sin que quede una selección anterior visible.
    versiones.delete(0, tk.END) # Se borra el contenido del campo de entrada para las versiones disponibles utilizando el método delete() del widget Entry llamado versiones. El primer argumento 0 indica que se debe comenzar a borrar desde el primer carácter, y tk.END indica que se debe borrar hasta el final del contenido del campo. Esto limpia completamente el campo de entrada para que el usuario pueda ingresar nuevas versiones sin tener que eliminar manualmente el contenido anterior.
    tiempo.delete(0, tk.END) # Se borra el contenido del campo de entrada para el tiempo estándar de ensamblaje utilizando el método delete() del widget Entry llamado tiempo. El primer argumento 0 indica que se debe comenzar a borrar desde el primer carácter, y tk.END indica que se debe borrar hasta el final del contenido del campo. Esto limpia completamente el campo de entrada para que el usuario pueda ingresar un nuevo tiempo sin tener que eliminar manualmente el contenido anterior.
    componentes.delete(0, tk.END) # Se borra el contenido del campo de entrada para los componentes requeridos utilizando el método delete() del widget Entry llamado componentes. El primer argumento 0 indica que se debe comenzar a borrar desde el primer carácter, y tk.END indica que se debe borrar hasta el final del contenido del campo. Esto limpia completamente el campo de entrada para que el usuario pueda ingresar nuevos componentes sin tener que eliminar manualmente el contenido anterior.
    especificaciones.delete(0, tk.END) # Se borra el contenido del campo de entrada para las especificaciones técnicas utilizando el método delete() del widget Entry llamado especificaciones. El primer argumento 0 indica que se debe comenzar a borrar desde el primer carácter, y tk.END indica que se debe borrar hasta el final del contenido del campo. Esto limpia completamente el campo de entrada para que el usuario pueda ingresar nuevas especificaciones sin tener que eliminar manualmente el contenido anterior.

# Ahora, asocia la función al botón Guardar
btn_save1.config(command=guardar_modelo) # Se configura el botón btn_save1 para que ejecute la función guardar_modelo() cuando se haga clic en él. Esto se logra utilizando el método config() del widget Button, pasando el argumento command=guardar_modelo. De esta manera, cuando el usuario haga clic en el botón "Guardar", se ejecutará la función guardar_modelo() que se encargará de obtener los datos del formulario, validar los campos, conectar a la base de datos y ejecutar el procedimiento almacenado para guardar el nuevo modelo de vehículo.
btn_clear1.config(command=limpiar_campos_modelo) # Se configura el botón btn_clear1 para que ejecute la función limpiar_campos_modelo() cuando se haga clic en él. Esto se logra utilizando el método config() del widget Button, pasando el argumento command=limpiar_campos_modelo. De esta manera, cuando el usuario haga clic en el botón "Limpiar", se ejecutará la función limpiar_campos_modelo() que se encargará de borrar el contenido de los campos de entrada del formulario de modelos, restablecer las selecciones y dejar el formulario listo para ingresar un nuevo modelo si el usuario lo desea.

# ==================== PESTAÑA 2: LÍNEAS DE PRODUCCIÓN ====================
titulo2 = tk.Label(tab2, text="FORMULARIO DE LÍNEAS PRODUCCIÓN", font=("Arial", 16, "bold"), fg="green") # Se crea un widget Label para mostrar el título "FORMULARIO DE LÍNEAS PRODUCCIÓN" en la pestaña 2 (tab2). El texto se muestra con una fuente Arial de tamaño 16, en negrita, y con color verde. El método pack() se utiliza para colocar el widget en la interfaz, con un espacio vertical de 20 píxeles (pady=20) para separar el título del resto del contenido.
titulo2.pack(pady=20) # Se crea un widget Label para mostrar el título "FORMULARIO DE LÍNEAS PRODUCCIÓN" en la pestaña 2 (tab2). El texto se muestra con una fuente Arial de tamaño 16, en negrita, y con color verde. El método pack() se utiliza para colocar el widget en la interfaz, con un espacio vertical de 20 píxeles (pady=20) para separar el título del resto del contenido.

form_frame2 = tk.Frame(tab2) # Se crea un widget Frame dentro de la pestaña 2 (tab2) para contener el formulario de entrada de datos relacionado con las líneas de producción. Este frame servirá como contenedor para organizar los widgets relacionados con el formulario, como etiquetas y campos de entrada. El frame se empaqueta con un espacio vertical de 20 píxeles (pady=20), alineado a la izquierda (anchor="w") y con un margen horizontal de 50 píxeles (padx=50) para separar el formulario del borde de la ventana.
form_frame2.pack(pady=20, anchor="w", padx=50) # Se empaqueta el frame form_frame2 para que se muestre en la pestaña 2 (tab2). El método pack() se utiliza para colocar el frame en la interfaz, con un espacio vertical de 20 píxeles (pady=20), alineado a la izquierda (anchor="w") y con un margen horizontal de 50 píxeles (padx=50) para separar el formulario del borde de la ventana. Esto asegura que el formulario esté bien organizado y visualmente separado del borde de la ventana.

# Fila 1: Número de línea
tk.Label(form_frame2, text="N° Línea:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
num_linea = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
num_linea.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Tipo vehículos (sedan, SUV, pickup)
tk.Label(form_frame2, text="Tipo vehículos:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
tipo_vehiculos = ttk.Combobox(form_frame2, values=["Sedan", "SUV", "Pickup", "Mixto"], width=23, font=("Arial", 12), state="readonly") # Se crea un widget Combobox para permitir al usuario seleccionar el tipo de vehículos que se producen en la línea de producción (sedan, SUV, pickup o mixto). El widget se coloca en la segunda fila (row=2) y segunda columna (column=1) del frame form_frame2 utilizando el método grid(). El Combobox tiene un ancho de 23 caracteres, utiliza una fuente Arial de tamaño 12, y su estado es "readonly", lo que significa que el usuario solo puede seleccionar una opción de la lista desplegable y no puede ingresar texto manualmente. Esto proporciona una forma controlada de seleccionar el tipo de vehículos para la línea de producción.
tipo_vehiculos.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Capacidad diaria
tk.Label(form_frame2, text="Capacidad diaria:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
capacidad = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
capacidad.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Estaciones trabajo
tk.Label(form_frame2, text="Estaciones trabajo:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
estaciones = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
estaciones.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Supervisor
tk.Label(form_frame2, text="Supervisor:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
supervisor = tk.Entry(form_frame2, width=25, font=("Arial", 12), relief="solid", bd=1)
supervisor.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Turno activo
tk.Label(form_frame2, text="Turno activo:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
turno = ttk.Combobox(form_frame2, values=["Mañana", "Tarde", "Noche"], width=23, font=("Arial", 12), state="readonly") # Se crea un widget Combobox para permitir al usuario seleccionar el turno activo de la línea de producción (matutino, vespertino o nocturno). El widget se coloca en la sexta fila (row=6) y segunda columna (column=1) del frame form_frame2 utilizando el método grid(). El Combobox tiene un ancho de 23 caracteres, utiliza una fuente Arial de tamaño 12, y su estado es "readonly", lo que significa que el usuario solo puede seleccionar una opción de la lista desplegable y no puede ingresar texto manualmente. Esto proporciona una forma controlada de seleccionar el turno activo para la línea de producción.
turno.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Estado operativo
tk.Label(form_frame2, text="Estado operativo:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
estado = ttk.Combobox(form_frame2, values=["Activo", "Mantenimiento", "Inactivo"], width=23, font=("Arial", 12), state="readonly")
estado.grid(row=7, column=1, sticky="w", pady=10)

# Frame para botones
button_frame2 = tk.Frame(tab2) # Se crea un widget Frame dentro de la pestaña 2 (tab2) para contener los botones de acción relacionados con el formulario de líneas de producción. Este frame servirá como contenedor para organizar los botones de guardar, actualizar, eliminar y limpiar. El frame se empaqueta con un espacio vertical de 20 píxeles (pady=20) para separar los botones del formulario y mejorar la apariencia visual de la interfaz.
button_frame2.pack(pady=20) # Se empaqueta el frame button_frame2 para que se muestre en la pestaña 2 (tab2). El método pack() se utiliza para colocar el frame en la interfaz, con un espacio vertical de 20 píxeles (pady=20) para separar los botones del formulario y mejorar la apariencia visual de la interfaz. Esto asegura que los botones estén bien organizados y visualmente separados del formulario de entrada de datos.

btn_save2 = tk.Button(button_frame2, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save2.pack(side=tk.LEFT, padx=5)

btn_update2 = tk.Button(button_frame2, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update2.pack(side=tk.LEFT, padx=5)

btn_delete2 = tk.Button(button_frame2, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete2.pack(side=tk.LEFT, padx=5)

btn_clear2 = tk.Button(button_frame2, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear2.pack(side=tk.LEFT, padx=5)

# ==================== FUNCIONES PARA LÍNEAS DE PRODUCCIÓN ====================
def guardar_linea():
    """Función para guardar una nueva línea de producción"""
    
    # Obtener datos
    num = num_linea.get()
    tipo = tipo_vehiculos.get()
    cap = capacidad.get()
    est = estaciones.get()
    sup = supervisor.get()
    turn = turno.get()
    est_op = estado.get()
    
    if not num or not tipo:
        messagebox.showerror("Error", "Número de línea y tipo son obligatorios")
        return
    
    conexion = database_config.obtener_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Mapear los valores de la interfaz a los valores de la BD
            mapa_turno = {
                'Matutino': 'mañana',
                'Vespertino': 'tarde', 
                'Nocturno': 'noche'
            }
            mapa_estado = {
                'Activo': 'activo',
                'Mantenimiento': 'mantenimiento',
                'Inactivo': 'parado'
            }
            
            cursor.callproc('sp_crear_linea', [
                num,
                tipo,
                int(cap) if cap else None,
                int(est) if est else None,
                sup,
                mapa_turno.get(turn, 'mañana'),
                mapa_estado.get(est_op, 'activo')
            ])
            
            conexion.commit()
            messagebox.showinfo("Éxito", "Línea guardada correctamente")
            
        except Error as e:
            messagebox.showerror("Error de BD", f"No se pudo guardar: {e}")
        finally:
            cursor.close()
            conexion.close()

# Asignar al botón
btn_save2.config(command=guardar_linea) # Se configura el botón btn_save2 para que ejecute la función guardar_linea() cuando se haga clic en él. Esto se logra utilizando el método config() del widget Button, pasando el argumento command=guardar_linea. De esta manera, cuando el usuario haga clic en el botón "Guardar" de la pestaña de líneas de producción, se ejecutará la función guardar_linea() que se encargará de obtener los datos del formulario, validar los campos, conectar a la base de datos y ejecutar el procedimiento almacenado para guardar la nueva línea de producción en la base de datos.

# ==================== FUNCIONES PARA CARGAR LÍNEAS ====================
def cargar_lineas():
    """Carga las líneas desde la BD al Treeview"""
    for row in tree_lineas.get_children():
        tree_lineas.delete(row)
    
    conexion = get_connection()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.callproc('sp_obtener_lineas')
            
            # Mapeo inverso para mostrar en español
            mapa_turno = {'mañana': 'Mañana', 'tarde': 'Tarde', 'noche': 'Noche'}
            mapa_estado = {'activo': 'Activo', 'mantenimiento': 'Mantenimiento', 'parado': 'Inactivo'}
            
            for result in cursor.stored_results():
                for row in result.fetchall():
                    tree_lineas.insert("", tk.END, values=(
                        row['id'],
                        row['numero_linea'],
                        row['tipo_vehiculos_ensambla'],
                        row['capacidad_diaria'],
                        row['numero_estaciones_trabajo'],
                        row['supervisor_responsable'],
                        mapa_turno.get(row['turno_activo'], row['turno_activo']),
                        mapa_estado.get(row['estado_operativo'], row['estado_operativo'])
                    ))
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error al cargar líneas: {e}")
        finally:
            cursor.close()
            conexion.close()

# ==================== PESTAÑA 3: COMPONENTES Y PARTES ====================
titulo3 = tk.Label(tab3, text="FORMULARIO DE COMPONENTES", font=("Arial", 16, "bold"), fg="red")
titulo3.pack(pady=20)

form_frame3 = tk.Frame(tab3) # Se crea un widget Frame dentro de la pestaña 3 (tab3) para contener el formulario de entrada de datos relacionado con los componentes y partes. Este frame servirá como contenedor para organizar los widgets relacionados con el formulario, como etiquetas y campos de entrada. El frame se empaqueta con un espacio vertical de 20 píxeles (pady=20), alineado a la izquierda (anchor="w") y con un margen horizontal de 50 píxeles (padx=50) para separar el formulario del borde de la ventana.
form_frame3.pack(pady=20, anchor="w", padx=50)

# Fila 1: Código componente
tk.Label(form_frame3, text="Código:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
codigo_comp = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
codigo_comp.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Descripción
tk.Label(form_frame3, text="Descripción:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
descripcion = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
descripcion.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Categoría
tk.Label(form_frame3, text="Categoría:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
categoria_comp = ttk.Combobox(form_frame3, values=["Motor", "Transmisión", "Suspensión", "Eléctrico", "Carrocería"], # Se crea un widget Combobox para permitir al usuario seleccionar la categoría del componente (Motor, Transmisión, Suspensión, Eléctrico o Carrocería). El widget se coloca en la tercera fila (row=3) y segunda columna (column=1) del frame form_frame3 utilizando el método grid(). El Combobox tiene un ancho de 23 caracteres, utiliza una fuente Arial de tamaño 12, y su estado es "readonly", lo que significa que el usuario solo puede seleccionar una opción de la lista desplegable y no puede ingresar texto manualmente. Esto proporciona una forma controlada de seleccionar la categoría del componente.
                            width=23, font=("Arial", 12), state="readonly") 
categoria_comp.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Proveedor principal
tk.Label(form_frame3, text="Proveedor:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
proveedor = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
proveedor.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Tiempo entrega (días)
tk.Label(form_frame3, text="Tiempo entrega:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
tiempo_entrega = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
tiempo_entrega.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Costo unitario
tk.Label(form_frame3, text="Costo unitario:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
costo = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
costo.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Stock mínimo
tk.Label(form_frame3, text="Stock mínimo:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
stock = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
stock.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Especificaciones técnicas
tk.Label(form_frame3, text="Especificaciones:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
especificaciones_comp = tk.Entry(form_frame3, width=25, font=("Arial", 12), relief="solid", bd=1)
especificaciones_comp.grid(row=8, column=1, sticky="w", pady=10)

# Frame para inventario
inventario_frame = tk.Frame(tab3)
inventario_frame.pack(pady=10, padx=50, anchor="w")

tk.Label(inventario_frame, text="Inventario - Cantidad:", font=("Arial", 12)).grid(row=0, column=0, padx=(0, 10), pady=5)
cantidad = tk.Entry(inventario_frame, width=10, font=("Arial", 12), relief="solid", bd=1)
cantidad.grid(row=0, column=1, pady=5)

tk.Label(inventario_frame, text="Calidad:", font=("Arial", 12)).grid(row=0, column=2, padx=(20, 10), pady=5)
calidad = ttk.Combobox(inventario_frame, values=["Aprobado", "En revisión", "Rechazado"], width=15, font=("Arial", 12), state="readonly")
calidad.grid(row=0, column=3, pady=5)

# Frame para botones
button_frame3 = tk.Frame(tab3)
button_frame3.pack(pady=20)

btn_save3 = tk.Button(button_frame3, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save3.pack(side=tk.LEFT, padx=5)

btn_update3 = tk.Button(button_frame3, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update3.pack(side=tk.LEFT, padx=5)

btn_delete3 = tk.Button(button_frame3, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete3.pack(side=tk.LEFT, padx=5)

btn_clear3 = tk.Button(button_frame3, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear3.pack(side=tk.LEFT, padx=5)

# ==================== PESTAÑA 4: ÓRDENES DE PRODUCCIÓN ====================
titulo4 = tk.Label(tab4, text="FORMULARIO DE ÓRDENES PRODUCCIÓN", font=("Arial", 16, "bold"), fg="purple")
titulo4.pack(pady=20)

form_frame4 = tk.Frame(tab4)
form_frame4.pack(pady=20, anchor="w", padx=50)

# Fila 1: Número orden
tk.Label(form_frame4, text="N° Orden:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0, 10), pady=10)
num_orden = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
num_orden.grid(row=1, column=1, sticky="w", pady=10)

# Fila 2: Fecha emisión
tk.Label(form_frame4, text="Fecha emisión:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0, 10), pady=10)
fecha_emision = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
fecha_emision.insert(0, "2024-01-15")
fecha_emision.grid(row=2, column=1, sticky="w", pady=10)

# Fila 3: Modelo vehículo (relación con Módulo 1)
tk.Label(form_frame4, text="Modelo vehículo:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0, 10), pady=10)
modelo_orden = ttk.Combobox(form_frame4, values=["Sedan Básico", "SUV Familiar", "Pickup Trabajo"], 
                           width=23, font=("Arial", 12), state="readonly")
modelo_orden.grid(row=3, column=1, sticky="w", pady=10)

# Fila 4: Cantidad a producir
tk.Label(form_frame4, text="Cantidad:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0, 10), pady=10)
cantidad_prod = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
cantidad_prod.grid(row=4, column=1, sticky="w", pady=10)

# Fila 5: Fecha inicio programada
tk.Label(form_frame4, text="Fecha inicio:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0, 10), pady=10)
fecha_inicio = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
fecha_inicio.grid(row=5, column=1, sticky="w", pady=10)

# Fila 6: Fecha fin estimada
tk.Label(form_frame4, text="Fecha fin est.:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0, 10), pady=10)
fecha_fin = tk.Entry(form_frame4, width=25, font=("Arial", 12), relief="solid", bd=1)
fecha_fin.grid(row=6, column=1, sticky="w", pady=10)

# Fila 7: Prioridad
tk.Label(form_frame4, text="Prioridad:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=(0, 10), pady=10)
prioridad = ttk.Combobox(form_frame4, values=["Alta", "Media", "Baja"], width=23, font=("Arial", 12), state="readonly")
prioridad.grid(row=7, column=1, sticky="w", pady=10)

# Fila 8: Estado actual
tk.Label(form_frame4, text="Estado:", font=("Arial", 12)).grid(row=8, column=0, sticky="w", padx=(0, 10), pady=10)
estado_orden = ttk.Combobox(form_frame4, values=["Planificada", "En producción", "Completada", "Cancelada"], 
                           width=23, font=("Arial", 12), state="readonly")
estado_orden.grid(row=8, column=1, sticky="w", pady=10)

# Fila 9: Línea producción (relación con Módulo 2)
tk.Label(form_frame4, text="Línea producción:", font=("Arial", 12)).grid(row=9, column=0, sticky="w", padx=(0, 10), pady=10)
linea_prod = ttk.Combobox(form_frame4, values=["Línea 1 - Sedan", "Línea 2 - SUV", "Línea 3 - Pickup"], 
                         width=23, font=("Arial", 12), state="readonly")
linea_prod.grid(row=9, column=1, sticky="w", pady=10)

# Frame para botones
button_frame4 = tk.Frame(tab4)
button_frame4.pack(pady=20)

btn_save4 = tk.Button(button_frame4, text="Guardar", font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
btn_save4.pack(side=tk.LEFT, padx=5)

btn_update4 = tk.Button(button_frame4, text="Actualizar", font=("Arial", 12), bg="#2196F3", fg="white", width=10)
btn_update4.pack(side=tk.LEFT, padx=5)

btn_delete4 = tk.Button(button_frame4, text="Eliminar", font=("Arial", 12), bg="#f44336", fg="white", width=10)
btn_delete4.pack(side=tk.LEFT, padx=5)

btn_clear4 = tk.Button(button_frame4, text="Limpiar", font=("Arial", 12), bg="#FF9800", fg="white", width=10)
btn_clear4.pack(side=tk.LEFT, padx=5)

# Frame informativo sobre relaciones
info_frame = tk.Frame(tab4, bg="#f0f0f0", relief="groove", bd=2)
info_frame.pack(pady=10, padx=50, fill="x")

tk.Label(info_frame, text="RELACIONES ENTRE MÓDULOS:", font=("Arial", 10, "bold"), 
        bg="#f0f0f0").pack()
tk.Label(info_frame, 
        text="• Órdenes de Producción → Modelo (selecciona el modelo a fabricar)\n• Órdenes de Producción → Línea (asigna a una línea específica)\n• Modelos → Componentes (cada modelo requiere componentes específicos)", 
        font=("Arial", 9), bg="#f0f0f0", justify=tk.LEFT).pack()

root.mainloop()

