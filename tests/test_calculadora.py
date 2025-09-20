# tests/test_calculadora.py
import pytest
from src.calculadora import somar, dividir, multiplicar, subtrair

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_subtrair():
    assert subtrair(2, 3) == -1
    assert subtrair(3, 3) == 0
    assert subtrair(100, 0) == 100
    assert subtrair(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(0, 3) == 0
    assert multiplicar(2, 0) == 0
    assert multiplicar(2, 2) == 4
    assert multiplicar(2, -3) == -6
    assert multiplicar(-2, -3) == 6