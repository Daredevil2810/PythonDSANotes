# Stack Using Linked List :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.display()
print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Stack after pop:")
stack.display()


# Output :

# Stack:
# 30 -> 20 -> 10 -> None
# Top element: 30
# Popped: 30
# Stack after pop:
# 20 -> 10 -> None