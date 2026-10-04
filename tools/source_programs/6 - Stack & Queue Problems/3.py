# Implement Queue Using Array :

class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        value = self.arr[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.arr[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for i in range(self.front, self.rear + 1):
            print(self.arr[i], end=" -> ")
        print("None")

queue = Queue(5)
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
# 10 -> 20 -> 30 -> None
# Front element: 10
# Dequeued: 10
# Queue after dequeue:
# 20 -> 30 -> None