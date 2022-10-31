# Encapsulation
# binding attributes(variable) and behaviour(method) together into single unit
# accessing private member through public environment

# private member - cannot be accessed outside the class
class laptop:

    def __init__(self,ram,processor,brand):
        self.ram = ram 
        self.processor = processor
        self.brand = brand

    # setter and getter - you can specifically modify each variable
    def set_ram(self,ram):
        self.ram = ram

    def get_ram(self):
        return self.ram

    def set_processor(self,processor):
        self.processor = processor

    def get_processor(self):
        return self.processor

    def set_brand(self,brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def __str__(self):
        return f"Ram : {self.ram} \nProcessor : {self.processor} \nBrand : {self.brand}"

laptop_obj = laptop("4","i3","HP")
print(laptop_obj)

# laptop_obj.set_ram("8")
# print(laptop_obj.get_ram())

# laptop_obj.set_brand("Lenovo")

# print(laptop_obj.display())






