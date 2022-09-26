import os

# deletes the file
# os.remove("demo2.txt")

# checks if file already exist or not
# is_exists = os.path.exists("bharati.txt")
# print("Is_Exist : ",is_exists)

# deletes the directory
# it only deletes the empty folder
# os.rmdir("B:\DS290822B\DS290822B\dump")

# file = open("B:\\api_example\\bharati.txt","w")
# file.write("Hey")

# x mode
# creates the file but gives error if the file already exist
file = open("edyoda.txt","x")
file.write("x mode")
