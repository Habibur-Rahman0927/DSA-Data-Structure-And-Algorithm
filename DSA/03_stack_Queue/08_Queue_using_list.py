# Queue using list


class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        else:
            values = [str(x) for x in self.items]
            return '\n'.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[0]
        
    def delete(self):
        self.items = []
        

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue(), '\n')

queue.delete()

print(queue)