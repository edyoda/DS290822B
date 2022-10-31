# str1 = "Python is a programming language"
# str_lst = str1.split()

# max_len = 0
# for i in str_lst:
#     if len(i) > max_len:
#         max_len = len(i) # 11
#         result = i       # programming

# print(result)

str1 = 'python is a programming language'
lst1 = (str1.split(" "))
lst2 = []
print(lst1)
for i in lst1:
    length = len(i)
    lst2.append(length)
print(lst2)
print(max(lst2))
