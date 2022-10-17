import requests

url = "http://api.zippopotam.us/us/90210"

response = requests.get(url=url).json()
print(response)