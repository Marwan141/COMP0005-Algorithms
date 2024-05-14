class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.adj = []
        for _ in range(0,self.V):
            self.adj.append(Bag())

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def adj(self,v):
        return self.adj[v]
    

class DFS:
    def __init__(self,G,s):
        self.marked = [False for v in range(0,G.V())]
        self.edgeTo = [-1 for v in range(0,G.V())]
        self.dfs(self, G,s)

    
    def dfs(self, G,V):
        self.marked[V] =True
        for w in G.adj(V):
            if (self.marked[w] == False):
                self.dfs(G,w)
                self.edgeTo[w] = V


class BFS:
    def __init__(self,G,S):
        self.distToSource = [-1 for v in range(0,G.V())]
        self.edgeTo = [-1 for v in range(0,G.V())]
        self.bfs(G,S)

    def bfs(self,G,S):
        q = Queue()
        q.enqueue(S)
        self.distToSource[S] = 0
        while(not(q.isEmpty())):
            v = q.dequeue()
            for w in G.adj(v):
                if (self.distToSource[w] == -1):
                    q.enqueue(w)
                    self.distToSource[w] = self.distToSource[v] + 1
                    self.edgeTo[w] = v

    def shortestPathTo(self, v, s):
        if (not self.hasPathTo(v)):
            return None
        path = Stack()
        x = v
        while (x != s):
            path.push(x)
            x = self.edgeTo[x]
        path.push(s)
        return path


class ConnectedComponents:
    def __init__(self,G) -> None:
        self.marked = [False] * G.V()
        self.cc = [None for v in range(G.V())]
        self.count = 0
        for v in range(G.V()):
            if not self.marked[v]:
                self.dfs(G,v)
                self.count += 1
    
    def dfs(self,G,v):
        self.marked[v] = True
        self.cc[v] =self.count
        for w in G.adj():
            if not self.marked[w]:
                self.dfs(G,v)
    