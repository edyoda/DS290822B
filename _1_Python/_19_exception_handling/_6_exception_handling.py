try:
    print(10/0)
except (ZeroDivisionError,TypeError) as ex:
    print(ex)
finally:
    print("Finally Block")

# finally block will execute everytime regardless of whether exception has occured or not
# it is mainly used to close the file and close the database