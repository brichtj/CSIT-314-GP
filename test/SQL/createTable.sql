DROP TABLE IF EXISTS "ServiceLikes" CASCADE;
DROP TABLE IF EXISTS "Views" CASCADE;
DROP TABLE IF EXISTS "Matches" CASCADE;
DROP TABLE IF EXISTS "Service" CASCADE;
DROP TABLE IF EXISTS "Category" CASCADE;
DROP TABLE IF EXISTS "HomeOwner" CASCADE;
DROP TABLE IF EXISTS "Cleaner" CASCADE;
DROP TABLE IF EXISTS "UserAdmin" CASCADE;
DROP TABLE IF EXISTS "PlatformManagement" CASCADE;
DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS "UserProfile" CASCADE;

CREATE TABLE "UserProfile"(
  "UserProfileID" integer PRIMARY KEY,
  "Name" varchar,
  "Privilages" varchar
);

CREATE TABLE "user" (
  "UserID" integer PRIMARY KEY,
  "Username" varchar NOT NULL,
  "UserProfileID" integer NOT NULL,
  "Email" varchar NOT NULL,
  "Phone" varchar,
  "Password" varchar NOT NULL,
  "IsActive" boolean NOT NULL
);

CREATE TABLE "HomeOwner" (
  "HomeOwnerID" integer PRIMARY KEY,
  "Address" varchar NOT NULL
);

CREATE TABLE "Cleaner" (
  "CleanerID" integer PRIMARY KEY,
  "Experience" float NOT NULL
);

CREATE TABLE "UserAdmin" (
  "AdminID" integer PRIMARY KEY
);

CREATE TABLE "PlatformManagement" (
  "ManagerID" integer PRIMARY KEY
);

CREATE TABLE "Service" (
  "ServiceID" integer PRIMARY KEY,
  "CategoryID" integer NOT NULL,
  "Title" varchar NOT NULL,
  "Description" text,
  "DatePosted" timestamp NOT NULL,
  "CleanerID" integer NOT NULL,
  "LikeCount" integer NOT NULL,
  "ViewCount" integer NOT NULL,
  "MatchCount" integer NOT NULL,
  "Price" float NOT NULL
);

CREATE TABLE "ServiceLikes" (
  "ServiceID" integer NOT NULL,
  "HomeOwnerID" integer NOT NULL
);

CREATE TABLE "Category" (
  "CategoryID" integer PRIMARY KEY,
  "Title" varchar NOT NULL,
  "Description" text
);

CREATE TABLE "Views" (
  "HomeOwnerID" integer NOT NULL,
  "ServiceID" integer NOT NULL
);

CREATE TABLE "Matches" (
  "ServiceID" integer NOT NULL,
  "HomeOwnerID" integer NOT NULL,
  "Price" float NOT NULL,
  "Date" timestamp NOT NULL,
  "Rating" Integer
);

CREATE UNIQUE INDEX ON "ServiceLikes" ("ServiceID", "HomeOwnerID");

CREATE UNIQUE INDEX ON "Views" ("ServiceID", "HomeOwnerID");

COMMENT ON TABLE "Service" IS 'Service can only be listed by Cleaners, so limit to UserID that has userprofileID of cleaner, LikeCount is so we dont have to aggregate for every service post';

COMMENT ON TABLE "ServiceLikes" IS 'AutoIncremented LikeID, ServiceLikes can only be owned by homeowner';

ALTER TABLE "user" ADD FOREIGN KEY ("UserProfileID") REFERENCES "UserProfile" ("UserProfileID") ON DELETE CASCADE;

ALTER TABLE "HomeOwner" ADD FOREIGN KEY ("HomeOwnerID") REFERENCES "user" ("UserID") ON DELETE CASCADE;

ALTER TABLE "Cleaner" ADD FOREIGN KEY ("CleanerID") REFERENCES "user" ("UserID") ON DELETE CASCADE;

ALTER TABLE "UserAdmin" ADD FOREIGN KEY ("AdminID") REFERENCES "user" ("UserID") ON DELETE CASCADE;

ALTER TABLE "PlatformManagement" ADD FOREIGN KEY ("ManagerID") REFERENCES "user" ("UserID") ON DELETE CASCADE;

ALTER TABLE "Matches" ADD FOREIGN KEY ("HomeOwnerID") REFERENCES "HomeOwner" ("HomeOwnerID") ON DELETE CASCADE;

ALTER TABLE "Views" ADD FOREIGN KEY ("HomeOwnerID") REFERENCES "HomeOwner" ("HomeOwnerID") ON DELETE CASCADE;

ALTER TABLE "ServiceLikes" ADD FOREIGN KEY ("HomeOwnerID") REFERENCES "HomeOwner" ("HomeOwnerID") ON DELETE CASCADE;

ALTER TABLE "Service" ADD FOREIGN KEY ("CleanerID") REFERENCES "Cleaner" ("CleanerID") ON DELETE CASCADE;

ALTER TABLE "ServiceLikes" ADD FOREIGN KEY ("ServiceID") REFERENCES "Service" ("ServiceID") ON DELETE CASCADE;

ALTER TABLE "Matches" ADD FOREIGN KEY ("ServiceID") REFERENCES "Service" ("ServiceID") ON DELETE CASCADE;

ALTER TABLE "Views" ADD FOREIGN KEY ("ServiceID") REFERENCES "Service" ("ServiceID") ON DELETE CASCADE;

ALTER TABLE "Service" ADD FOREIGN KEY ("CategoryID") REFERENCES "Category" ("CategoryID") ON DELETE CASCADE;
