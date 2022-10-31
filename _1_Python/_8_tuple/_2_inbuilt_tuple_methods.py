tup = (3,4,5,6,8,9,10,3)
print(tup)

count_demo = tup.count(3)
print(count_demo)

index_demo = tup.index(10)
print(index_demo)

length = len(tup)
print(length)

# 2nd way of creating tuple
# tuple()
tup = tuple((1,2,3,))
print(tup,type(tup))

count_demo = tup.count(3)
print(count_demo)

for i in tup:
    print(i)


# dir()
# tuple_methods = dir(tuple)
# print(tuple_methods)

# list_methods = dir(list)
# print(list_methods)

