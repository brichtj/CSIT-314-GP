import requests

url = "http://localhost:5000/login"
data = {
    "email": "homeowner1@example.com",
    "password": "passwordHO1",
    "user_profile": "HomeOwner"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
