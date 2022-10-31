# class father:
#     def __init__(self):
#         print("Parent Class Constructor")

# class son(father):
#     def __init__(self):
#         super().__init__()
#         print("Child Class Constructor")
    
# son_obj = son()

# class father:
#     def __init__(self):
#         print("Parent Class Constructor")

# class son(father):
#     def __init__(self):
#         super().__init__()
#         print("Child Class Constructor")
    
# son_obj = son()

class college:
    def __init__(self,name,address):
        self.name = name
        self.address = address

class student(college):
    def __init__(self,student_name,rno,age,name,address):
        super().__init__(name,address)
        self.student_name = student_name
        self.rno = rno 
        self.age = age 

    def __str__(self):
        return f"Student Name : {self.student_name} \nRno : {self.rno} \nAge : {self.age} \nCollege Name : {self.name} \nCollege Address : {self.address}"

student_name = input("Enter student name : ")
student_rno = input("Enter student rno : ")
student_age = input("Enter student  age : ")
college_name = input("Enter college name : ")
college_address = input("Enter college address : ")

student_obj = student(student_name,student_rno,student_age,college_name,college_address)
print(student_obj)




