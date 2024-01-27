# trying to implement a queue in python
# like a human queue, add from the back of the line
# enqueue adds nodes at the back of the LL
# dequeue removes nodes at the front of the LL

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None #new node point at nothing

class Queue:
    def __init__(self):
        self.head = None
        #self.tail = None

    
    def enQ(self, val):
        new_node = Node(val)
        current_node = self.head

        if self.head is None:
            self.head = new_node
            return
        else:
            while current_node.next:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def dQ(self):
        current_node = self.head

        if current_node is None:
            print("Error there is no queue implemented")
            return
        else:
            self.head = current_node.next # why does this not work if current_node = current_node.next
            current_node.next = None
            

    def printQ(self):
        current_node = self.head

        if current_node is None:
            print("There is no Queue!")
            return
        else:
            while current_node:
                print(current_node.val)
                current_node = current_node.next
                


#TESTS

kew = Queue()

kew.enQ(20)
kew.enQ('a')
kew.enQ('B')
kew.enQ(2)

kew.dQ() 

kew.printQ() 
