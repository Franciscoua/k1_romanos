def entero_a_romano(n_int):
    if n_int < 1:
        return ""

    simbolos_valores_superiores = {
        4000000: "((IV))",
        1000000: "M",
        900000: "CM",
        500000: "D",
        400000: "CD",
        100000: "C",
        90000: "XC",
        50000: "L",
        40000: "XL",
        10000: "X",
        9000: "IX",
        5000: "V",
        4000: "IV",
        1000: "I"
    }

    simbolos_valores_inferiores = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    resultado_vs = ""
    resultado_vi = ""

    if n_int >= 4000:
        for valor, simbolo in simbolos_valores_superiores.items():
            while n_int >= valor:
                n_int -= valor
                resultado_vs += simbolo

    for valor, simbolo in simbolos_valores_inferiores.items():
        while n_int >= valor:
            n_int -= valor
            resultado_vi += simbolo

    if resultado_vs:
        resultado_vs = f"({resultado_vs})"

    resultado = resultado_vs + resultado_vi

    return resultado

if __name__ == "__main__":
    resultado = entero_a_romano(45)
    print(resultado)






"""        
    if n_int in simbolos:
        return simbolos[n_int]
    
    if n_int < 4:
        return n_int * simbolos[1]
    elif n_int == 4:
        
        return simbolos[1] + simbolos[5]
    else:
        multiplicador = n_int -5
        return simbolos[5] + multiplicador * simbolos[1]
"""
