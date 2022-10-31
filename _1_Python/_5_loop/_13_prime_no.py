no = int(input("Enter your no :  "))

if no != 1:
    for i in range(2,no):
        if no % i == 0:
            print("Composite no")
            break
    else:
        print("Prime no")
else:
    print("It is neight prime nor composite")