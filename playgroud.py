#self.marked
#self.edgeTo

def DFS(G,V):
    self.marked[V] = True
    for w in G.adj(V):
        if not self.marked[w]:
            self.dfs(G,w)
            self.edgeTo[w] = V


#self.distToSource
#self.edgeTo
def BFS(G,S):
    self.distTo = [-1 for v in range(0,G.V())]
    self.edgeTo = [None for v in range(0,G.V())]
    q = Queue()
    self.distTo[S] = 0
    q.enqueue(S)
    while(not q.isEmpty):
        v = q.dequeue()
        for w in G.adj(v):
            if self.distTo[w] == -1:
                self.edgeTo[w] = v
                q.enqueue(w)
                self.distTo[w] = self.distTo[v] + 1
            
    
class Prim:
    self.marked = [False for v in range(0,G.V())]
    self.mst = Queue()
    self.pq = MinPQ()
    visit(G,0)
    while(not pq.isEmpty and self.mst.size()<G.V() - 1):
        e = self.pq.delMin()
        v = e.endPoint()
        w = e.otherEndPoint(v)
        if self.marked[v] and self.marked[w]:
            continue
        self.mst.enqueue(e)
        if not self.marked[v]:
            visit(G,v)
        if not self.marked[w]:
            visit(G,w)

    def visit(G,W):
        self.marked[W] = True
        for e in G.adj(W):
            if not self.marked[e.otherEndPoint(W)]:
                self.pq.insert(e)


def partition(a, lo,hi):
    i = lo
    j = hi+1
    p = a[lo]
    while True:
        while(a[i] < p):
            i += 1
            if i == hi:
                break
        while (p < a[j]):
            j -= 1
            if j == lo:
                break
        if i >= j:
            break
        swap(a[i],a[j])
    swap(a[lo],a[j])
    return j

def sort(a,lo,hi):
    if hi<=lo:
        return
    j = partition(a,lo,hi)
    sort(a,lo,j-1)
    sort(a,j, hi)