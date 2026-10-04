# Stack Using Single Queue (Efficient Pop) :

from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, value):
        size = len(self.queue)
        self.queue.append(value)
        for _ in range(size):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.queue[0]

    def display(self):
        print(list(self.queue))

stack = StackUsingQueue()
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

# [30, 20, 10]
# Top element: 30
# Popped: 30
# Stack after pop:
# [20, 10]