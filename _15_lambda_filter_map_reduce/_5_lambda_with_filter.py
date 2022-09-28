lst = [4,5,61,2,8,10,11]

# def even(lst):
#     even_lst = []
#     for i in lst:
#         if i%2==0:
#             even_lst.append(i)
#     return even_lst

# elst = even(lst)
# print(elst)




# def even(lst):
#     return lst%2==0

# even_lst = list(filter(even,lst))
# print(even_lst)



even_lst = list(filter(lambda lst : lst%2==0,lst))
print(even_lst)