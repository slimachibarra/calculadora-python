import pytest
from calculadora import sumar, dividir

# Caso exitoso
def test_suma_correcta():
    assert sumar(10, 5) == 15

# Caso de error
def test_division_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

# Caso borde (edge case)
def test_suma_con_cero():
    assert sumar(0, 5) == 5