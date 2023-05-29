from cromannumbers_clase import RomanNumber
import pytest


def test_instanciar_un_numero_romano():
    romano = RomanNumber(23)
    assert romano.numero == 23
    assert romano.simbolo == "XXIII"

def test_instanciar_otro():
    romano = RomanNumber(13)
    assert romano.numero == 13
    assert romano.simbolo == "XIII"


def test_instanciar_con_simbolo():
    romano = RomanNumber("XI")
    assert romano.numero == 11
    assert romano.simbolo == "XI"

def test_cambiar_valor_de_romano():
    romano = RomanNumber(1)
    assert romano.numero == 1
    assert romano.simbolo =="I"

    romano.numero = 2
    assert romano.numero == 2
    assert romano.simbolo == "II"

    romano.simbolo ="III"
    assert romano.numero == 3
    assert romano.simbolo == "III"


def test_multiplicacion():
    romano1 = RomanNumber("X")
    romano2 = RomanNumber(5)
    assert romano1 * romano2 == RomanNumber("L")
    assert romano1 *5 == RomanNumber(50)
    assert romano1 * "V" == RomanNumber(50)



    assert 5* romano1 == RomanNumber(50)