import random
import csv
from SQL.DatabaseConnection import DB

db = DB()
cur = db.getCursor()
cur.execute("SELECT \"UserID\" FROM \"user\" WHERE \"UserProfileID\" = 3;")
home_owner_ids = [row[0] for row in cur.fetchall()]
cur.execute("SELECT \"ServiceID\" FROM \"Service\"")
service_ids = [row[0] for row in cur.fetchall()]

unique_views = set()

while len(unique_views) < 100:
    ho_id = random.choice(home_owner_ids)
    svc_id = random.choice(service_ids)
    unique_views.add((ho_id, svc_id))

with open('Views.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['HomeOwnerID', 'ServiceID'])
    writer.writerows(list(unique_views))
