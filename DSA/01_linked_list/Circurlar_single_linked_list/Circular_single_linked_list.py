
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None



class CircularSingleLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if self.head == self.tail:
                break


    def createSLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.next = node
        return "The CSLL has been created"
    
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The Head reference is None"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp = self.head
                index = 0
                while index < location -1:
                    temp = temp.next
                    index += 1
                next_node = temp.next
                temp.next = new_node
                new_node.next = next_node
            return "The node has been succesfully inserted"
        
    def traversal(self):
        if self.head is None:
            print("there is not any element for traversal")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp == self.tail.next:
                    break

    def searchCSLL(self, value):
        if self.head is None:
            return "There is not any node in the this CSLL"
        else:
            temp = self.head
            while temp:
                print(temp.value)
                if temp.value == value:
                    return temp.value
                temp = temp.next
                # if temp == self.tail.next:
                #     return "There node does not exits in the CSLL"
        



CSLL = CircularSingleLinkedList()
CSLL.createSLL(1)
CSLL.createSLL(2)
CSLL.createSLL(3)
CSLL.createSLL(4)
CSLL.createSLL(5)
# CSLL.insertCSLL(0, 1)
# CSLL.insertCSLL(1, 2)
# CSLL.insertCSLL(3, 3)
# CSLL.insertCSLL(4, 4)
# CSLL.insertCSLL(5, 5)

CSLL.traversal()

print(CSLL.searchCSLL(5))


# print([node.value for node in CSLL])


