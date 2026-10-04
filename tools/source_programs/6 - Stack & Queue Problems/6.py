# Circular Queue Using Linked List :

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        value = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.front:
                break
        print("(back to front)")

queue = CircularQueue()
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
# 10 -> 20 -> 30 -> (back to front)
# Front element: 10
# Dequeued: 10
# Queue after dequeue:
# 20 -> 30 -> (back to front)