# types of argument/parameters
# 1. required / positional argument
# 2. default argument
# 3. keyword argument
# 4. variable-length argument
#     a) Arbitary positional argument (*args)
#     b) Arbitary keyword argument    (**kwargs)


# # required / positional argument
# def student(rno,name):
#     print("Rno : ",rno,"Name : ",name)

# student(12,"Rakesh")



# # default argument
# def student(rno,name="Bharati",address="Mumbai"):
#     print("Rno : ",rno,"Name : ",name, "Address : ",address)

# student(6)



# keyword argument
# def nos(no1,no2=20,no3=30,no4=40):
#     print(no1,no2,no3,no4)

# nos(no1=100,no4=400)


# Variable-length argument
# *args
# tuple

# def users(*args):
#     print(args,type(args))
#     for i in args:
#         print(i)
#     data = args[4]
#     print(data)

# users(5,7,8,9,10,[1,5,6,7,100],{1:"Bharati"})

# **kwargs
# dict
def users(**kwargs):
    print(kwargs,type(kwargs))
    for k,v in kwargs.items():
        print(k," ",v)

users(one="Bharati",two="Ranjana",three="Hemlatha")
