class BruteForce:
    def __init__(self,pattern,text) -> None:
        M = len(pattern)
        N = len(text)
        for i in range(0,N-M):
            for j in range(0,M):
                if text[i+j]!=pattern[j]:
                    break
            if j==M:
                return i
        return N
    
class Knuth:
    def __init__(self,pattern,text) -> None:
       self.M = len(pattern)
       self.DFA = [[-1 for j in range(0,M)] for v in range(0,R)]
       self.DFA[pattern[0]][0] = 1
       x = 0
       for j in range(1,self.M):
            for c in range(0,R):
               self.DFA[c][j] = self.DFA[c][x]
            self.DFA[pattern[j]][j] = j+1
            x= self.DFA[pattern[j]][x]
           
    def subStringSearch(self, inp):
        j = 0
        i = 0
        while(not inp.isEmpty() and j<M):
            j = self.DFA[inp.readChar()][j]
            i += 1
        if(j==self.M):
            return i-self.M
        else:
            return -1
    
class BoyerMoore:
    def __init__(self, pattern, text) -> None:
        self.M = len(pattern)
        self.index = [-1 for v in range(0,R)]
        for j in range(0,self.M):
            self.index[pattern[j]] = j


    def subStringSearch(self, text,pattern):
        N = len(text)
        i = 0
        while(i<N-self.M):
            skip = 0
            j = self.M-1
            while(j>=0):
                if pattern[j] != text[i+j]:
                    skip = max(1, j-self.index[text[i+j]])
                    break
                else:
                    j = j -1
        i = i + skip
        if (skip == 0):
            return i
        return N
            