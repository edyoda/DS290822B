import re

# data="hello ranjana"
# res=re.findall("[lea]", data) # it will return only characters like l,e,a
# print(res)

# data="hello ranjana"
# res=re.findall("[^ahz]", data) # it will return all the characters excluding a,h,z
# print(res)

# data="hello ranjana"
# res=re.findall("[a-f]", data) # it will return all the characters between a and f including both
# print(res)

# data="Hello Ranjana"
# res=re.findall("[a-zA-Z]", data) # it will return all the small and capital letters
# print(res)

# data="hello ranjana"
# res=re.findall("[a]", data) # it will return all the 'a' from the string
# print(res)

# data="hello ranjana"
# res=re.findall("[a-z]{5}", data) # it will return all the starting 5 small letters of every word
# print(res)

# data = "67 89"
# res = re.findall("[4-7]",data)
# print(res)

# data="795"
# res=re.findall("[1-5][5-9][1-3]", data)
# print(res)

data = "abc123"
res = re.findall("\d{10}",data)

if res:
    print("Format is fine")
else:
    print("Format is incorrect")

