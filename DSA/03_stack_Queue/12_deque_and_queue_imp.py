# class Dequeue:
#     def __init__(self) -> None:
#         self.items = []


#     def __str__(self):
#         if self.isEmpty():
#             return "Empty"
#         else:
#             values = [str(x) for x in self.items]
#             return '\n'.join(values)

#     def isEmpty(self):
#         if self.items == []:
#             return True
#         else:
#             return False
        
#     def enqueue(self, value):
#         return self.items.append(value)
    
    
#     def dequeue(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.items.pop(0)
    
#     def pop(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.items.pop()
        
#     def size(self):
#         return len(self.items)
    



# dequeue = Dequeue()

# print(dequeue.isEmpty())

# print(dequeue.enqueue(1))
# print(dequeue.enqueue(2))
# print(dequeue.enqueue(3))

# print(dequeue)
# print(dequeue.dequeue(), '\n')
# print(dequeue)
# print(dequeue.pop(), '\n')


class Dequeue:
    def __init__(self) -> None:
        self.items = []


    def __str__(self):
        if self.isEmpty():
            return "Empty"
        else:
            values = [str(x) for x in self.items]
            return '\n'.join(values)

    def isEmpty(self):
        return self.items == []
        
    def addFront(self, value):
        self.items.append(value)
    
    
    def addRear(self, value):
        self.items.insert(0, value)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)

dequeue = Dequeue()

dequeue.addFront(1)
dequeue.addFront(2)
dequeue.addFront(3)
dequeue.addFront(4)
dequeue.addFront(0)
print(dequeue, '\n')
dequeue.addRear(1)
dequeue.addRear(2)
dequeue.addRear(3)
print(dequeue)