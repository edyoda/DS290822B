class student:

    clg_name = "Gyan Ganga College of Excellence"

    def info(self):
        self.name = input("Enter your name :")
        self.rno = input("Enter your Roll no. :")

    def marks(self):
        self.maths = int(input("Marks in Maths :"))
        self.science = int(input("Marks in Science :"))
        self.english = int(input("Marks in English :"))
        self.total = self.maths + self.science + self.english
        return self.total
      
    def percent(self,total):
        self.percentage = total / 300 * 100
        return self.percentage

    def grading(self,percentage):
        self.grade = ""
        if percentage >= 90:
            self.grade = "A"
        elif percentage < 90 and percentage >= 75:
            self.grade = "B"
        elif percentage < 75 and percentage >= 60:
            self.grade = "C"
        else:
            self.grade = "D"
        return self.grade

    def __init__(self):
        self.name = ""
        self.rno = ""
        self.grade = ""
        self.maths = ""
        self.science = ""
        self.english = ""
        self.percentage = ""
        
    def set_name(self):
        self.name = input("Enter your name :")

    def get_name(self):
        return self.name

    def set_rno(self):
        self.name = input("Enter your Roll no. :")

    def get_rno(self):
        return self.rno

    def set_maths(self):
        self.maths = input("Marks in Maths :")

    def get_maths(self):
        return self.maths

    def set_science(self):
        self.science = input("Marks in Science :")

    def get_science(self):
        return self.science

    def set_english(self):
        self.english = input("Marks in English :")

    def get_english(self):
        return self.english

    def __str__(self):
        return f"\n \n \n Name of College : {student.clg_name} \n Name of Student : {self.name} \n Roll no. : {self.rno} \n Marks in Maths : {self.maths} \n Marks in Science : {self.science} \n Marks in English : {self.english} \n Total Marks : {self.total}/300 \n Percentage : {percentage}% \n Grade : {self.grade}"

student_obj = student()
student_obj.info()
total = student_obj.marks()
percentage = student_obj.percent(total)
grade = student_obj.grading(percentage)
print("Grade : ",grade)




print(student_obj)
