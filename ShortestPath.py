class Dijkstras:
    #O(ElogV)
    def __init__(self, G,S) -> None:
        self.edgeTo = [None for v in range(0, G.V())]
        self.distTo = [-1 for v in range(0,G.V())]
        self.distTo[S] = 0
        self.pq = MinPQ()
        self.pq.insert(s,0)
        while(not self.pq.isEmpty()):
            v = self.pq.delMin()
            for e in G.adj(v):
                self.relax(e)

    def relax(self,e):
        v = e.endPoint()
        w = e.otherEndPoint()
        if self.distTo[w] > self.distTo[v] + e.weight:
            self.distTo[w] = self.distTo[v] + e.weight
            self.distTo[w] = e
            if self.pq.contains(w):
                self.pq.decreaseKey(w,self.distTo[w])
            else:
                self.pq.insert(w,self.distTo[w])

class DAG:
    def __init__(self,G) -> None:
        self.marked = [False for v in range(0,G.V())]
        self.reverseOrder = Stack()
        for v in range(G.V()):
            if not self.marked[v]:
                self.dfs(G,v)
                self.reverseOrder.push(v)
        
    def dfs(self,G, S):
        self.marked[S] = True
        for v in G.adj(S):
            if not self.marked[v]:
                self.dfs(G,v)
                self.reverseOrder.push(v)


class EdgeWeightedDAG:
    #Compute Topological Order
    #Add Vertex to the SPT and relax all outgoing edges
    #O(E+V)
    def __init__(self, G,V) -> None:
        self.edgeTo = [None for v in range(0,G.V())]
        self.distTo = [float('inf') for v in range(0,G.V())]
        self.distTo[V] = 0
        self.reverseOrder = DAG(G).reverseOrder
        self.topo = self.reverseOrder.reverse()
        
        while (not self.topo.isEmpty()):
            current = self.topo.pop()
            for e in G.adj(current):
                self.relax(e)
    def relax(self, e):
        v = e.endPoint()
        w = e.otherEndPoint(v)
        if self.distTo[w] > self.distTo[v] + e.weight():
            self.distTo[w] = self.distTo[v] + e.weight
        

class BellmanFord:
    #O(EV)
    #Can be reduced to O(E+V) with a queue implementation
    def __init__(self,G,V) -> None:
        self.distTo = [float('inf') for v in range(0,G.V())]
        self.distTo[V] = 0
        for v in range(0,G.V()):
            for i in range(0,G.V()):
                for w in G.adj(i):
                    self.relax(w)

    def relax(self, e):
        v = e.endPoint()
        w = e.otherEndPoint(v)
        if self.distTo[w] > self.distTo[v] + e.weight():
            self.distTo[w] = self.distTo[v] + e.weight
        