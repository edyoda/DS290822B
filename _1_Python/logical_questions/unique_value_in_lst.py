# lis3 = [2,4,6,6,4,3,6,6,9,8,3,2,5,2,5,1,8]
# lis4 = []
# for i in lis3:
#   if i not in lis4:
#     lis4.append(i)
# print(lis4)

lst = [5,6,3,1,3,5,2,4]
lst1 = []
for i in lst:
    count = lst.count(i)
    if count == 1:
        lst1.append(i)
print(lst1)

