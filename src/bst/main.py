class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"
    
    def split(self, s):
        if self.value > s:
            if self.left:
                left, right = self.left.split(s)
                self.left = right
                return left, self
            else:
                return None, self
        else:
            if self.right:
                left, right = self.right.split(s)
                self.right = left
                return self, right
            else:
                return self, None
  
n2 = Node(2)
n1 = Node(1, None, n2)

n5 = Node(5)
n4 = Node(4, None, n5)

root = Node(3, n1, n4)

print(root)
# (3, (1, None, (2)), (4, None, (5)))

print(root.split(2))
# ((1, None, (2)), (3, None, (4, None, (5))))
