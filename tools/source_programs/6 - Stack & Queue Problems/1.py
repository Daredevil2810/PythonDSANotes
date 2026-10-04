# Stack Using Array :

# Support basic stack operations:
# Push – add element to the top
# Pop – remove element from the top
# Peek/Top – see the top element
# IsEmpty – check if stack is empty
# IsFull – check if stack is full

class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.top = -1

    def push(self, value):
        if self.top >= self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        if self.top < 0:
            print("Stack Underflow")
            return None
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.top < 0:
            print("Stack is empty")
            return None
        return self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Top element after pop:", stack.peek())


# Output :

# Top element: 30
# Popped: 30
# Top element after pop: 20