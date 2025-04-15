DROP TABLE IF EXISTS Shortlist_Record CASCADE;
DROP TABLE IF EXISTS Matched_History CASCADE;
DROP TABLE IF EXISTS Service CASCADE;
DROP TABLE IF EXISTS Category CASCADE;
DROP TABLE IF EXISTS UserAdmin CASCADE;
DROP TABLE IF EXISTS Cleaner CASCADE;
DROP TABLE IF EXISTS HomeOwner CASCADE;
DROP TABLE IF EXISTS PlatformManagement CASCADE;
DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS Login_Details CASCADE;
DROP TYPE IF EXISTS user_profile CASCADE;

CREATE TYPE user_profile AS ENUM ('UserAdmin', 'Cleaner', 'HomeOwner', 'PlatformManagement');

-- Table: Login_Details
CREATE TABLE Login_Details (
    UserProfile user_profile NOT NULL, -- Use the defined ENUM type here
    Email VARCHAR(255) PRIMARY KEY NOT NULL,
    Password VARCHAR(255) UNIQUE NOT NULL
);

-- Table: User
CREATE TABLE "user" (
    UserID VARCHAR(255) PRIMARY KEY NOT NULL,
    Username VARCHAR(255) UNIQUE NOT NULL,
    UserProfile user_profile NOT NULL, -- Use the defined ENUM type here
    Email VARCHAR(255) UNIQUE NOT NULL,
	Phone VARCHAR(255) UNIQUE,
    DOB DATE,
	FOREIGN KEY (Email) REFERENCES Login_Details(Email) ON DELETE CASCADE
);

-- Table: UserAdmin
CREATE TABLE UserAdmin (
    UserID VARCHAR(255) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UserID) REFERENCES "user"(UserID) ON DELETE CASCADE
);

-- Table: Cleaner
CREATE TABLE Cleaner (
    UserID VARCHAR(255) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UserID) REFERENCES "user"(UserID) ON DELETE CASCADE
);

-- Table: HomeOwner
CREATE TABLE HomeOwner (
    UserID VARCHAR(255) PRIMARY KEY NOT NULL,
    Address TEXT NOT NULL,
    FOREIGN KEY (UserID) REFERENCES "user"(UserID) ON DELETE CASCADE
);

-- Table: PlatformManagement
CREATE TABLE PlatformManagement (
    UserID VARCHAR(255) PRIMARY KEY NOT NULL,
    FOREIGN KEY (UserID) REFERENCES "user"(UserID) ON DELETE CASCADE
);

-- Table: Category
CREATE TABLE Category (
    CategoryID VARCHAR(255) PRIMARY KEY NOT NULL,
    Description TEXT
);

-- Table: Service
CREATE TABLE Service (
    ServiceID VARCHAR(255) PRIMARY KEY NOT NULL,
    Title TEXT NOT NULL,
    UserID VARCHAR(255) NOT NULL,
	CategoryID VARCHAR(255) NOT NULL,
	Price DECIMAL(8,2) NOT NULL,
    Description TEXT,
    Views INT DEFAULT 0,
    Shortlisted INT DEFAULT 0,
    FOREIGN KEY (UserID) REFERENCES Cleaner(UserID),
	FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)    
);

-- Table: Shortlist_Record
CREATE TABLE Shortlist_Record (
    UserID VARCHAR(255) NOT NULL,
    ServiceID VARCHAR(255) NOT NULL,
	FOREIGN KEY (UserID) REFERENCES HomeOwner(UserID) ON DELETE CASCADE,
	FOREIGN KEY (ServiceID) REFERENCES Service(ServiceID) ON DELETE CASCADE,
	PRIMARY KEY (UserID, ServiceID)
);

-- Table: Matched_History
CREATE TABLE Matched_History (
    HistoryID VARCHAR(255) PRIMARY KEY NOT NULL,
    Date DATE NOT NULL,
    HOUserID VARCHAR(255) NOT NULL,
    ServiceID VARCHAR(255) NOT NULL,
	FOREIGN KEY (HOUserID) REFERENCES HomeOwner(UserID) ON DELETE CASCADE,
	FOREIGN KEY (ServiceID) REFERENCES Service(ServiceID) ON DELETE CASCADE
);