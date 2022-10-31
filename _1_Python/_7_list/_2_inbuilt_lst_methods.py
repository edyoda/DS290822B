lst = [6,7,4,2,5,7,8]
print("Og : ",lst)

# lst.append(10)           # used to add element at the end of the list
# print("Append : ",lst)

# lst.insert(2,100)        # used to add an element at specific position on the bases of index
# print("Insert : ",lst)

# lst.extend([5,6,7,8])
# print("Extend : ",lst)

# lst.remove(7)              # deletes the value on the bases of element passed
# print("Remove : ",lst)

# lst.pop()                   # bydefault deletes the last value of list
# print("Pop : ",lst)

# lst.pop(1)                   # deletes the value on the bases of index passed
# print("Pop : ",lst)

# lst.reverse()
# print("Reverse : ",lst)

# lst.sort()               # ascending order
# print("Sort : ",lst)

# lst.sort(reverse=True)   # descending order
# print("Sort : ",lst)

# lst.clear()
# print(lst)

# counter = lst.count(7)
# print("Count : ",counter)

# index_demo = lst.index(4)
# print("Index : ",index_demo)

# length = len(lst)
# print(length)

# str1 = "Ankit"
# count = 0
# for i in str1:
#     count = count + 1 #5
#     print(i,count)

del lst[2]
print(lst)