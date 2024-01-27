# trying to implement a stack in python
# something like a queue but removing is opposite
# add and remove from the head (push, pop)
# like a stack of pancakes

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    
    def push(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        current_node = self.head

        if self.head is None:
            print("There is no stack implemented")
            return
        else:
            self.head = current_node.next
            current_node.next = None

    def printstk(self):
        current_node = self.head
        
        if self.head is None:
            print("There is no stack!")
            return
        else:
            while current_node:
                print(current_node.val)
                current_node = current_node.next

stk = Stack()

stk.push(1)
stk.push('a')
stk.push(3)
stk.push('b')

stk.pop()

stk.printstk()