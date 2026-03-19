# utils/helpers.py
import re
from datetime import datetime

def validar_codigo(codigo):
    """Valida que el código tenga el formato correcto"""
    patron = r'^[A-Z0-9-]{3,20}$'
    return bool(re.match(patron, codigo))

def validar_email(email):
    """Valida que el email tenga formato correcto"""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

def formatear_fecha(fecha):
    """Formatea una fecha a string YYYY-MM-DD"""
    if isinstance(fecha, datetime):
        return fecha.strftime('%Y-%m-%d')
    return fecha

def formatear_moneda(valor):
    """Formatea un valor como moneda"""
    try:
        return f"${float(valor):,.2f}"
    except:
        return "$0.00"

def truncar_texto(texto, longitud=50):
    """Trunca un texto a una longitud determinada"""
    if texto and len(texto) > longitud:
        return texto[:longitud] + "..."
    return texto

def obtener_fecha_actual():
    """Retorna la fecha actual en formato YYYY-MM-DD"""
    return datetime.now().strftime('%Y-%m-%d')
