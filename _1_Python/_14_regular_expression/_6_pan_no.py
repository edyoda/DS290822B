import re

data =(input("enter the no."))
res = re.findall(r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$",data)

if res:
   print("format is fine")
else:    
     print("format is inncorect")
