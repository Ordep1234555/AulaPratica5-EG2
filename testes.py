import pytest

def test_lista_vazia():
    numeros = []
    resultado = calcular_media(numeros)
    assert resultado == 0

def test_lista_com_valores():
    numeros = [1, 2, 3, 4, 5]
    resultado = calcular_media(numeros)
    assert resultado == 3.0

def test_lista_com_valor_negativo():
    numeros = [-1, 2, 3, 4, 5]
    resultado = calcular_media(numeros)
    assert resultado == 2.6
