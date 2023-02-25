import pytest
from src.main import newDrink, validateName, validateSize

@pytest.mark.parametrize(
    "input,expected",
    [
        # Válido: Nombre debe contener solo caracteres alfabéticos
        ('abcdefg',True),

        # Válido: Nombre debe tener una longitud de entre 2 a 15 caracteres
        ('Frescolita',True),

        # Válido: Nombre puede una extensión de dos caracteres
        ('Lu',True),

        # Válido: Nombre puede tener una extensión de 15 caracteres
        ('TingleTangoFizz',True),

        # Inválido: Nombre no puede contener caracteres no alfabéticos
        ('c0cac0!a',False),

        # Inválido: Nombre no puede tener una longitud menor que dos caracteres
        ('',False),

        # Inválido: Nombre no puede tener una extensión de 1 caracter
        ('A',False),

        # Inválido: Nombre no puede tener una extensión de más de 15 caracteres
        ('ChillaCherryCrush',False)
    ]
)
def test_validateName(input,expected):
    assert validateName(input) == expected


@pytest.mark.parametrize(
    'input,expected',
    [
        # Inválido: Tamaño no puede ser decimal
        ('',True),

        # Válido: Tamaño es numérico
        ('',True),

        # Inválido: Tamaño no puede incluir valores no numéricos
        ('',True),

        # Válido: Los tamaños deben estar ordenados de forma ascendente
        ('',True),

        # Inválido: Los tamaños no pueden no estár ordenados
        ('',True),

        # Válido: Deben ingresarse de 1 a 5 tamaños
        ('',True),

        # Inválido: No pueden haber más de 5 tamaños
        ('',True),

        # Inválido: Tamaño no puede ser menor que 1
        ('',True),

        # Válido: Tamaño debe encontrarse en un rango de 1 a 48
        ('',True),

        # Tamaño no puede ser mayor de 48
        ('',True),

        # Tamaño es un número entero
        ('',True)
    ]
)
def test_validateSize(input,expected):
    assert validateSize(input) == expected

    # Nombre debe estár al inicio de la cadena
    # Nombre no puede no estár al inicio de la cadena
    # Se debe separar cada dato con una coma
    # No pueden ingresarse datos si no están separados por coma
    # La entrada puede contener espacios en blanco
    # La entrada puede no tener espacios en blanco
