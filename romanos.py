
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# 1137 ----> MCXXXVII
# |||| _______________ VII ----- 7 * 10 ELEVADO A 0
# ||| ________________ XXX ----- 3 * 10 ELEVADO A 1
# || _________________ C ------- 1 * 10 ELEVADO A 2
# | __________________ m ------- 1 * 10 ELEVADO A 3
# 1M 1C 3D 7U
# 1137 / 1000 = 1
# 1137 % 1000 = 137 
# 
# 137 / 100 = 1
# 137 % 100 = 37

# 37 / 10 = 3
# 37 % 10 = 1

# 7 / 1 = 7
# 7 % 1 = 0




def num_romano(numero):
    # if type(numero) != int:
    if not isinstance(numero, int):
        return f"Error: debes introducir un numero entero ({numero})"
    if not (0 < numero < 4000):
        return f"Error: el numero debe ser entre 0 y 3999({numero})"
    millares = ["", "M", "MM", "MMM"]
    centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    decenas =  ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    millar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    resto = resto % 100
    decena = resto // 10
    resto = resto % 10
    unidad = resto
    
    # DESCOMPOSICION EN MILLARES, CENTENAS, DECENAS Y UNIDADES
    # MAPEAR EL COSCIENTE(DICCIONARIO)
    romano = millares[millar] + centenas[centena] + decenas[decena] + unidades[unidad]
    # SI HAY RESTO REPETIMOS
    
    return romano

print(num_romano(56))
print(num_romano(56.1))
print(num_romano("lo que quiera"))
print(num_romano([]))
print(num_romano({}))
print(num_romano(0))
print(num_romano(4000))
print(num_romano(1))
print(num_romano(3999))

# if not isinstamce(numero, int):
#       return f"Error": debes introducir un numero entero ({numero})
#  return "TODO: convertir a romano"
