import json

file = open("B:\\DS290822B\\DS290822B\\_21_json\\sample_json.json")
# file = open("_21_json\\sample_json.json")

# convert json into dict
data = json.load(file)
print(data)
print(type(data))

file1 = open("B:\\DS290822B\\DS290822B\\_21_json\\sample_json1.json","w")
# convert dict into json
json.dump(data,file1)
