import re

aadhar = (input("Enter your Aadhar no :"))
res = re.findall("^[1-9]{1}[0-9]{3}[-][0-9]{4}[-][0-9]{4}$", aadhar)
if res:
   print("It is correct")

else:
    print("It is incorrect")

# 1234-5678-8907