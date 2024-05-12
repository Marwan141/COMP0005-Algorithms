class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.color = False


class RedBlackTree:
    def __init__(self) -> None:
        self.NIL = Node(0,0)
        self.root = self.NIL

    def get(self, node, key):
        if (node is None):
            return None
        if (node.key == key):
            return node.value
        elif (key < node.key):
            return self.get(node.left, key)
        elif (key > node.key):
            return self.get(node.right, key)

    def flipColor(self, node):
        node.color = True
        node.left.color = False
        node.right.color = False

    def rotate_left(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        temp.color = node.color
        node.color = True

    def rotate_right(self,node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        temp.color = node.color
        node.color = True

    def put(self, n, key, value):
        if n == None:
            return Node(key, value)
        if key < n.key:
            n.left = self.put(n.left, key, value)
        elif key > n.key:
            n.right = self.put(n.right, key, value)
        else:
            n.value = value

        if n.right.color == True and n.left.color == False:
            n = self.rotate_left(n)
        if n.left.color == True and n.left.left.color == True:
            n = self.rotate_right(n)
        if n.left.color == True and n.right.color == True:
            n = self.flipColor(n)

        return n





