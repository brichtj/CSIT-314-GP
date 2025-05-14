import random
from faker import Faker
import csv
from datetime import datetime
from SQL.DatabaseConnection import DB

db = DB()
cur = db.getCursor()
cur.execute("SELECT \"UserID\" FROM \"user\" WHERE \"UserProfileID\" = 3;")
home_owner_ids = [row[0] for row in cur.fetchall()]
cur.execute("SELECT \"ServiceID\" FROM \"Service\"")
service_ids = [row[0] for row in cur.fetchall()]

fake = Faker()

reviews = []
unique_pairs = set()

while len(reviews) < 100:
    service_id = random.choice(service_ids)
    home_owner_id = random.choice(home_owner_ids)
    
    if (service_id, home_owner_id) in unique_pairs:
        continue
    
    unique_pairs.add((service_id, home_owner_id))
    
    price = round(random.uniform(20.0, 100.0), 2)
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2025, 12, 31)
    date = fake.date_between(start_date=start_date, end_date=end_date)
    rating = random.randint(1, 5)

    reviews.append([service_id, home_owner_id, price, date, rating])


with open("Matches.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ServiceID", "HomeOwnerID", "Price", "Date", "Rating"])
    writer.writerows(reviews)