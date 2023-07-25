
"""# I = 1
#V = 5
 X = 10
 L = 50
C = 100
D = 500
M = 1000
"""

def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un número entero ({numero})"
    # validar el valor del número
    if not (0 < numero < 4000):
        return f"Error: el número debe estar entre 1 y 3999 ({numero})"
    
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
 # DESCOMPOSICION EN MILLARES, CENTENAS, DECENAS Y UNIDADES
    # MAPEAR EL COSCIENTE(DICCIONARIO)

    # SI HAY RESTO REPETIMOS
# if not isinstamce(numero, int):
#       return f"Error": debes introducir un numero entero ({numero})
#  return "TO DO: convertir a romano"
