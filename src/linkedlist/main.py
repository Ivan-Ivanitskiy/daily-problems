class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"({self.value}, {self.next})"

def remove_dup(lst):
  current = lst
  while current and current.next:
    if current.value == current.next.value:
      current.next = current.next.next
    else:
      current = current.next

# Initialize your linked list
lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

# Call the function to remove duplicates
remove_dup(lst)

# Print the modified linked list
print(lst)
# Output: (1, (2, (3, None)))
