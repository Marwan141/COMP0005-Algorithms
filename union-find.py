class EagerApproach:
    #uses one list initiliased to each index, later will store the root.
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
    #uses trees, so root will have the same root as it's own value.
    def __init__(self, n):
        self.id = []
        self.N = n
        for i in range(n):
            self.id.append(i)

    def root(self,u):
        if self.id[u] == u:
            return u
        else:
            return self.root(self.id[u])

    def union(self, u, v):
        r_u = self.root(u)
        r_v = self.root(v)
        self.id[r_u] = self.id[r_v]

    def find(self,u,v):
        return self.root(u) == self.root(v)
    

class ImprovedLazyApproach:
    #Same here but maximases performance for union operations by minimising the amount of comparisons, as root will be the smaller tree.
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
            return self.root(self.id[u])

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

