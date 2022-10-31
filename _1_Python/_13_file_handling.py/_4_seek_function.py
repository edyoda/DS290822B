# seek function
# it allows you to modify the cursor position

# seek(offset,from_what)
# offset - no of position to move forward
# from_what - point of reference

# from_what - bydefault value - 0
# 0 - beginning
# 1 - current position
# 2 - end of the file

file = open("demo.txt","w")

current_position = file.tell()
print("before seek : ",current_position)

file.seek(4,0)

current_position = file.tell()
print("after seek : ",current_position)

file.write("Hello")

current_position = file.tell()
print("after writing : ",current_position)





