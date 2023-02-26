import pytest
from src.main import validateName, validateSize, validateString

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
        # 0.-Válido: Tamaño es numérico
        (['2','5','8'],True),

        # 1.-Válido: Los tamaños deben estar ordenados de forma ascendente
        (['1','2','3'],True),

        # 2.-Válido: Deben ingresarse de 1 a 5 tamaños
        (['1','2','3','4','5'],True),

        # 3.-Válido: Tamaño debe encontrarse en un rango de 1 a 48
        (['1','48'],True),

        # 4.-Válido: Tamaño es un número entero
        (['1'],True),

        # 5.-Inválido: Tamaño no puede incluir valores no numéricos
        (['a','2','3'],False),

        # 6.-Inválido: Tamaño no puede tener valores decimales
        (['1','2.3'],False),

        # 7.-Inválido: Los valores de Tamaño no pueden no estár ordenados
        (['3','2','1'],False),

        # 8.-Inválido: No pueden haber más de 5 tamaños
        (['1','2','3','4','5','6'],False),

        # 9.-Inválido: Tamaño no puede tener valores menores que 1
        (['0'],False),

        # 10.-Inválido: Tamaño no puede tener valores mayores de 48
        (['49'],False),

        # 11.-Inválido: Tamaño no puede contener valores repetidos
        (['1','2','2','3'],False)

    ]
)
def test_validateSize(input,expected):
    assert validateSize(input) == expected


@pytest.mark.parametrize(
    'input,expected',
    [
        # Válido: Nombre debe estár al inicio de la cadena
        ('TingleTangoFizz, 2, 5, 8',True),

        # Inválido: Nombre no puede no estár al inicio de la cadena
        ('2, TingleTangoFizz, 5, 8',False),

        # Válido: Se debe separar cada dato con una coma
        ('Frescolita, 2, 5, 8',True),

        # Inválido: No pueden ingresarse datos si no están separados por coma
        ('Frescolita-2-5-8',False),

        # Válido: La entrada puede contener espacios en blanco
        ('Sprite, 3, 6, 9',True),

        # Válido: La entrada puede no tener espacios en blanco
        ('Sprite,3,6,9',True)
    ]
)
def test_validateString(input,expected):
    assert validateString(input) == expected
