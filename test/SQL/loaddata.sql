INSERT INTO "UserProfile" ("UserProfileID", "Name", "Privilages")
VALUES
  (1, 'Admin', 'Full Access'),
  (2, 'Cleaner', 'Service Management'),
  (3, 'HomeOwner', 'Service Browsing'),
  (4, 'Manager', 'Platform Oversight');

DO $$
BEGIN
  FOR i IN 1..100 LOOP
    INSERT INTO "user" ("UserID", "Username", "UserProfileID", "Email", "Phone", "Password", "IsActive")
    VALUES (
      i,
      'user' || i,
      CASE 
        WHEN i BETWEEN 1 AND 25 THEN 1         -- Admin
        WHEN i BETWEEN 26 AND 50 THEN 2        -- Cleaner
        WHEN i BETWEEN 51 AND 75 THEN 3        -- HomeOwner
        ELSE 4                                 -- Manager
      END,
      'user' || i || '@example.com',
      '012345678' || i,
      'password' || i,
      TRUE
    );
  END LOOP;
END $$;

INSERT INTO "Cleaner" ("CleanerID", "Experience")
SELECT i, (random() * 10)::numeric(3,1)
FROM generate_series(26, 50) AS i;

INSERT INTO "HomeOwner" ("HomeOwnerID", "Address")
SELECT i, 'Address ' || i
FROM generate_series(51, 75) AS i;

INSERT INTO "PlatformManagement" ("ManagerID")
SELECT generate_series(76, 100);

INSERT INTO "Category" ("CategoryID", "Title", "Description")
SELECT i, 'Category ' || i, 'Description for category ' || i
FROM generate_series(1, 10) AS i;

INSERT INTO "Service" (
  "ServiceID", "CategoryID", "Title", "Description", "DatePosted", 
  "CleanerID", "LikeCount", "ViewCount", "MatchCount", "Price"
)
SELECT
  i,                                       -- ServiceID
  (i % 10) + 1,                            -- CategoryID (1 to 10)
  'Service ' || i,                         -- Title
  'Description for service ' || i,        -- Description
  NOW() - (i || ' days')::interval,       -- DatePosted (random past date)
  25 + (i % 25) + 1,                       -- CleanerID (26–50)
  (random() * 100)::int,                  -- LikeCount
  (random() * 200)::int,                  -- ViewCount
  (random() * 50)::int,                   -- MatchCount
  (random() * 500)::numeric(5,2) + 50     -- Price (random between 50–550)
FROM generate_series(1, 50) AS i;

INSERT INTO "ServiceLikes" ("ServiceID", "HomeOwnerID")
SELECT
  (random() * 49 + 1)::int,         -- ServiceID (1–50)
  (random() * 24 + 51)::int        -- HomeOwnerID (51–75)
FROM generate_series(1, 100);

INSERT INTO "Matches" ("ServiceID", "HomeOwnerID", "Price", "Date", "Rating")
SELECT
  (random() * 49 + 1)::int,               -- ServiceID
  (random() * 24 + 51)::int,              -- HomeOwnerID
  (random() * 500)::numeric(5,2) + 50,    -- Price
  NOW() - (i || ' days')::interval,       -- Date
  (random() * 5 + 1)::int                 -- Rating (1–5)
FROM generate_series(1, 50) AS i;
