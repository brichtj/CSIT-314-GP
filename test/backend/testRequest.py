import requests

url = {
    "login": "http://localhost:5000/login",
    "logout": "http://localhost:5000/logout"
}

datas = {
    "Email": "user1@example.com",
    "Password": "user123",
    "UserProfileID": 0
}, {
    "Email": "user2@example.com",
    "Password": "user123",
    "UserProfileID": 0
}, {
    "Email": "user26@example.com",
    "Password": "user123",
    "UserProfileID": 1
}, {
    "Email": "user27@example.com",
    "Password": "user123",
    "UserProfileID": 1
}, {
    "Email": "user51@example.com",
    "Password": "user123",
    "UserProfileID": 2
}, {
    "Email": "user52@example.com",
    "Password": "user123",
    "UserProfileID": 2
}, {
    "Email": "user76@example.com",
    "Password": "user123",
    "UserProfileID": 3
}, {
    "Email": "user77@example.com",
    "Password": "user123",
    "UserProfileID": 3
}

for data in datas:
    response = requests.post(url["login"], json=data)
    print(response.status_code)
    print(response.json())


response = requests.post(url["logout"])
print(response.status_code)
print(response.json())
