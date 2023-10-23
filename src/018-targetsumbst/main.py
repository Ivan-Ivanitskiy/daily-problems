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
    
    def isTargetSum(self, sum):
        if self.left and self.right:
            return self.left.isTargetSum(sum - self.value) or self.right.isTargetSum(sum - self.value)
        if self.left:
            return self.left.isTargetSum(sum - self.value) or (sum - self.value == 0)
        if self.right:
            return self.right.isTargetSum(sum - self.value) or (sum - self.value == 0)
        return sum - self.value == 0

def target_sum_bst(root, target):
    return root.isTargetSum(target)

#      1
#    /   \
#   2     3
#    \     \
#     6     4
n6 = Node(6)
n4 = Node(4)
n3 = Node(3, None, n4)
n2 = Node(2, None, n6)
n1 = Node(1, n2, n3)

print(n1)
print(target_sum_bst(n1, 9))
# True
# Path from 1 -> 2 -> 6