class exp_handling:
    def divide(self):
        div = 0
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        div = no1 / no2    
        print("Division : ",div)
        print("End of program")

# class exp_handling:
#     def divide(self):
#         div = 0
#         no1 = int(input("Enter no1 : "))
#         no2 = int(input("Enter no2 : "))
#         try:
#             div = no1 / no2
#         except Exception as ex:
#             print(ex)
            
#         print("Division : ",div)
#         print("End of program")

obj = exp_handling()
obj.divide()

# Block
# try    - it is use to store suspious code
# except - is use to handle the exception