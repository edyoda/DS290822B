class private:

    def __init__(self):
        self.__name = "Bharati"

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

obj = private()
obj.set_name("Aaditya")
print(obj.get_name())
