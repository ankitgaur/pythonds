from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            print("Error: Queue is empty.")

    def size(self):
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    queue = Queue()

    print("Is the queue empty?", queue.is_empty())

    queue.enqueue("one")
    queue.enqueue("two")
    queue.enqueue("three")

    print("Queue size:", queue.size())

    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)

    print("Queue size after dequeue:", queue.size())

    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)

    print("Queue size after dequeue:", queue.size())

    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)

    print("Queue size after dequeue:", queue.size())
