# Circular Queue Using Array :

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [0]*size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow")
            return
        if self.is_empty(): self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        value = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
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
        i = self.front
        while True:
            print(self.arr[i], end=" -> ")
            if i == self.rear: break
            i = (i + 1) % self.size
        print("None")

queue = CircularQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Queue:")
queue.display()
print("Front element:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Queue after dequeue:")
queue.display()


# Output :

# Queue:
# 10 -> 20 -> 30 -> 40 -> None
# Front element: 10
# Dequeued: 10
# Queue after dequeue:
# 20 -> 30 -> 40 -> None