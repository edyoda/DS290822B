# 1. local variable
# - are variables are define inside the function
# - scope - within the same function
# parameters/argument - local variables


# 2. global variable
# - are the variable which are define outside the function
# - scope - throughout the python file


name = "Bharati"            # global variable


def add(no3):               # local variable
    no1 = 10                # local variable
    no2 = 20
    addition = no1 + no2 + no3
    global address          # global variable
    address = "Mumbai"
    print("Inside the function : ",name)
    print("Inside the function : ",address)
    return addition


add(6)
print("Outside the function : ",name)
print("Outside the function : ",address)


def test():
    print(address)

test()