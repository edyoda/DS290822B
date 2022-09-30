# set comprehension - it is used to create a new set from another set/list/tuple

lst = [4,5,2,1,3,5,6]

even = { i for i in lst if i%2 == 0 }
print(even)