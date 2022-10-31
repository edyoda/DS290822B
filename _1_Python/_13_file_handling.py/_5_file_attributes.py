file = open("test.txt")
file.close()

mode = file.mode
print("Mode : ",mode)

file_name = file.name
print("Filename : ",file_name)

close = file.closed
print("Close : ",close)