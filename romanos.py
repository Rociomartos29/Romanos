class RomanNumber:

    def __init__(self, entrada):
        if isinstance(entrada, int):
            self.valor = entrada
            self.cadena = self.convertir_a_romano()

        elif isinstance(entrada, str):
            self.cadena = entrada
            self.valor = self.romano_a_entero()

        else:
            raise TypeError('Solo acepto enteros o cadenas')

    def convertir_a_romano(self):

        numero = self.valor
        if type(numero) != int:
            raise ValueError(
                "Error: debes introducir un número entero ({numero})")
    # validar el valor del número
        if not (0 < numero < 4000):
            raise ValueError(
                "Error: el número debe estar entre 1 y 3999 ({numero})")

        conversores = [
            ["", "M", "MM", "MMM"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ]
        divisores = [1000, 100, 10, 1]
        resultado = ""
        contador = 0
        for divisor in divisores:
            cociente = (numero // divisor)
            numero = numero % divisor
            resultado = resultado + conversores[contador][cociente]
            contador = contador + 1
        return resultado

    def romano_a_entero(self):
        romano = self.cadena
        digitos_romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if not isinstance(romano, str):
            raise TypeError(
                'ERROR: tiene que ser un numero romano en formato cadena de texto')

        resultado = 0
        anterior = 0
        super_anterior = 0
        for letra in romano:
            if letra not in digitos_romanos:
                raise ValueError(
                    'ERROR: {letra} no es un digito romano válido')

        actual = digitos_romanos[letra]

        if anterior < actual:
            # Comprobar que la resta es posible
            # el orden de magnitud  no es mayor de uno
            if anterior > 0 and len(str(actual)) - len(str(anterior)) > 1:
                raise ValueError(f'ERROR: resta no posible')
            if anterior > 0 and actual > super_anterior > 0:
                raise ValueError(f'ERROR: dos restas consecutivas')
        # deshacer la suma que hemos hecho antes
            resultado = resultado - anterior
        # sumar el valor actual, pero restando el anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + actual
        super_anterior = anterior
        anterior = actual

        return resultado

    def __str__(self):
        return f'Objeto: {self.cadena}'

    def __repr__(self):
        return f'Objeto: {self.cadena}'

    def __eq__(self, otro):
        return self.valor == otro or self.cadena == otro

    def __ne__(self, otro):
        if isinstance(otro, RomanNumber):
            return self.valor != otro.valor
        if isinstance(otro, int):
            return self.cadena != otro
        if isinstance(otro, str):
            return self.valor != otro
        raise ValueError(
            'Solo puedo comparar numeros romanos, enteros o cadenas')

    def __lt__(self, otro):
        if isinstance(otro, RomanNumber):
            return self.valor < otro.valor
        if isinstance(otro, int):
            return self.valor < otro
        if isinstance(otro, str):
            return self.cadena < otro
        raise ValueError('No puedo comparar si no es RomanNumber')

    def __gt__(self, otro):
        if isinstance(otro, RomanNumber):
            return self.valor < otro.valor
        if isinstance(otro, int):
            return self.valor < otro
        if isinstance(otro, str):
            return self.cadena < otro
        raise ValueError('No puedo comparar si no es RomanNumber')

    def __add__(self, otro):
        if isinstance(otro, RomanNumber):
            return self.valor + otro.valor
        if isinstance(otro, int):
            return self.valor + otro
        if isinstance(otro, str):
            return self.cadena + RomanNumber(otro).valor
        raise ValueError('Solo puedo sumar RomanNumber, cadena o entero')

    def __radd__(self, otro):
        return self.__add__(otro)

    def __sub__(self, otro):
        resta = 0
        if isinstance(otro, RomanNumber):
            resta = self.valor - otro.valor
        elif isinstance(otro, int):
            resta = self.valor - otro
        elif isinstance(otro, str):
            resta = self.cadena - RomanNumber(otro).valor
        else:
            raise ValueError('Solo sé restar RomanNumber, cadena o entero')
        if resta < 0:
            raise ValueError('Un número romano no puede ser negativo')
        else:
            return RomanNumber(resta)

    def __rsub__(self, otro):
        resta = 0
        if isinstance(otro, RomanNumber):
            resta = otro.valor - self.valor
        elif isinstance(otro, int):
            resta = otro - self.valor
        elif isinstance(otro, str):
            resta = RomanNumber(otro).valor - self.valor
        else:
            raise ValueError('Solo sé restar RomanNumber, cadena o entero')
        if resta < 0:
            raise ValueError('Un número romano no puede ser negativo')
        else:
            return RomanNumber(resta)
