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
    
    def minDepth(self, depth = 0):
        if self.left and self.right:
            return min(self.left.minDepth(depth+1), self.right.minDepth(depth + 1))
        if self.left:
            return self.left.minDepth(depth + 1)
        if self.right:
            return self.right.minDepth(depth + 1)
        return depth + 1

def min_depth_bst(root):
    return root.minDepth()
  
n3 = Node(3, None, Node(4))
n2 = Node(2)
n1 = Node(1, n2, n3)

#     1
#    / \
#   2   3
#        \
#         4
print(n1)
print(min_depth_bst(n1))
# 2