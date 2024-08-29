class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Добавляем элемент в конец списка
        self.stack.append(item)

    def pop(self):
        # Удаляем и возвращаем последний элемент списка
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        # Возвращаем последний элемент списка без удаления
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        # Проверяем, пуст ли стек
        return len(self.stack) == 0

    def size(self):
        # Возвращаем размер стека
        return len(self.stack)

# Реализация очереди с помощью списка
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Добавляем элемент в конец списка
        self.queue.append(item)

    def dequeue(self):
        # Удаляем и возвращаем первый элемент списка
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        # Возвращаем первый элемент списка без удаления
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        # Проверяем, пуста ли очередь
        return len(self.queue) == 0

    def size(self):
        # Возвращаем размер очереди
        return len(self.queue)

# Примеры использования стека
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack size:", stack.size())
print("Stack top:", stack.peek())
print("Pop from stack:", stack.pop())
print("Stack size after pop:", stack.size())

# Примеры использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())
print("Queue front:", queue.front())
print("Dequeue:", queue.dequeue())
print("Queue size after dequeue:", queue.size())