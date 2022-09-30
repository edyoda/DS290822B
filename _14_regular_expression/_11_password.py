import re
password = input("Enter a Password :")
res = re.findall(r"^.*(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]){8,16}.*$",password)
print(res)
if res:
    print("Correct Format")
else:
    print("Incorrect Format")
