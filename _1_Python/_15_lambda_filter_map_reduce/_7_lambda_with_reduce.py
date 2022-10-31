from functools import reduce

data = [4,5,2,1,3,5,6]
result = reduce(lambda data1,data2 : data1+data2 , data)
print(result)
