stack = []

# Push
stack.append("Matematica")
stack.append("Lengua")
stack.append("Historia")

print("Stack actual:", stack)

# Pop
print("Elemento eliminado:", stack.pop())

# Peek
print("Ultimo elemento:", stack[-1])

# IsEmpty
print("Esta vacio:", len(stack) == 0)

# Size
print("Cantidad de elementos:", len(stack))


queue = []

# Enqueue
queue.append("Matematica")
queue.append("Lengua")
queue.append("Historia")

print("Queue actual:", queue)

# Dequeue
print("Elemento eliminado:", queue.pop(0))

print("Queue actual:", queue)



class Stack:

    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        return "La stack esta vacia"

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        return "La stack esta vacia"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def mostrar(self):
        return self.items


pila = Stack()

pila.push(1)
pila.push(2)
pila.push(3)

print("Stack:", pila.mostrar())
print("Pop:", pila.pop())
print("Peek:", pila.peek())
print("Esta vacia:", pila.is_empty())
print("Size:", pila.size())


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, valor):
        self.items.append(valor)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        return "La queue esta vacia"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def mostrar(self):
        return self.items


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.mostrar())
print("Dequeue:", queue.dequeue())
print("Cola actual:", queue.mostrar())
print("Esta vacia:", queue.is_empty())
print("Size:", queue.size())