from _9_custom_exception import InvalidAgeError

class vote:
    def voting(self):
        age = int(input("Enter your age : "))
        if age >= 18:
            print("You voted successfully")
        else:
            try:
                raise InvalidAgeError()
            except Exception as ex:
                print(ex)

            
obj = vote()
obj.voting()