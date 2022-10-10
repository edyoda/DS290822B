# static and class variable are same thing
# but static method and class method are different

# cls - class

class college:

    college_name = "Edyoda"                                # class / static variable

    def __init__(self,name,rno):                           # constructor
        self.name = name
        self.rno = rno

    def __str__(self):                                     # instance method / overridden method
        return f"Name : {self.name} | Roll No. : {self.rno}"

    @classmethod
    def get_college_name(cls):
        return cls.college_name

    @classmethod
    def set_college_name(cls,college_name):
        cls.college_name = college_name

college_obj = college("Bharati",67)
print(college_obj)

data = college.get_college_name()
print(data)

college.set_college_name("Coder")
    
data = college.get_college_name()
print(data)
