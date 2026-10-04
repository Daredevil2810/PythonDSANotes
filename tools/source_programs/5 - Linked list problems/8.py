# Search Node in Linked List :

# Search for a node with a given value in a singly linked list, Return its position (1-based index) if found, If not found, return -1 or display "Not found".

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_node(head, key):
    current = head
    position = 1
    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1
    return -1  # Not found

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Linked List:")
display(head)

key = 30
pos = search_node(head, key)
if pos != -1:
    print(f"Element {key} found at position {pos}")
else:
    print(f"Element {key} not found")


# Output :

# Linked List:
# 10 -> 20 -> 30 -> 40 -> None
# Element 30 found at position 3