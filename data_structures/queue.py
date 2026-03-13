class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.peek())
print("Dequeued element:", queue.dequeue())
print("Queue size:", queue.size())
print("Is queue empty?", queue.is_empty())
