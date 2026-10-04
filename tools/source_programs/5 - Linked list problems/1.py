# Create a Singly Linked List and Display objectives :

# Traverse the list using a pointer starting at head.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Linked List:")
display(head)


# Output : 

# Linked List:
# 10 -> 20 -> 30 -> None