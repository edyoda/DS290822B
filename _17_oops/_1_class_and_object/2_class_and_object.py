class shape:
    def triangle(self):
        base = int(input("Enter base value :"))
        height = int(input("Enter height value :"))
        area = height * base / 2
        print("Area of triangle :", area)

    def square(self):
        side = int(input("Enter length of side :"))
        area = side ** 2
        print("Area of square :", area)

    def circle(self):
        radius = int(input("Enter length of radius :"))
        area = 3.14159 * radius ** 2
        print("Area of circle :", area)

shape_obj = shape()   # default constructor

shape_obj.triangle()
shape_obj.square()
shape_obj.circle()

# self - is a keyword
# it represents the object of current class
