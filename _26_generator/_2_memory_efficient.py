import memory_profiler as memory

# def fun(no):
#     lst = []
#     for i in range(no):
#         lst.append(i)
#     return lst

# print("Before calling function : ",memory.memory_usage())
# fun(100000000)
# print("After calling function : ",memory.memory_usage())

# Before calling function :  [18.03125]
# After calling function :  [7.26171875]

def gen(no):
    for i in range(no):
        yield i

print("Before calling function : ",memory.memory_usage())
gen(100000000)
print("After calling function : ",memory.memory_usage())
