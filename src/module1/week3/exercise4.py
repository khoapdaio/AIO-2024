class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Enqueue to a full queue")
        self.queue.append(value)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]

# Ví dụ sử dụng
queue = MyQueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue is full:", queue.is_full())  # Output: True
print("Front element:", queue.front())    # Output: 1

queue.dequeue()
print("Front element after dequeue:", queue.front())  # Output: 2
print("Queue is empty:", queue.is_empty())            # Output: False

queue.dequeue()
queue.dequeue()
print("Queue is empty after dequeuing all elements:", queue.is_empty())  # Output: True

# Thử đẩy vào một phần tử vào queue đầy sẽ gây ra lỗi
try:
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)  # This will raise an OverflowError
except OverflowError as e:
    print(e)

# Thử lấy phần tử đầu tiên từ queue rỗng sẽ gây ra lỗi
try:
    queue.dequeue()  # This will raise an IndexError
except IndexError as e:
    print(e)
