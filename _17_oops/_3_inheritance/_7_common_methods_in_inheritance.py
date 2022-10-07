class mother:
    def car(self):
        print("Audi")

class father:
    def flat(self):
        print("Flat")

    def car(self):
        print("Maruti")

class son(father,mother):
    def car(self):
        # super().car()
        mother.car(self)
        father.car(self)
        print("BMW")

    def mobile(self):
        print("Mobile")

# super - represents immediate parent class object

son_obj = son()
son_obj.mobile()
son_obj.flat()
son_obj.car()
