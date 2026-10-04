# Insert Node at Beginning

# Update the head pointer to the new node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # Update head

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(20)
head.next = Node(30)

print("Original Linked List:")
display(head)

head = insert_at_beginning(head, 10)
print("After Inserting 10 at Beginning:")
display(head)


# Output : 

# Original Linked List:
# 20 -> 30 -> None
# After Inserting 10 at Beginning:
# 10 -> 20 -> 30 -> None