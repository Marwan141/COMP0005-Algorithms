class KeyIndexCounting:
    def __init__(self, a) -> None:
        N = len(a)
        count = [0 for i in range(0,len(a))]
        for i in range(N):
            count[list[i] + 1] += 1
        for r in range(0,R):
            count[r+1] += count[r]
        for i in range(N):
            aux[count[a[i]]] = a[i]
            count[a[i]] += 1
        for i in range(N):
            a[i] = aux[i]

        
class LSDSort:
    def __init__(self,a) -> None:
        N = len(a)
        W = len(a[0])
        
        for d in range(W-1, -1, -1): #In pseudo would be up to 0
            count = [0 for i in range(0,len(a[W]))]
            for i in range(0,N):
                count[a[i][d]+1] += 1
            for r in range(0,R):
                count[r+1] += count[r]
            for i in range(0,N):
                aux[count[a[i][d]]] = a[i]
            for i in range(0,N):
                a[i] = aux[i]

class MSDSort:
    def MSDsort(a,aux,lo,hi,d):
        if (hi<=lo):
            return
        count = [0 for _ in range(R+2)]
        for r in range(0,R+1):
            count[r+1] += count[r]
        for i in range(lo,hi):
            aux[count[a[i][d] + 1]] = a[i]
            count[a[i][d]+1] += 1
        for i in range(lo,hi):
            a[i] = aux[i-lo]
        for r in range(0,R):
            MSDSort(a,aux,lo+count[r],lo+count[r+1] -1, d+1)

 


            


            