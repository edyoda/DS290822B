# # folder --> packages
# # python file (.py file) --> modules

# # packages
# # to store/group similar kind of programs
# # to keep things organized
# # security purpose
# # to reuse the code

# # modules
# # to write the code
# # reuse the code


# # 20-09-2022

# # write a program to reverse the list take dynamic list
# # method -1               general method

# # num = int(input('please enter number of elements in list = '))
# # list1 = []
# # for i in range(1, num+1):
# #   list2 = int(input('elements = '))
# #   list1.append(list2)
  
# # print('given list = ',list1)
# # print('reverse list = ',list1[::-1])


# # write a program to reverse the list take dynamic list
# # method - 2         nested loop method

# num3 = int(input('please enter number of elements in list = '))
# vari1 = []
# for i in range(1, num3 +1):
#   vari2 = int(input('elements = '))
#   vari1.append(vari2)
# print('given list = ',vari1)

# # [6, 1, 2]
# # [1, 6, 2]
# # []

# for i in range(num3): # 2
#   for j in range(i):  # 0
#     print(vari1[i],vari1[j])
#     vari1[i],vari1[j] = vari1[j],vari1[i] # 2,1 = 1,2
#     print(vari1[i],vari1[j])
#     print(vari1)

# print('reverse list =',vari1)

# l1 = [1,3,5,7,9]
# l2 = [2,4,6,8,10]
# index = 0
# for i in range(1,11,2):        # 5
#     l1.insert(i, l2[index])    #l2[2] = 2
#     index += 1
# print(l1)


