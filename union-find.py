class EagerApproach:

    def __init__(self, n):
        self.id = []
        self.N = n
        for i in range(n):
            self.id.append(i)
            
        
    def union(self,u,v):
        uid = self.id[u]
        vid = self.id[v]
        for i in range(self.N):
            if self.id[i] == uid:
                self.id[i] = vid
        
    def find(self, u,v):
        return self.id[u] == self.id[v]
    


class LazyApproach:
    def __init__(self, n):
        self.id = []
        self.N = n
        for i in range(n):
            self.id.append(i)

    def root(self,u):
        if self.id[u] == u:
            return u
        else:
            self.root(self.id[u])

    def union(self, u, v):
        r_u = self.root(u)
        r_v = self.root(v)
        self.id[r_u] = self.id[r_v]

    def find(self,u,v):
        return self.root(u) == self.root(v)
    

class ImprovedLazyApproach:
    def __init__(self, n):
        self.id = []
        self.size = []
        self.N = n
        for i in range(n):
            self.id.append(i)
            self.size.append(1)

    def root(self,u):
        if self.id[u] == u:
            return u
        else:
            self.root(self.id[u])

    def union(self, u, v):
        r_u = self.root(u)
        r_v = self.root(v)
        if self.id[r_u] == self.id[r_v]:
            return
        if self.size[r_u] < self.size[r_v]:
            self.id[r_u] = self.id[r_v]
            self.size[r_v] += self.size[r_u]
        else:
        
            self.id[r_v] = self.id[r_u]
            self.size[r_u] += self.size[r_v]

