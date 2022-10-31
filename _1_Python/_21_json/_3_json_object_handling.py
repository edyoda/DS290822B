import json

json_obj = """{
    "name":"Bharati",
    "female": true,
    "qualification": null,
    "abc": false
}"""

# converts json into dict
data = json.loads(json_obj)
print(data)
print(type(data))


# convert dict into json
json_obj = json.dumps(data)
print(json_obj)


