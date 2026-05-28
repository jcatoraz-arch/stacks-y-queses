class Stack:

    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def invertir_lista(lista):

    stack = Stack()

    # apilar elementos
    for elemento in lista:
        stack.push(elemento)

    # reescribir lista al reves
    for i in range(len(lista)):
        lista[i] = stack.pop()

    return lista


numeros = [1, 2, 3, 4, 5]

print("Lista original:", numeros)

invertida = invertir_lista(numeros)

print("Lista invertida:", invertida)