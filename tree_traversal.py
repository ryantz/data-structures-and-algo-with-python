# trying to implement a simple tree traversal
# inorder, preorder, postorder

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def preorder(root_node):
    if root_node is None:
        return
    else:
        print(root_node.val, end = ", ")
        preorder(root_node.left)
        preorder(root_node.right)

def inorder(root_node):
    if root_node is None:
        return
    else:
        inorder(root_node.left)
        print(root_node.val, end = ", ")
        inorder(root_node.right)

def postorder(root_node):
    if root_node is None:
        return
    else:
        postorder(root_node.left)
        postorder(root_node.right)
        print(root_node.val, end = ", ")



# building the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

#TESTS
#preorder(root)
#inorder(root)
postorder(root)
