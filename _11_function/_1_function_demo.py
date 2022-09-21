# Function
# it is use to reuse the code
# you can use the same set of code with little modification if needed
# syntax : 
# def <function_name>:
#    <function_body>

def addition():               # defining the function
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    add = no1 + no2
    print("Addition : ",add)

# addition()                    # calling the function
# addition()

def sorting():
    size = int(input("Enter the size of list :"))
    lst = []
    for i in range(size):
        element = int(input("Enter a number :"))
        lst.append(element)

    for i in range(size):
        for j in range(i+1, size):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
                # lst[i], lst[j] = lst[j], lst[i]
    print("Ascending order :", lst)


# sorting()

# for i in range(2):
#     sorting()

