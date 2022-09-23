file = open("demo.txt","w")
current_position = file.tell()
print("Before writing : ",current_position)

file.write("Python is my fav!")

current_position = file.tell()
print("After writing : ",current_position)
