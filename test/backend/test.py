import requests

url = "http://127.0.0.1:8000/login"
payload = {
    "username": "user_1",
    "password": "user123"
}

response = requests.post(url, json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())
