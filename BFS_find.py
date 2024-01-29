# trying to implement a bfs search on a tree
# left side of the tree is <=
# right side of the tree is >

# creating the Tree

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def search(tree, target):
    
    if tree is None: # if there is no tree
        return False
    
    if tree.val == target: # if the value is the target
        return True
    
    
    if tree.val < target: # traverse to the right
        return search(tree.right, target)
        
    else: # traverse to the left  
        return search(tree.left, target)


# create the tree
tree = Node(5)
tree.left = Node(3)
tree.right = Node(7)
tree.left.left = Node(2)
tree.left.right = Node(4)
tree.right.left = Node(6)
tree.right.right = Node(8)

# TESTS
needle1 = 8
needle2 = 200
print(search(tree, needle1))
print(search(tree, needle2))