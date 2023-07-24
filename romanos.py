def num_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un numero entero ({numero})"
    elif type(numero) == int:
        return "TODO: convertir a romano"


print(num_romano(56))
print(num_romano(56.1))
print(num_romano("lo que quieras"))
print(num_romano([]))
print(num_romano({}))


# if not isinstamce(numero, int):
#       return f"Error": debes introducir un numero entero ({numero})
#  return "TODO: convertir a romano"
