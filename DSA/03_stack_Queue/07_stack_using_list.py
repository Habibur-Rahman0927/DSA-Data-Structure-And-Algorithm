# stack implementation is easy, if we use list, but it's not efficent and when it's big performance is not good


class Stack:
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self) -> bool:
        if self.list == []:
            return True
        else:
            return False

    # isFull
    def isFull(self) -> bool:
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    # push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1]
    
    # delete
    def delete(self):
        self.list = None


stack = Stack(4)
print(stack.isEmpty())
print(stack.isFull())
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.peek()
print(stack)
