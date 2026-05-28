def anidada(cadena):

    stack = []

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caracter in cadena:

        # si es apertura
        if caracter in "([{":
            stack.append(caracter)

        # si es cierre
        else:

            # stack vacio
            if len(stack) == 0:
                return 0

            # verificar coincidencia
            ultimo = stack.pop()

            if ultimo != pares[caracter]:
                return 0

    # si quedaron aperturas sin cerrar
    if len(stack) != 0:
        return 0

    return 1


print(anidada("()"))
print(anidada("([{}])"))
print(anidada("(]"))
print(anidada("({[)]}"))
print(anidada(""))