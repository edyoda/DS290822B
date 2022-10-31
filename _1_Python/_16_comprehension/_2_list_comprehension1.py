# lst = [4,5,61,2,8,10,11]

# even_lst = []
# for i in lst:
#     if i%2==0:
#         even_lst.append(i)

# print(even_lst)


# data = [i for i in lst if i%2==0]
# print(data)


# str1 = "Python"
# o/p = ['P','y','t','h','o','n']

# word = input("Enter a word :")
# data = [i for i in word]
# print(data)


# lst = ["apple","mango","Aeroplane","ac","laptop","diary","mobile"]
# o/p = ["apple","Aeroplane"] # starts with A and length more than 4

# lst = ["apple","mango","Aeroplane","ac","laptop","diary","mobile"]
# data=[i for i in lst if i.lower().startswith('a') and len(i)>4]
# print(data)

# lst = ["apple","mango","Aeroplane","ac","laptop","diary","mobile"]
# data = [i for i in lst if (i.startswith("a") or i.startswith("A")) and len(i) > 4]
# print(data)


# lst = [10,4,6,1,7,8,9,11,56] # 9 - 0 ,1 ,2, 3 ,4 ,5 ,6 ,7 ,8
# 0 , 2 , 5, 7
# [10,6,8,11]

# data = [lst[i] for i in range(len(lst)) if i in (0,2,5,7)]
# print(data)

# new_lst = []
# for i in range(len(lst)):
#     if i in [0,2,5,7]:
#         new_lst.append(lst[i])



# lst = [10,4,6,1,7,8,9,11,56,10,2,3,4,5] # 9 - 0 ,1 ,2, 3 ,4 ,5 ,6 ,7 ,8
# [4,1,8,11]

# lst = [10,4,6,1,7,8,9,11,56]
# data=[lst[i] for i in range(len(lst)) if i%2!=0]
# print(data)




lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

# o/p [4,5]

data = [i for i in lst1 for j in lst2 if i==j]
print(data)

lst3 = []
for i in lst1:
    for j in lst2:
        if i == j:
            lst3.append(i)