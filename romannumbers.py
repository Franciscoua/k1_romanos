class RomanNumberError(Exception):
    pass

def entero_a_romano(n_int):
    if n_int < 1:
        return ""

    simbolos_valores_superiores = {
        4000000: "(IV)",
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
    resultado = entero_a_romano(4000000)
    print(resultado)






"""        
La ventaja del código es la simpleza (quiero decir, el algoritmo con los dos fors). La desventaja es que has aumentado el límite de 4000 a 4000000 pero el 
problema es el mismo. Si lograras, con esta filosofía, hacer un formato comun y escalable seria genial.
Así a bote pronto date cuenta que lo que cambian de valores inveriores a valores superiores es que multiplicas por mil las claves. Ahí hay un hilo del que tirar
"""
