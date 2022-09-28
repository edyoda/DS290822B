from functools import reduce

lst = [4,5,1,2,10,9,7,45]

# def sum(data):
#     sums = 0
#     for i in data:
#         sums += i
#     return sums

# result = sum(lst)
# print(result)

def sum(data1,data2):
    return data1 * data2

result = reduce(sum,lst)
print(result)

