from logging import exception
from sqlite3.dbapi2 import _Statement
from telnetlib import theNULL


class InvalidAgeError(Exception):
    
    # def __init__(self):
    #     print("InvalidAgeError : You are still a bacchu")

    def __str__(self):
        return "You are still a bacchu"


# ATM Machine

# ask for pin first - hardcoded
# balance           - hardcoded

# if pin is correct then 
# 1. Deposit 
#     ask for amount and add it to the balance
#     if amount is greater than 25000 then raise the exception
#     if amount 100,500,1000,2000 then raise the exception

# 2. Withdraw 
#     ask for amount and subtract it to the balance
#     if amount is greater than 25000 then raise the exception
#     if amount 100,500,1000,2000 then raise the exception
#     if amount is greater than balance then raise the exception

# 3. Mini_Statement 
#     show the balance in a file

# if pin is incorrect then then raise an exception saying InvalidPinError
# if pin length is incorrect then raise the exception
# if entered pin starts with 0 then raise the exception

# Note : Try to use OOPs (getter,setter,class,method,object,file handling)