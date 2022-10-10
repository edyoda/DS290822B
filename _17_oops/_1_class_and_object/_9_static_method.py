class college:

    college_name = "Edyoda"                                # class / static variable

    def __init__(self,name,rno):                           # constructor
        self.name = name
        self.rno = rno

    def __str__(self):                                     # instance method / overridden method
        return f"Name : {self.name} | Roll No. : {self.rno}"

    @staticmethod
    def general():
        no = 10
        return f"I am static method! {no}"

college_obj = college("Bharati",78)
print(college_obj.general())