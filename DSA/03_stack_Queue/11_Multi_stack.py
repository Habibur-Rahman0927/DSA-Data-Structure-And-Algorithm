
# Use a single list to implement there stack

class MultiStack:
    def __init__(self, stacksize) -> None:
        self.numberstacks = 3
        self.cusList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def display(self):
        # it's for understand
        print(self.numberstacks)
        print(self.stacksize * self.numberstacks)
        print(self.cusList)
        print(self.sizes)
        print(self.stacksize)

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.cusList[self.indexOfTop(stacknum)] = item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.cusList[self.indexOfTop(stacknum)]
            self.cusList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.cusList[self.indexOfTop(stacknum)]
            return value

    





multi_stack = MultiStack(6)

multi_stack.display()

print(multi_stack.isFull(0))
print(multi_stack.isEmpty(0))
print(multi_stack)