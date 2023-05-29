"""from romannumbers_calase import romano_a_entero, RomanNumberError
import pytest

def test_simbolos():    
    assert romano_a_entero("I")==1
    assert romano_a_entero("L")==50

def test_sumando():
    assert romano_a_entero("CXXIII") == 123


def test_resta_normal():
    assert romano_a_entero("IV") == 4
    assert romano_a_entero("IX") == 9

def test_composicion_numero():
    assert romano_a_entero("MMCMXLIX") == 2949

def test_de_no_mas_de_tres_repeticiones():
    with pytest.raises(RomanNumberError):
        romano_a_entero("CCCC")

def test_de_no_repetir_VLD():
    with pytest.raises(RomanNumberError):
        romano_a_entero("VV")  
    with pytest.raises(RomanNumberError):
        romano_a_entero("LL")
    with pytest.raises(RomanNumberError):
        romano_a_entero("DD")  

def test_restas_permitidas():
    with pytest.raises(RomanNumberError):
        romano_a_entero("IC")
    with pytest.raises(RomanNumberError):
        romano_a_entero("IL")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XD")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XM")
    with pytest.raises(RomanNumberError):
        romano_a_entero("VL")
    with pytest.raises(RomanNumberError):
        romano_a_entero("LM")

def test_no_resta_multiplos_5():   
    with pytest.raises(RomanNumberError):
        romano_a_entero("VX")
    with pytest.raises(RomanNumberError):
        romano_a_entero("LC")
    with pytest.raises(RomanNumberError):
        romano_a_entero("DM")

def test_no_repeticion_de_restas():
    with pytest.raises(RomanNumberError):
        romano_a_entero("IIX")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XM")
    with pytest.raises(RomanNumberError):
        romano_a_entero("XM")
    with pytest.raises(RomanNumberError):
        romano_a_entero("IVX")


    with pytest.raises(RomanNumberError):
        romano_a_entero("IIX") 
    with pytest.raises(RomanNumberError):
        romano_a_entero("IVIX")
    with pytest.raises(RomanNumberError):
        romano_a_entero("VIX")

def test_random():
    romano_a_entero("MCMXCIX") == 1999



def test_suma():
    romano1 = RomanNumber(10)
    romano2 = RomanNumber(5)
    resultado = romano1 + romano2
    assert resultado.numero == 15
    assert resultado.simbolo == "XV"

    romano1 = RomanNumber("C")
    romano2 = RomanNumber(45)
    resultado = romano1 + romano2
    assert resultado.numero == 145
    assert resultado.simbolo == "CXLV"

    romano1 = RomanNumber("MM")
    romano2 = RomanNumber(5)
    resultado = romano1 + romano2
    assert resultado.numero == 2005
    assert resultado.simbolo == "MMV"

def test_resta():
    romano1 = RomanNumber(10)
    romano2 = RomanNumber(5)
    resultado = romano1 - romano2
    assert resultado.numero == 5
    assert resultado.simbolo == "V"

    romano1 = RomanNumber(10)
    romano2 = RomanNumber(10)
    resultado = romano1 - romano2
    assert resultado.numero == 0
    assert resultado.simbolo == ""

    romano1 = RomanNumber("CCLXII")
    romano2 = RomanNumber(5)
    resultado = romano1 - romano2
    assert resultado.numero == 257
    assert resultado.simbolo == "CCLVII"

def test_suma_resultado_negativo():
    romano1 = RomanNumber(5)
    romano2 = RomanNumber(-8)
    with pytest.raises(RomanNumberError):
        resultado = romano1 + romano2

def test_resta_resultado_negativo():
    romano1 = RomanNumber(10)
    romano2 = RomanNumber(15)
    with pytest.raises(RomanNumberError):
        resultado = romano1 - romano2


def test_division():
    romano1 = RomanNumber(50)
    romano2 = RomanNumber(10)
    resultado = romano1 / romano2
    assert resultado.numero == 5
    assert resultado.simbolo == "V"

    romano1 = RomanNumber(500)
    romano2 = RomanNumber("II")
    resultado = romano1 / romano2
    assert resultado.numero == 250
    assert resultado.simbolo == "CCL"

    romano1 = RomanNumber("MM")
    romano2 = RomanNumber(5)
    resultado = romano1 / romano2
    assert resultado.numero == 400
    assert resultado.simbolo == "CD"

    romano1 = RomanNumber(8)
    romano2 = RomanNumber(3)
    resultado = romano1 / romano2
    assert resultado.numero == 2
    assert resultado.simbolo == "II"

def test_multiplicacion_resultado_negativo():
    romano1 = RomanNumber(5)
    romano2 = RomanNumber(-8)
    with pytest.raises(RomanNumberError):
        resultado = romano1 * romano2

def test_division_por_cero():
    romano1 = RomanNumber(10)
    romano2 = RomanNumber(0)
    with pytest.raises(ZeroDivisionError):
        resultado = romano1 / romano2

def test_division_resultado_negativo():"""
       
