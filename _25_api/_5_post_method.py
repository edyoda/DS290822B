from urllib import request
import requests
url = "https://jsonplaceholder.typicode.com/todos"

request_body = {
    'rno' : 1,
    'name' : "Bharati"
}

# response = requests.request("POST",url,json=request_body)
# print(response.json())

response = requests.post(url,json=request_body)
print(response.json())