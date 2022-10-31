# deque

# it is open from both the ends
# one can add/delete the elements from both the ends

from collections import deque

deque_obj = deque([3,41,2,4,6,7])
print(deque_obj)

print(deque_obj[1])

deque_obj.append(10)
print(deque_obj)

deque_obj.appendleft(20)
print(deque_obj)

deque_obj.pop()
print(deque_obj)

deque_obj.popleft()
print(deque_obj)

deque_obj.
