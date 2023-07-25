


def romano_a_entero(romano):

    digitos_romanos = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    valores = [1, 5, 10, 50, 100, 500, 1000]
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
        return 'ERROR: tiene que ser un numero romano en formato cadena de texto'
    
    
  

    resultado = 0
    anterior = 0
    for letra in romano:
        if letra not in digitos_romanos:
            return f'ERROR: {letra} no es un digito romano válido'
        


        actual = digitos_romanos[letra]

        if anterior < actual: 
            #Comprobar que la resta es posible
            #el orden de magnitud  no es mayor de uno
            if anterior < 0 and len(str(actual)) > len (str(anterior)) > 1:
                return 'ERROR: resta no posible'
            #deshacer la suma que hemos hecho antes
            resultado = resultado - anterior
            #sumar el valor actual, pero restando el anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + actual


        anterior = actual
    return resultado

errores = ['A', '', 3, ['X', 'X', 'I']]
pruebas = [ 'I', 'MCXXIII', 'VIII', 'LVI', 'IV', 'DCIV']
for valor in pruebas:
    print(romano_a_entero(valor))

