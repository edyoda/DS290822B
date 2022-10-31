# Heirarchical Inheritance
# single parent class and multiple child classes

class country:
    def region(self):
        print("Country is a region!")

class india(country):
    def language(self):
        print("Hindi")

    def game(self):
        print("Hockey")

class usa(country):
    def language(self):
        print("English")

    def game(self):
        print("Baseball")


india_obj = india()
india_obj.language()
india_obj.game()
india_obj.region()

usa_obj = usa()
usa_obj.language()
usa_obj.game()
usa_obj.region()

