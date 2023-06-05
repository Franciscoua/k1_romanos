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
        other = self.__to_roman(other)
        return self.numero == other.numero
    
    def __req__(self,other):
        return self.__eq__(other)
    
    def __lt__(self,other):
        other = self.__to_roman(other)
        return self.numero<other.numero
    
    def __le__(self,other):
        other = self.__to_roman(other)
        return self.numero<=other.numero
    
    def __gt__(self,other):
        other = self.__to_roman(other)
        return self.numero>other.numero
    
    def __ge__(self,other):
        other = self.__to_roman(other)
        return self.numero>=other.numero
    
    def __ne__(self,other):
        other = self.__to_roman(other)
        return self.numero!=other.numero
    

    
    """
    metodo mágico para aritmética

    """
    def __to_roman(self,otro):
        if not isinstance(otro,RomanNumber):
            otro = RomanNumber(otro)
        return otro

    def __mul__(self, otro):
        if  not isinstance(otro, RomanNumber):
            otro = RomanNumber(otro)

        resultado = self.numero * otro.numero

        return RomanNumber(resultado)
    
    def __rmul__(self, otro):
        return self.__mul__(otro)
    

    
    def __add__(self, otro2):
        if not isinstance(otro2, RomanNumber):
            otro2 = RomanNumber(otro2)
        resultado = self.numero + otro2.numero
        if resultado <0:
            raise RomanNumberError("No existen los números negativos en romano")
        return RomanNumber(resultado)
    
    def __radd__(self, otro2):
        return self.__add__(otro2)
    
    

    def __sub__(self, otro3):
        if not isinstance(otro3, RomanNumber):
            otro3 = RomanNumber(otro3)
            
        return RomanNumber(self.numero - otro3.numero)


    def __rsub__(self, otro):
        otro = self.__to_roman(otro)

        return otro.__sub__(self)

    
    
    def __floordiv__(self, otro4):
        if not isinstance(otro4, RomanNumber):
            otro4 = RomanNumber(otro4)
        resultado = self.numero//otro4.numero
        return RomanNumber(resultado)

    
    def __rfloordiv__(self, otro4):
        otro4 = RomanNumber(otro4) 
        return otro4.__floordiv__(self)
    
    def __pow__(self, otro):
        otro = self.__to_roman(otro)
        return RomanNumber(self.numero ** otro.numero)
    
    def __rpow__(self, otro):
        otro = self.__to_roman(otro)
        return otro.__pow__(self)
    

    """
    metodo mágico para representación
    """

    def __repr__(self):
        return f"{self.numero}-{self.simbolo}"
    
    def __str__(self):
        return self.__repr__()
        
