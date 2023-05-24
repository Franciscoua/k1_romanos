from romannumbers import entero_a_romano

def test_cero_es_none():
    assert entero_a_romano(0) ==""



def test_uno_es_palito():
    assert entero_a_romano(1) == "I"


def test_dos_es_palito_palito():
    assert entero_a_romano(2) == "II"

def test_tres_es_palito_palito_palito():
    assert entero_a_romano(3) == "III"

def test_cuatro_es_palito_uve():
    assert entero_a_romano(4) == "IV" 


def test_cinco_es_uve():
    assert entero_a_romano(5) == "V" 

def test_seis_es_uve_palito():
    assert entero_a_romano(6) == "VI" 

def test_siete_es_uve_palito_palito():
    assert entero_a_romano(7) == "VII"

def test_ocho_es_uve_palito_palito_palito():
    assert entero_a_romano(8) == "VIII"

def test_nueve_es_palito_equis():
    assert entero_a_romano(9) == "IX"

def test_nueve_es_palito_equis():
    assert entero_a_romano(14) == "XIV"

def test_nueve_es_palito_equis():
    assert entero_a_romano(15) == "XV"

def test_nueve_es_palito_equis():
    assert entero_a_romano(49) == "IXL"

def test_nueve_es_palito_equis():
    assert entero_a_romano(99) == "XCIX"   

def test_nueve_es_palito_equis():
    assert entero_a_romano(399) == "CCCXCIX" 

def test_cuatro_mil_es_raya_palito_uve_raya():
    assert entero_a_romano(4000) == "(IV)"

def test_siete_mil_cuatrocientos_cincuenta_y_tres_es_raya_palito_uve_raya_tres_emes_ce_de_ele_tres_I():
    assert entero_a_romano(7453) == "(IV)MMMCDLIII"

def test_siete_mil_cuatrocientos_cincuenta_y_tres_es_raya_palito_uve_raya_tres_emes_ce_de_ele_tres_I():
    assert entero_a_romano(2543280 ) == "(M)(M)(D)(XL)MMMCCLXXX"

def test_siete_mil_cuatrocientos_cincuenta_y_tres_es_raya_palito_uve_raya_tres_emes_ce_de_ele_tres_I():
    assert entero_a_romano(4000000 ) == "((IV))"


def test_siete_mil_cuatrocientos_cincuenta_y_tres_es_raya_palito_uve_raya_tres_emes_ce_de_ele_tres_I():
    assert entero_a_romano(5125) == "(V)CXXV"




def test_siete_mil_cuatrocientos_cincuenta_y_tres_es_raya_palito_uve_raya_tres_emes_ce_de_ele_tres_I():
    assert entero_a_romano(53125) == "(LIII)CXXV" # + (L)MMMCXXV

def test_siete_mil_cuatrocientos_cincuenta_y_tres_es_raya_palito_uve_raya_tres_emes_ce_de_ele_tres_I():
    assert entero_a_romano(54125) == "(LIV)CXXV"
