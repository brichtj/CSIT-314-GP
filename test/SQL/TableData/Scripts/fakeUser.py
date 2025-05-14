import csv
import random
import faker
from faker import Faker

fake = faker.Faker()

user_profile_ids = [1, 2, 3, 4]
user_data = []

email_domains = ['gmail.com', 'yahoo.com',
                 'outlook.com', 'hotmail.com', 'icloud.com']

phone_formats = [
    '+1-###-###-####',
    '+44-7####-######',
    '+60-1#-####-####',
    '+91-9####-#####',
    '+49-1##-######',
]


for user_id in range(1, 201):
    username = fake.user_name()
    domain = random.choice(email_domains)
    email = f"{username}{random.randint(1, 999)}@{domain}"

    phone_format = random.choice(phone_formats)
    phone = fake.numerify(phone_format)

    password = f"password_{user_id}"
    is_active = random.choice([True, False])
    profile_id = user_profile_ids[(user_id - 1) % 4]

    address = None
    if profile_id == 3:
        address = fake.address().replace("\n", " ")

    experience = None
    if profile_id == 2:
        experience = f"{random.randint(1, 10)}"

    user_data.append([
        user_id, username, email, phone, password, is_active, profile_id, address, experience
    ])

with open('User.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['UserID', 'Username', 'Email', 'Phone', 'Password',
                    'IsActive', 'UserProfileID', 'Address', 'Experience'])
    writer.writerows(user_data)
