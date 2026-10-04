# Find Maximum and Minimum Node in Linked List systematically :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_max_min(head):
    if head is None:
        print("List is empty")
        return

    max_val = head.data
    min_val = head.data
    current = head.next

    while current:
        if current.data > max_val:
            max_val = current.data
        if current.data < min_val:
            min_val = current.data
        current = current.next

    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(10)
head.next = Node(50)
head.next.next = Node(30)
head.next.next.next = Node(5)

print("Linked List:")
display(head)

find_max_min(head)


# Output :

# Linked List:
# 10 -> 50 -> 30 -> 5 -> None
# Maximum value: 50
# Minimum value: 5