# Count Nodes in Linked List :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):
    current = head
    count = 0
    while current:
        count += 1
        current = current.next
    return count

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

total_nodes = count_nodes(head)
print(f"Total nodes in the linked list: {total_nodes}")


# Output :

# Linked List:
# 10 -> 20 -> 30 -> 40 -> None
# Total nodes in the linked list: 4