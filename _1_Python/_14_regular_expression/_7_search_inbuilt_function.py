import re

data="hello ranjana"
res=re.search("hello", data) # it will return only characters like l,e,a
print(res)

# search() is same as findall() but it gives output as <re.Match object; span=(0, 5), match='hello'>

