# static/class variable
# it is defined inside the class but outside the method/constructor
# scope - throughout the class
# it is used for memory management
# to call static variable , you need to call it using class name
# whenever there is a common value for all the objects, that is the time when we use static variable


class institute:

    ins_name = "Edyoda"

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

    def display(self):
        print("Institute : ",institute.ins_name)
        print("Name : ",self.name)
        print("Rno : ",self.rno)
        

institute_obj = institute("Raj",89)
institute_obj.display()

institute.ins_name = "Coder"

institute_obj1 = institute("Prerna",80)
institute_obj1.display()

institute.ins_name = "Sanket"

institute_obj2 = institute("Aaditya",81)
institute_obj2.display()