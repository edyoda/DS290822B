class grandpa():
    def field(self):
        print("Field")

# parent class
class father(grandpa):
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
son_obj.field()


