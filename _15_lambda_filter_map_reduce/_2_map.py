lst = [4,5,1,2,10,9,7,45]

# def square(data):
#     sq_lst = []
#     for i in data:
#         sq = i ** 2
#         sq_lst.append(sq)
#     return sq_lst

# square_lst = square(lst)
# print(square_lst)

def square(data):
    return data ** 2

square_lst = list(map(square,lst))
print(square_lst)

