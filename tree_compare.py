# implementing a tree comparison
# base cases for recursion
# if a and b are null, equal
# if a is null but b is not, not equal
# if the values in a and b are not the same

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def compare(tree1, tree2):

    # structural checks
    if tree1 is None and tree2 is None:
        return True
    
    if tree1 is None or tree2 is None:
        return False

    # node value check
    if tree1.val != tree2.val:
        return False
    
    # compare the left side if true and right side if true
    # if one side is false, it will result in the && operation being false
    # thus the whole tree will return false
    return compare(tree1.left, tree2.left) and compare(tree1.right, tree2.right)



# create trees for comparison
a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)

b = Node(1)
b.left = Node(2)
b.right = Node(3)
b.left.left = Node(4)
b.left.right = Node(5)

c = Node(1)
c.left = Node(2)
c.right = Node(3)
c.left.left = Node(4)

print(compare(a,b)) # should return true
print(compare(a,c)) # should return false