class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def isEmpty(self):
        if self.top == None and self.height == 0:
            # print("Stack is Empty")
            return True
        else:
            return False

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.isEmpty():
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.top.value
        
    def delete(self):
        self.top = None
        self.height = 0
    

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), '\n')

my_stack.isEmpty()

print(my_stack.peek(), '\n')

# my_stack.delete()

my_stack.print_stack()
