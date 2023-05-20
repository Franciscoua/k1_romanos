simbolos = {
    1:"I",
    5:"V",
    10:"X"
}

def entero_a_romano(n_int):
    if n_int in simbolos:
        return simbolos[n_int]
    
    if n_int < 4:
        return n_int * simbolos[1]
    elif n_int == 4:
        
        return simbolos[1] + simbolos[5]
    else:
        multiplicador = n_int -5
        return simbolos[5] + multiplicador * simbolos[1]
    


if __name__ == "__main__":
    print(entero_a_romano(6))




"""
def entero_a_romano(n_int):
    if n_int < 1 or n_int > 3999:
        return "Número fuera de rango"
    
    # Definimos las listas con los símbolos romanos para unidades, decenas, centenas y miles
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    miles = ["", "M", "MM", "MMM"]
    
    # Convertimos el número a romano concatenando los símbolos de cada lista de acuerdo a su posición
    return miles[n_int // 1000] + centenas[(n_int % 1000) // 100] + decenas[(n_int % 100) // 10] + unidades[n_int % 10]
"""