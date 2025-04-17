import requests

url = "http://localhost:5000/login"
data1 = {
    "Email": "user1@example.com",
    "Password": "user123",
    "UserProfileID": 0
}
data2 = {
    "Email": "user2@example.com",
    "Password": "user123",
    "UserProfileID": 0
}
data3 = {
    "Email": "user26@example.com",
    "Password": "user123",
    "UserProfileID": 1
}
data4 = {
    "Email": "user27@example.com",
    "Password": "user123",
    "UserProfileID": 1
}
data5 = {
    "Email": "user51@example.com",
    "Password": "user123",
    "UserProfileID": 2
}
data6 = {
    "Email": "user52@example.com",
    "Password": "user123",
    "UserProfileID": 2
}
data7 = {
    "Email": "user76@example.com",
    "Password": "user123",
    "UserProfileID": 3
}
data8 = {
    "Email": "user77@example.com",
    "Password": "user123",
    "UserProfileID": 3
}

response = requests.post(url, json=data8)
print(response.status_code)
print(response.json())
