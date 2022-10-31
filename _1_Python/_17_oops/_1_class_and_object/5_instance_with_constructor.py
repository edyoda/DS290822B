# it is use to initialize instance variable - hold

class student:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        
    def display(self):
        print("Name : ",self.name)
        print("Rno : ",self.rno)

student_obj = student("Bharati",20)
student_obj.display()

student_obj1 = student("Vishal",30)
student_obj1.display()
