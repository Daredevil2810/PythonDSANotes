# Delete Node from Specific Position :

# If position == 1, delete the head node, If the position is greater than the list length, display an error.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_from_position(head, position):
    if head is None:
        return None
    if position == 1:
        new_head = head.next
        head.next = None
        return new_head

    current = head
    count = 1
    while current.next and count < position - 1:
        current = current.next
        count += 1

    if current.next:
        node_to_delete = current.next
        current.next = node_to_delete.next
        node_to_delete.next = None
    else:
        print("Position out of bounds")

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
head.next.next.next = Node(40)

print("Original Linked List:")
display(head)

head = delete_from_position(head, 3)
print("After Deleting Node at Position 3:")
display(head)


# Output :

# Original Linked List:
# 10 -> 20 -> 30 -> 40 -> None
# After Deleting Node at Position 3:
# 10 -> 20 -> 40 -> None