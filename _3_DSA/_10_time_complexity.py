# # O(1) - Constant Time
# # - An algorithm is said to have constant time when it is non-dependent on the input data(n).
# # - No matter the size of input, the execution time will always be the same

# no1 = 100
# no2 = 200
# no3 = no1 + no2

# if no1 > no2:
#     print(True)
# else:
#     print(False)

# lst = [1,2,4,56,3]
# print(lst[0])


# O(n) - Linear Time
# - An algorithm is said to have linear time when the execution time increases linearly with 
# the increase in the size of the input

# def add(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     print("sum : ",sum)

# add(1)

# add([2,6,8,2])

# add([i for i in range(1000)])

# add([i for i in range(10000)])



# # O(n2) - Quadratic Time (read as O of n square)
# # An algo where for each input, another O(n) is executed is said to have quadratic time

# def add(lst):
#     sum = 0
#     for row in lst:
#         for element in row:
#             sum += element

#     print("Sum : ",sum)


# add([[0]])

# add([[1,2],[3,4]])

# add([1,2,3],[4,5,6],[7,8,9])



# # O(log n) - Logarithmic Time
# # - An algo where with every iteration, the size of input keeps reducing is said to have 
# # logarithmic time.

# # Binary Search
# def binary_search(lst,value): # [1,2,3,4,5,6,7] , 5
#     length = len(lst) # 7
#     left = 0
#     right = length - 1 # 6
#     while left <= right:
#         middle = (left + right) // 2
#         if value < lst[middle]:
#             right = middle + 1
#         elif value > lst[middle]:
#             left = middle + 1   # 1
#         elif value == lst[middle]:
#             return value
#         else:
#             return False

# data = binary_search([1,2,3,4,5,6,7],8)
# print(data)


# O(n!) - Factorial Time
# An algo where the execution complexity increases factorially with the increase in the input
# value
def factorial(data): # 123 = 6
    fact = 1
    for i in data:
        fact *= i

    print(fact)

factorial(1) # 1

factorial(5) # 1 * 2 * 3 * 4 * 5

factorial(100)


