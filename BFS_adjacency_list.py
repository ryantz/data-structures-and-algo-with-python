# perform DFS on an adjacency list
# one visited list and a q 
# visit node, add in q and visited
# pop from q, if is destination, return true
# is the node reachable from the source. is there a path

# create the graph
from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addedge(self, u, v):
        self.graph[u].append(v)

    def isreachable(self, source, destination):
        #introduce the 2 ds: q and visited
        visited = [False]*(self.V)#fill with false, the number of vertices
        q = []
        # add source vertix to the q and visited(root node)
        q.append(source)
        visited[source] = True

        #loop until it stops
        while q:
            out = q.pop(0)
            #print(out, end=" ")

            if out == destination:
                return True
            
            # explore children in node popped
            for children in self.graph[out]:
                if visited[children] == False:
                    q.append(children)
                    visited[children] = True

        # if not reachable, return false
        return False
    

g = Graph(4)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
print(g.graph)

u = 1; v = 3

if g.isreachable(u,v) == True:
    print("There is a path from %d to %d" % (u,v))
else:
    print("There is no path")

