
class EdgeWeightedGraph:
    def __init__(self, V):
        self.V = V
        self.adj = []
        for _ in range (0,V):
            self.adj.append(Bag())

    def addEdge(self, e):
        v = e.endpoint()
        w = e.otherEndPoint(v)
        self.adj[v].add(e)
        self.adj[w].add(e)

    def adj (self, v):
        return self.adj[v]


class KruskalMST:
    def __init__(self, G):
        self.mst = Queue()
        self.pq = MinPQ()
        for e in G.edges():
            self.pq.insert(e)
        
        uf = UF(G.V())
        while (not self.pq.isEmpty and self.mst.size() < G.V() - 1):
            e = self.pq.delMim()
            v = e.endPoint()
            w = e.otherEndPoint(v)
            if (not uf.connected(v,w)):
                uf.union(v,w)
                self.mst.enqueue(e)
            
    def edges(self):
        return self.mst


class LazyPrimMST:
    def __init__(self,G) -> None:
        self.marked = [False for v in range(0,G.V())]
        self.mst = Queue()
        self.pq = MinPQ()
        self.visit(G,0)

        while(not self.pq.isEmpty() and self.mst.size()< G.V() - 1):
            e = self.pq.delete()
            v = e.endPoint()
            w = e.otherEndPoint(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.enqueue(e)
            if (not self.marked[v]):
                self.visit(G,v)
            if (not self.marked[w]):
                self.visit(G,w)

    def visit(self,G,V):
        self.marked[V] =True
        for e in G.adj(V):
            if (not self.marked[e.otherEndPoint(V)]):
                self.pq.insert(e)
    
    def edges(self):
        return self.mst
            