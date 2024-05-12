class Heap:
    def __init__(self):
        self.a = [None]
        self.N = 0

    def enqueue(self, key):
        self.N += 1
        self.a.append(key)
        self.swim(self.N)

    def swim(self,i):
        while (i>1 and self.a[i/2]<self.a[i]):
            temp = self.a[i/2]
            self.a[i/2] = self.a[i]
            self.a[i] = temp
            i = i//2

    def delete(self):
        temp = self.a[self.N]
        self.a[self.N] = self.a[1]
        self.a[1] = temp
        self.a[self.N] = None
        self.N -= 1
        self.sink(1)
    
    def sink(self, i):
        while 2*i <= self.N:
            j = 2*i
            if j < self.N and self.a[j] < self.a[j+1]:
                j += 1
            if not self.a[i] < self.a[j]:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
            i = j


            