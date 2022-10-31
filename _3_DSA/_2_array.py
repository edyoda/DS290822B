# Array ----> List

# List
# -> it accepts heterogenous data (only in python and js)
# -> it doesnot have a fix size (only in python and js)
# -> it is used to store collection of same/different types of data
# -> fetch the data 
# -> insert the data at specify position 
# -> remove the data 

# lst = [] # [6,7,1,2,4,5]
# lst.append(6)
# lst.extend([6,7,1,2,4,5])
# lst.insert(2,10)
# lst.remove(4)
# print(lst)

# type of arrays
# 1D - [1,3,4,5,7,7]
# 2D - 
# [ 
#     1, 2, 3
#     4, 5, 6
# ]

class array:
    def __init__(self,fix_size):
        self.fix_size = fix_size
        self.length   = 0
        self.data     = []
    
    def add(self,element):
        if self.length < self.fix_size:
            self.data.append(element)
            self.length += 1
        else:
            print("Array is full")

    def remove(self,index):
        for i in range(self.length):
            if i == index:
                del self.data[index]
                self.length -= 1
            else:
                "No such index found"

    def insert(self,index,element):
        if self.length < self.fix_size:
            self.data.insert(index,element)
            # for i in range(self.length,index,-1): # 3, 2, -1
            #     self.data[i] = self.data[i-1]
            # self.data[index] = element
            # self.length += 1

obj = array(5)
obj.add(10)
obj.add(20)
obj.add(30)
obj.add(40)
obj.insert(2,100)
print(obj.data)
