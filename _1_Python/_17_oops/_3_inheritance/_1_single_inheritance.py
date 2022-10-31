# Inheritance
# accessing one class from another class
# reuse the code
# saving our time and efforts
# it follows Is-A Relationship

# Types of inheritance 
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# Single Inheritance 
# single parent class and single child class

# parent class
class father:
    def flat(self):
        print("Flat")

    def car(self):
        print("Car")

# child class
class son(father):
    def bike(self):
        print("Bike")

    def mobile(self):
        print("Mobile")

son_obj = son()
son_obj.bike()
son_obj.mobile()
son_obj.flat()
son_obj.car()



# class -  student
# constructor

# info()
# name,rno - take input

# marks()
# maths,science,eng - take input

# percentage()
# calculate percentage

# grade()
# calculate grade

# __str__()
# college name
# name
# rno
# sci marks
# maths marks
# eng marks
# total marks / out marks
# percentage
# grade 