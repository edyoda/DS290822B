# dict comprehension - to create new dict from another data type

# str1 = "Python"
# # o/p {"P":"p","Y":"y"}

# dict_comp = {i.upper() : i.lower() for i in str1}
# print(dict_comp)

keys = [1,2,3,4,5]
value = [10,20,30,40,50]
dict1 = {k:v for k,v in zip(keys,value)}
print(dict1)

dict1 = {keys[i]:value[i] for i in range(len(keys))}
print(dict1)

# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

# [4,5,8,1,2,3]
# {4:[4,8,12.....40],5:[5,10,15,20,25,30....50]}
lst = [4,5,8,1,2,3]
# dict1 = {j:[i*j for i in range(1,11)] for j in lst}
# print(dict1)

lst1 = []
dict1 = {}
for j in lst:
    lst1 = []
    for i in range(1,11):
        lst1.append(i * j) # [5,10,15 .... 50]
    dict1[j] = lst1        # {4:[4,8,12 .... 40],5:[5,10,15 .... 50]}

print(dict1)

