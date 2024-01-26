# creating a linked list
# nodes containing values that point to other nodes
# head value and tail value to point at starting and ending points


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None # not pointing to anything
        

class Linked_list:

    def __init__(self):
        self.head = None # empty linked list
        #self.tail = None


    def insert_at_head(self, val):
         new_node = Node(val)
        #current_node = self.head
         if self.head is None:
            self.head = new_node
            return
         else:
            new_node.next = self.head # before adjusting head index
            self.head = new_node # bring head to the front of the list
       

    def insert_at_tail(self, val):
        new_node = Node(val)
        current_node = self.head

        if self.head is None:
            self.head = new_node
        else:
            while(current_node.next):
                current_node = current_node.next #traverses the list
            current_node.next = new_node

    def delete_at_head(self):
        current_node = self.head

        if self.head is None:
            print("The list is empty")
        else:
            self.head = current_node.next
            current_node.next = None

    def delete_at_tail(self):
        current_node = self.head

        if self.head is None:
            print("The list in empty")

        else:
            while(current_node.next.next):
                current_node = current_node.next
            current_node.next = None


    def insert_at_index(self, index, val):
        new_node = Node(val)
        current_node = self.head
        position = 0

        if index == position:
            self.insert_at_head(val)
        
        else:
            # position + 1 since adding a node in
            while current_node != None and index != position + 1:
                position += 1
                current_node = current_node.next
            
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node

            else:
                print("Index is not within range")
        

    def delete_at_index(self, index):
        current_node = self.head
        position = 0

        if index == position:
            self.delete_at_head()
        else:
            while current_node != None and index != position + 1:
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("index is out of range")

        
    def update_node_val(self, index, new_val):
        position = 0
        current_node = self.head
        
        if index == position:
            current_node.val = new_val
        else:
            # no pos + 1 since there is no new nodes added
            while current_node != None and index != position:
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.val = new_val
            else:
                print("the index is out of range")


    def print_ll(self):
        current_node = self.head

        while(current_node):
            print(current_node.val)
            current_node = current_node.next

    def len_ll(self):
        length = 0 
        current_node = self.head
        
        if current_node is None:
            print("There is no linked list")
        else:
            while(current_node):
                length += 1
                current_node = current_node.next
            print("The length of the linked list is: " + str(length))

#TESTS
ll = Linked_list()

ll.insert_at_head(2)
ll.insert_at_head('a')

ll.insert_at_tail(3)
ll.insert_at_tail('b')
ll.insert_at_tail(4)

ll.delete_at_tail()

ll.delete_at_head()

ll.insert_at_index(2, 'a1')

ll.delete_at_index(2)

ll.update_node_val(2,'update')

ll.print_ll()
ll.len_ll()