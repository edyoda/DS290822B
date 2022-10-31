import re
# pin = (input("Enter your Pincode :"))
# res = re.findall("[1-9][0-9][0-9][0-9][0-9][0-9]", pin)
# if res:
#    print("It is correct")
# else:
#     print("It is incorrect")


pin = (input("Enter your Pincode :"))
res = re.findall("^[1-9]{1}[0-9]{5}$", pin)
if res:
   print("It is correct")

else:
    print("It is incorrect")



