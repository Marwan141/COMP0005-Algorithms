class DiGraph:
    def __init__(self, V) -> None:
        self.V = V
        self.adj = []
        for _ in range(0,self.V):
            self.adj.append(Bag()) 

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def adj(self,v):
        return self.adj[v]
    
#Exactly the same algo as non-directional
class DFS:
    def __init__(self,G,S) -> None:
        self.marked = [False for v in range(0,G.V())]
        self.edgeTo = [-1 for v in range(0,G.V())]
        self.dfs(G,S)

    def dfs(self, G, S):
        self.marked[S] = True
        for v in G.adj(S):
            if not self.marked[v]:
                self.edgeTo[v] =S
                self.dfs(G,v)

#Exactly the same algo as non-directional
class BFS:
    def __init__(self,G,S) -> None:
        self.distTo = [-1 for v in range(0,G.V())]
        self.edgeTo = [-1 for v in range(0,G.V())]
        self.bfs(G,S)

    def bfs(self,G,S):
        q = Queue()
        q.enqueue(S)
        self.distTo[S] = 0
        while(not(q.isEmpty())):
            v = q.dequeue()
            for w in G.adj(v):
                if (self.distTo[w] == -1):
                    q.enqueue(w)
                    self.distTo[w] = self.distTo[w] + 1
                    self.edgeTo[w] = v

#Compute the topological order using 
class DepthFirstOrder:
    def __init__(self,G) -> None:
        self.marked = [False for v in range(0,G.V())]
        self.reversePost = Stack()
        for v in range(0,G.V()):
            if not self.marked[v]:
                self.dfs(G,v)
                

    def dfs(self, G,V):
        self.marked[V] = True
        for w in G.adj(V):
            if not self.marked[w]:
                self.dfs(G,w)
        self.reversePost.push(V)

#Check there are no cycles in the graph          
class DirectedGraph:
    def __init__(self,G) -> None:
        self.marked = [False for v in range(0,G.V())]
        self.OnStack = []
        self.hasCycle = False
        for v in range(0,G.V()):
            if not self.marked[v]:
                self.dfs(G,v)

    def dfs(self, G,V):
        self.marked[V] = True
        self.OnStack.append(V)
        for w in G.adj(V):
            if self.hasCycle:
                return
            if w in self.OnStack:
                self.hasCycle = True
            if not self.marked[w]:
                self.dfs(G,w)
        self.OnStack.remove(V)

class StronglyConnectedComponent:
    #V and W are strongly connected if there is both a directed path from v to w and viceversa.
    #First compute DAG of reverse of G
    #DFS on the DAG
    def __init__(self,G) -> None:
        self.marked = [False for v in range(0,G.V())]
        self.scc = [-1 for v in range(0,G.V())]
        self.count = 0
        dfsOrder = DepthFirstOrder(G.reverse())
        reverseOrder = dfsOrder.reversePost()
        while (not reverseOrder.isEmpty()):
            v = reverseOrder.pop()
            if not self.marked[v]:
                self.scc[v] = self.count
                self.dfs(G,v)
            self.count += 1 

    def dfs(self, G,V):
        self.marked[V] = True
        for w in G.adj(V):
            if not self.marked[w]:
                self.scc[w] = self.count
                self.dfs(G,w)
            
