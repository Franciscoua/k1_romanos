from romannumbers_clase import*
class RomanNumberError(Exception):
    pass

class RomanNumber:
    def __init__(self, entrada):
        if type(entrada) == int:
            self._numero = entrada
            self._simbolo = entero_a_romano(entrada)
        elif type(entrada) == str:
            self._numero = romano_a_entero(entrada)
            self._simbolo = entrada
        else:
            raise RomanNumber("Debe inicializarse con un entero o romano valido")

    def __add__(self, otro_numero):
        resultado = self.numero + otro_numero.numero
        if resultado <0:
            raise RomanNumberError("No existen los números negativos en romano")
        return RomanNumber(resultado)

    def __sub__(self, otro_numero):
        resultado = self.numero - otro_numero.numero
        if resultado <0:
            raise RomanNumberError("No existen los números negativos en romano")
        return RomanNumber(resultado)

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, entrada):
        self._numero = entrada
        self._simbolo = entero_a_romano(entrada)

    @property
    def simbolo(self):
        return self._simbolo

    @simbolo.setter
    def simbolo(self, entrada):
        self._simbolo = entrada
        self.numero = romano_a_entero(entrada)

    """
    metodos mágicos para lógica
    """
    
    def __eq__(self, other):
        return self.numero == other.numero
    
    """
    metodo mágico para aritmética
    """

    def __mul__(self, otro):
        if  not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)

        resultado = self.numero * otro.numero

        return RomanNumber(resultado)
    
    def __rmul__(self, otro):
        return self.__mul__(otro)
    
    """
    metodo mágico para representación
    """

    def __repr__(self):
        return f"{self.numero}-{self.simbolo}"
    
    def __str__(self):
        return self.__repr__()
        
