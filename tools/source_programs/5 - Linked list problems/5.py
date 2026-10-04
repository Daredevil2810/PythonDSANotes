# Delete Node from Beginning :

# Update the head pointer to the second node, If the list is empty, do nothing.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_from_beginning(head):
    if head is None:
        return None
    new_head = head.next
    head.next = None  # Disconnect old head
    return new_head

def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original Linked List:")
display(head)

head = delete_from_beginning(head)
print("After Deleting from Beginning:")
display(head)


# Output : 

# Original Linked List:
# 10 -> 20 -> 30 -> None
# After Deleting from Beginning:
# 20 -> 30 -> None