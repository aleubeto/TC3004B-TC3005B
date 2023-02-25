import pytest
from src.main import newDrink

def test_name():
    # Nombre debe contener solo caracteres alfabéticos
    # Nombre no puede contener caracteres no alfabéticos
    # Nombre no puede tener una longitud menor que dos caracteres
    # Nombre debe tener una longitud de entre 2 a 15 caracteres
    # Nombre puede una extensión de dos caracteres
    # Nombre puede tener una extensión de 15 caracteres
    # Nombre no puede tener una extensión de 1 caracter
    # Nombre no puede tener una extensión de más de 15 caracteres
    assert True


def test_size():
    # Tamaño no puede ser decimal
    # Tamaño es numérico
    # Tamaño no puede incluir valores no numéricos
    # Los tamaños deben estar ordenados de forma ascendente
    # Los tamaños no pueden no estar ordenados
    # Deben ingresarse de 1 a 5 tamaños
    # No pueden haber más de 5 tamaños
    # Tamaño no puede ser menor que 1
    # Tamaño debe encontrarse en un rango de 1 a 48
    # Tamaño no puede ser mayor de 48
    # Tamaño es un número entero
    assert True


def test_string():
    # Nombre debe estár al inicio de la cadena
    # Nombre no puede no estár al inicio de la cadena
    # Se debe separar cada dato con una coma
    # No pueden ingresarse datos si no están separados por coma
    # La entrada puede contener espacios en blanco
    # La entrada puede no tener espacios en blanco
    assert True