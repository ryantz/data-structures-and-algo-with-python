# trying to implement a heap in python
# heap is basically an array
# values are inserted left to right
# always a full tree
# left node from parent 2i + 1
# right node from parent 2i + 2
# child to parent i-1/2
# insert at the end, bubble up while comparing
# delete, bubble largest value up, heapyfy down
# heapify up: compare the value with parent and swap if smaller than parent
# heapify down: check which side of the tree is shorter, go to the shorter side, compare if bigger

class Minheap():
    def __init__(self):
        # store data into an array and record index of the length of the array        
        self.data = []
        self.length = 0

    # obtaining the index of different nodes
    def parent(self, idx):
        p = (idx - 1)//2
        return p
    
    def leftchild(self, idx):
        lc = 2 * idx + 1
        return lc
    
    def rightchild(self, idx):
        rc = 2 * idx + 2
        return rc
    
    def heapifyup(self, idx):
        currV = self.data[idx]
        parent = self.parent(idx)
        parentV = self.data[parent]

        if idx == 0: # there is only 1 element, nothing to heapify up with
            return
        
        if currV < parentV:
            # swap current and parent position
            self.data[idx] = parentV
            self.data[parent] = currV
            self.heapifyup(parent)
       

    def heapifydown(self, idx):
        rIdx = self.rightchild(idx)
        lIdx = self.leftchild(idx)
    
        if idx >= self.length or lIdx >= self.length: # at the bottom or larger than the tree, nothing to heapify down
            return
        
        rVal = self.data[rIdx]
        lVal = self.data[lIdx]
        currVal = self.data[idx]

        # top node in minheap has to be the smallest.
        # find the smallest child node 
        if (lVal > rVal and currVal > rVal):
            # swap places with right child
            temp = self.data[idx]
            self.data[idx] = self.data[rIdx]
            self.data[rIdx] = temp
            self.heapifydown(rIdx)

        if (rVal > lVal and currVal > lVal):

            temp = self.data[idx]
            self.data[idx] = self.data[lIdx]
            self.data[lIdx] = temp
            self.heapifydown(lIdx)

    def insert(self,val):
        # insert data at the bottom of the tree, heapify up
        self.data.append(val)
        self.heapifyup(self.length)
        self.length += 1
        

    def delete(self):
        # delete data by swapping with first element of the tree and heapifying down
        if self.length == 0: # no elements in the heap
            return -1
        
        if self.length == 1:
            out = self.data[0]
            self.data = []
            self.length -= 1

        else:
            self.length -= 1
            self.data[0] = self.data[self.length] # swap values of first element and last
            self.data.pop(self.length) # remove the value of last in the array
            self.heapifydown(0)


       

#TESTS
mh = Minheap()

mh.insert(1)
'''
mh.insert(2)
mh.insert(3)
mh.insert(4)
mh.insert(5)
mh.insert(6)
'''
mh.delete()

print(mh.length)
print(len(mh.data))
print(mh.data)
