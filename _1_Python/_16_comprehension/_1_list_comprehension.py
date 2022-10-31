# list comprehension - it is used for creating new list from another list


# for i in lst:
#     if <condition>:
#         <body>

# [body for i in lst if <condition>]

# if you have else in your program then 
# [body if body else body for i in lst] ---> only works if you have else

# nums = [5,6,3,2,4,8,6,9]

# normal way
# new_lst = []

# for i in nums:
#     new_lst.append(i)

# print(new_lst)

# with list comprehension
# data = [i for i in nums]
# print(data)