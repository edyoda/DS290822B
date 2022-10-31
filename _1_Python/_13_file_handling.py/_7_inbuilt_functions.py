file = open("demo1.txt","w")

# data = file.read() #reads the whole data
# print(data)

# data = file.read(5) #reads only 5 characters as we mentioned 5 in parameter
# print(data)

# data = file.readline() # only reads the first line
# print(data)

# data = file.readlines() # it returns list of lines
# print(data)

# for i in file:
#     print(i,end="")

# file.write("Hello")

lst = ["Hey all\n","Bye All"]
file.writelines(lst)