# Insert Node at End :

# Traverse the list to reach the last node, then link the new node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node  # Empty list

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(10)
head.next = Node(20)

print("Original Linked List:")
display(head)

head = insert_at_end(head, 30)
print("After Inserting 30 at End:")
display(head)


# Output : 

# Original Linked List:
# 10 -> 20 -> None
# After Inserting 30 at End:
# 10 -> 20 -> 30 -> None