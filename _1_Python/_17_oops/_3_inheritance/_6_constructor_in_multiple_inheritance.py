# Multiple Inheritance
# multiple parent classes and single child class

class c:
    def procedure_feature(self):
        print("C is procedural language")

    def language(self):
        print("C is a programming language")

class cpp:
    def oops_feature(self):
        print("Cpp is object oriented programming language")

    def language(self):
        print("Cpp is a programming language")

class python(cpp,c):
    def both_feature(self):
        print("Procedural + OOPs Feature")

    def language(self):
        print("Python is a programming language")

python_obj = python()
python_obj.procedure_feature()
python_obj.oops_feature()
python_obj.both_feature()
python_obj.language()

