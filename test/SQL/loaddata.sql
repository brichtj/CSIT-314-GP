INSERT INTO "User" (
    "UserID",
    "Username",
    "UserProfile",
    "Email",
    "Phone",
    "Password",
    "IsActive"
)
SELECT i,
       'user_' || i,
       (CASE
            WHEN i <= 25 THEN 'Admin'
            WHEN i <= 50 THEN 'Cleaner'
            WHEN i <= 75 THEN 'HomeOwner'
            ELSE 'Manager'
        END)::"UserProfile",
       'user' || i || '@example.com',
       '012345678' || (i % 10),
       'user123',
       (i % 2 = 0)
FROM generate_series(1, 100) AS s(i);

INSERT INTO "HomeOwner" ("HomeOwnerID",
                         "Address")
SELECT i,
       'Address ' || i
FROM generate_series(51, 75) AS i;


INSERT INTO "Cleaner" ("CleanerID",
                       "Experience")
SELECT i,
       round((random() * 10)::numeric, 1)
FROM generate_series(26, 50) AS i;


INSERT INTO "UserAdmin" ("AdminID")
SELECT i
FROM generate_series(1, 25) AS i;


INSERT INTO "PlatformManagement" ("ManagerID")
SELECT i
FROM generate_series(76, 100) AS i;


INSERT INTO "Category" ("CategoryID",
                        "Title",
                        "Description")
SELECT i,
       'Category ' || i,
       'Description for category ' || i
FROM generate_series(1, 100) AS i;


INSERT INTO "Service" ( "ServiceID",
                        "CategoryID",
                        "Title",
                        "Description",
                        "DatePosted",
                        "CleanerID",
                        "LikeCount",
                        "ViewCount",
                        "MatchCount",
                        "Price")
SELECT i,
       (i % 100) + 1,
       'Service ' || i,
       'Service description ' || i,
       now() - (i || ' days')::interval, ((i - 1) % 25 + 26), -- Cleaners 26 to 50
 (random() * 100)::int,
 (random() * 500)::int,
 (random() * 30)::int,
 round((random() * 100)::numeric, 2)
FROM generate_series(1, 100) AS i;


INSERT INTO "ServiceLikes" ("ServiceID",
                            "HomeOwnerID")
SELECT (i % 100) + 1, ((i - 1) % 25 + 51)
FROM generate_series(1, 100) AS i;


INSERT INTO "Views" ("HomeOwnerID",
                     "ServiceID")
SELECT ((i - 1) % 25 + 51), (i % 100) + 1
FROM generate_series(1, 100) AS i;


INSERT INTO "Matches" ("ServiceID",
                       "HomeOwnerID",
                       "Price",
                       "Date",
                       "Rating")
SELECT (i % 100) + 1, ((i - 1) % 25 + 51), round((random() * 100)::numeric, 2),
                                           now() - (i || ' days')::interval,
                                           (random() * 5)::int
FROM generate_series(1, 100) AS i;

