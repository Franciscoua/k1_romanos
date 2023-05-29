from romannumbers_clase import *
import pytest


def test_cero_es_none():
    assert entero_a_romano(0) ==''



def test_resto_de_decenas():
    assert entero_a_romano(10) == 'X'
    assert entero_a_romano(20) == 'XX'
    assert entero_a_romano(30) == 'XXX'
    assert entero_a_romano(40) == 'XL'
    assert entero_a_romano(50) == 'L'
    assert entero_a_romano(60) == 'LX'
    assert entero_a_romano(70) == 'LXX'
    assert entero_a_romano(80) == 'LXXX'
    assert entero_a_romano(90) == 'XC'

def test_101_es_c_palito():
    assert entero_a_romano(101)== 'CI'


def test_20_es_equis_equis():
    assert entero_a_romano(20) == 'XX'

def test_numeros_rarunos():
    assert entero_a_romano(2345) == 'MMCCCXLV'
    assert entero_a_romano(3999) == 'MMMCMXCIX'

def test_4000_es_error():
    with pytest.raises(RomanNumberError):
        entero_a_romano(4000)




