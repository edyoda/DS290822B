# Dunder Method | Special Method | Magic Method

# __init__
# __str__
# __mro__ mro()

# print(dir(list))

# no1 = 10
# no2 = 90
# add = no1 + no2  # call goes to __add__
# print(add)

class special_method:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self,self1):
        return self.salary + self1.salary

    def __mul__(self,self1):
        return self.salary * self1.salary

    def __len__(self):
        return len(self.name)
    
obj = special_method("Raj",10000)
obj1 = special_method("Ram",20000)

print(obj + obj1)

print(obj * obj1)

print(len(obj))