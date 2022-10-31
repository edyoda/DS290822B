# stack = [1,6,1,2,4,5]
# print(stack.pop())
# print(stack)


from collections import deque
# deque_obj = deque()
# deque_obj.append([1,2,3,4])
# print(deque_obj)


class stack:
    def __init__(self):
        self.obj = deque()

    def push(self,element):
        self.obj.append(element)
        
    def pop(self):
        return self.obj.pop()

    def peek(self):
        return self.obj[-1]

    def is_Empty(self):
        return len(self.obj) == 0

    def delete(self):
        self.obj.clear()

    
stack_obj = stack()
stack_obj.push("aaditya")
stack_obj.push("ankita")
stack_obj.push("nishant")
print("Peek : ",stack_obj.peek())
print(stack_obj.obj)
stack_obj.pop()
print(stack_obj.obj)
stack_obj.delete()
print(stack_obj.is_Empty())

    