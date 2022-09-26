# w mode
# file = open("demo.txt","w") # filepath/filename,mode
# file.write("Good Evening!")


# # r mode - bydefault mode
# file = open("demo.txt")
# data = file.read()
# print(data)


# a mode 
# file = open("test.txt","a")
# # file.write("Hello")
# file.write("Students!")


# w+ mode
# file = open("demo1.txt","w+")
# file.write("Hey All")
# data = file.read()
# print(data)


# # r+ mode
# file = open("demo1.txt","r+")
# data = file.read()
# print(data)
# file.write("Good Night")


# # a+ mode
# file = open("demo2.txt","a+")
# file.write("Python")

# current_position = file.tell()
# print("After writing : ",current_position)

# file.seek(0,0)

# data = file.read()
# print(data)


file = open("demo1.txt","w")
file.write("hey all")
file.close()
