import csv
import random
from datetime import datetime
from faker import Faker
from SQL.DatabaseConnection import DB

fake = Faker()

db = DB()
cur = db.getCursor()
cur.execute("SELECT \"UserID\" FROM \"user\" WHERE \"UserProfileID\" = 2;")
cleaner_ids = [row[0] for row in cur.fetchall()]

base_categories = [
    (1, "General Cleaning", "Standard cleaning for homes, offices, and other spaces"),
    (2, "Washing", "Includes washing of clothes, linens, and other fabric items"),
    (3, "Laundry Services",
     "Complete laundry services including washing, drying, and folding"),
    (4, "Polishing", "Polishing of furniture, floors, and other surfaces to restore shine"),
    (5, "Sanitization",
     "Sanitizing high-touch areas and surfaces to prevent the spread of germs"),
    (6, "Deep Cleaning", "Thorough cleaning of all surfaces, including hard-to-reach areas"),
    (7, "Disinfection", "Applying disinfectants to kill germs and viruses on all surfaces"),
    (8, "Surface Cleaning",
     "General cleaning of all types of surfaces including tables, counters, and shelves"),
    (9, "Upholstery Cleaning",
     "Cleaning and maintaining sofas, chairs, and other fabric-covered furniture"),
    (10, "Floor Care", "Cleaning, waxing, and polishing of all floor types (wood, tile, carpet)"),
    (11, "Window Cleaning",
     "Exterior and interior window cleaning to remove dirt and smudges"),
    (12, "Dusting", "Removing dust from all surfaces, including furniture, shelves, and baseboards"),
    (13, "Trash Removal", "Disposing of trash and recyclables from homes or offices"),
    (14, "Pressure Washing",
     "Using high-pressure water to clean exterior surfaces like driveways and walls"),
    (15, "Organizing & Decluttering",
     "Sorting, organizing, and decluttering spaces such as closets and rooms"),
    (16, "Home Maintenance Cleaning",
     "General upkeep cleaning of homes, ensuring everything stays tidy and organized"),
    (17, "Carpet and Rug Care",
     "Vacuuming, shampooing, and restoring carpets and rugs to their original state"),
    (18, "Gutter Cleaning",
     "Cleaning and clearing debris from roof gutters to prevent blockages"),
    (19, "Post-Construction Cleaning",
     "Removing dust, debris, and materials left behind after construction work"),
    (20, "Move-In/Move-Out Cleaning",
     "Thorough cleaning services for homes when moving in or out")
]

adjectives = [
    "Premium", "Express", "Deep", "Eco-Friendly", "Basic", "Quick", "Intensive",
    "Gentle", "Affordable", "Top-Rated", "Deluxe", "Reliable", "Thorough", "Complete"
]

used_titles = set()
services = []
i = 1

while len(services) < 100:
    category = random.choice(base_categories)
    adj = random.choice(adjectives)
    title = f"{adj} {category[1]}"
    if title in used_titles:
        continue
    used_titles.add(title)

    description = category[2]
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2025, 12, 31)
    date_posted = fake.date_between(start_date=start_date, end_date=end_date)
    cleaner_id = random.choice(cleaner_ids)
    like_count = 0
    view_count = 0
    match_count = 0
    price = round(random.uniform(20, 150), 2)
    image_link = f"https://example.com/images/{category[1].lower().replace(' ', '_')}.jpg"

    services.append([i, category[0], title, description, date_posted, cleaner_id,
                     like_count, view_count, match_count, price, image_link])
    i += 1

with open("Service.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ServiceID", "CategoryID", "Title", "Description", "DatePosted", "CleanerID",
                     "LikeCount", "ViewCount", "MatchCount", "price", "ImageLink"])
    writer.writerows(services)
