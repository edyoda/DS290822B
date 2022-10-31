age = int(input("Enter your age : "))

if age >= 18:
    print("You are eligible to work, but we would need to check your qualification too")
    qualification = int(input("Enter your qualification, for ex. for graduation you may enter 15 : "))
    if qualification >= 15:
        print("You are hired!")
        if qualification == 19:
            print("You are over-qualified!")
    elif qualification <= 13:
        print("Complete your graduation first!")
    else:
        print("You are not eligible")
else:
    print("You are not eligible")

    
