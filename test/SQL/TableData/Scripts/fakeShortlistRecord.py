import random
from faker import Faker
import csv
from SQL.DatabaseConnection import DB

db = DB()
cur = db.getCursor()
cur.execute("SELECT \"UserID\" FROM \"user\" WHERE \"UserProfileID\" = 3;")
home_owner_ids = [row[0] for row in cur.fetchall()]
cur.execute("SELECT \"ServiceID\" FROM \"Service\";")
service_ids = [row[0] for row in cur.fetchall()]

fake = Faker()

shortlist_records = set()

while len(shortlist_records) < 100:
    service_id = random.choice(service_ids)
    home_owner_id = random.choice(home_owner_ids) 

    shortlist_records.add((service_id, home_owner_id)) 

with open('Shortlist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ServiceID", "HomeOwnerID"])
    writer.writerows(shortlist_records)

