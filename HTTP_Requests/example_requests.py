import requests

response = requests.get('https://api.github.com/users/gvanrossum')

data = response.json()
type(data) # dict
print(data)