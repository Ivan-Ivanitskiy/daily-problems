# Remove duplicates from the linked list

Given a sorted linked list of integers, remove all the duplicate elements in the linked list so that all elements in the linked list are unique.

Here's an example and some starter code:

``` python

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"({self.value}, {self.next})"

def remove_dup(lst):
  # Fill this in.

lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))
```