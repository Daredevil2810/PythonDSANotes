# Delete Node from End :

# Update secondToLast.next = null, If the list has only one node, set head = null.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_from_end(head):
    if head is None:        # Empty list
        return None
    if head.next is None:   # Single node
        return None

    current = head
    while current.next.next:  # Traverse to second-to-last
        current = current.next
    current.next = None       # Delete last node
    return head

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

head = delete_from_end(head)
print("After Deleting from End:")
display(head)


# Output :

# Original Linked List:
# 10 -> 20 -> 30 -> None
# After Deleting from End:
# 10 -> 20 -> None