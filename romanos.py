
def num_romano(numero):
    # if type(numero) != int:
    if not isinstance(numero, int):
        return f"Error: debes introducir un numero entero ({numero})"
    if not (0 < numero < 4000):
        return f"Error: el numero debe ser entre 0 y 3999({numero})"
    elif type(numero) == int:
        return "TODO: convertir a romano"


print(num_romano(56))
print(num_romano(56.1))
print(num_romano("lo que quieras"))
print(num_romano([]))
print(num_romano({}))
print(num_romano(1))
print(num_romano(3999))

# if not isinstamce(numero, int):
#       return f"Error": debes introducir un numero entero ({numero})
#  return "TODO: convertir a romano"
