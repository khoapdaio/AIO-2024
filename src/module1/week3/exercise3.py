class MyStack:
	def __init__(self, capacity):
		self.capacity = capacity
		self.stack = []

	def is_empty(self):
		return len(self.stack) == 0

	def is_full(self):
		return len(self.stack) == self.capacity

	def pop(self):
		if self.is_empty():
			raise IndexError("Pop from an empty stack")
		return self.stack.pop()

	def push(self, value):
		if self.is_full():
			raise OverflowError("Push to a full stack")
		self.stack.append(value)

	def top(self):
		if self.is_empty():
			raise IndexError("Top from an empty stack")
		return self.stack[-1]


# Ví dụ sử dụng
stack = MyStack(3)
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack is full:", stack.is_full())  # Output: True
print("Top element:", stack.top())  # Output: 3

stack.pop()
print("Top element after pop:", stack.top())  # Output: 2
print("Stack is empty:", stack.is_empty())  # Output: False

stack.pop()
stack.pop()
print("Stack is empty after popping all elements:", stack.is_empty())  # Output: True

# Thử đẩy vào một phần tử vào stack đầy sẽ gây ra lỗi
try:
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)  # This will raise an OverflowError
except OverflowError as e:
	print(e)

# Thử lấy phần tử trên cùng từ stack rỗng sẽ gây ra lỗi
try:
	stack.pop()  # This will raise an IndexError
except IndexError as e:
	print(e)
