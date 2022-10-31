from collections import deque

class queue:
    def __init__(self):
        self.data = deque()

    def add(self,element):
        self.data.append(element)

    def pop(self):
        self.data.popleft()

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def delete(self):
        del self.data

queue_obj = queue()
# queue_obj.add(10)
# queue_obj.add(20)
# queue_obj.add(30)
# print(queue_obj.data)

# queue_obj.pop()
# print(queue_obj.data)

# print(queue_obj.is_empty())

# print(queue_obj.size())


size = int(input("Enter the size : "))
for i in range(size):
    element = int(input("Enter the element : "))
    queue_obj.add(element)

print(queue_obj.data)