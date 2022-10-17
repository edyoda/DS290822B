# Array ----> List

# List
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

obj = array(2)
obj.add(10)
print(obj.data)
obj.add(20)
print(obj.data)
obj.add(30)
print(obj.data)

