# Insert Node at Specific Position :

# If the position is 1, insert at the beginning, If the position is greater than the list length + 1, the insertion is invalid.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, data, position):
    new_node = Node(data)
    if position == 1:
        new_node.next = head
        return new_node

    current = head
    count = 1
    while current and count < position - 1:
        current = current.next
        count += 1

    if current:
        new_node.next = current.next
        current.next = new_node
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

print("Original Linked List:")
display(head)

head = insert_at_position(head, 25, 3)
print("After Inserting 25 at Position 3:")
display(head)


# Output : 

# Original Linked List:
# 10 -> 20 -> 30 -> None
# After Inserting 25 at Position 3:
# 10 -> 20 -> 25 -> 30 -> None