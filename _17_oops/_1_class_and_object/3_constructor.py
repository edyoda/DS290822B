# Constructor
# is a special kind of method
# it has same name as class name
# it is use to create object of class
# it is use to initialize instance variable - hold
# it is represented by __init__()
# it gets called when an object is created

class constructor: 
    def __init__(self,no1,no2):                    # Zero Constructor
        print("It's a constructor")

constructor_obj = constructor(4,5)

# Types of Constructor
# 1. Default Constructor - if you don't create a constructor in your class, 
#                          then compiler provides you a default constructor constructor
# 2. Zero Constructor    - constructor without any paramter except "self"
# 3. Parameterized Constructor - constructor with parameters

    