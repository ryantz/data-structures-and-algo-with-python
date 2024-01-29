# trying to create a BFS traversal by hand
# needs to have a visited and a queue

# creating the tree
tree = {'1': ['2','3'], 
        '2': ['4','5'], 
        '3': ['6','7'],
        '4': [], 
        '5': [], 
        '6': [], 
        '7': []
        }

# create queues for visited and unvisited
v = []
q = []

def bfs(v, tree, node):
    v.append(node) # v = [1..2..3]
    q.append(node) # q = [1...2,3...4,5...6,7]

    while q:
        curr = q.pop(0) # remove first element
        print(curr, end = " ") # [1]

        for children in tree[curr]: # [1: 2, 3]
            if children not in v:
                q.append(children) # put children into the queue
                v.append(children)


bfs(v, tree, '1')

    


