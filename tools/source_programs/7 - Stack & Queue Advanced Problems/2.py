# Implement Queue Using Stack :

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue Underflow")
            return None
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue is empty")
            return None
        return self.stack2[-1]

    def display(self):
        temp = self.stack2[::-1] + self.stack1
        print(temp)

queue = QueueUsingStack()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:")
queue.display()
print("Front element:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Queue after dequeue:")
queue.display()


# Output :

# Queue:
# [10, 20, 30]
# Front element: 10
# Dequeued: 10
# Queue after dequeue:
# [20, 30]