class ChainedHashTable:
    class Node:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, M) -> None:
        self.list = [None for k in range(0, M)]
        self.M = M
    
    def put(self,key,value):
        hashKey = self.hashKey(key)
        if self.list[hashKey] == None:
            self.list[hashKey] = self.Node(key,value)
        else:
            current = self.list[hashKey]
            while (current.next != None):
                current = current.next
            current.next = self.Node(key,value)

    def hashKey(self, key):
        return key % self.M

    def get(self,key):
        hashKey = self.hashKey(key)
        current = self.list[hashKey]
        while (current != None):
            if current.key == key:
                return current.value
            else:
                current = current.next    
        
        return None