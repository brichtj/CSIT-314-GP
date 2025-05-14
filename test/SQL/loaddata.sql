\copy "UserProfile" ("UserProfileID", "Name", "Privilege", "Is_Active") FROM 'TableData/UserProfile.csv' DELIMITER ',' CSV HEADER;
\copy "user" ("UserID", "Username", "Email", "Phone", "Password", "IsActive", "UserProfileID", "Address", "Experience") FROM 'TableData/User.csv' DELIMITER ',' CSV HEADER;
\copy "Category" ("CategoryID", "Title", "Description", "Is_Active") FROM 'TableData/Category.csv' DELIMITER ',' CSV HEADER;
\copy "Service"("ServiceID", "CategoryID", "Title", "Description", "DatePosted", "CleanerID", "LikeCount", "ViewCount", "MatchCount", "price", "ImageLink") FROM 'TableData/Service.csv' DELIMITER ',' CSV HEADER;


\copy "Matches"("ServiceID", "HomeOwnerID", "Price", "Date", "Rating") FROM 'TableData/Matches.csv' DELIMITER ',' CSV HEADER;
\copy "Shortlist_Record"("ServiceID", "HomeOwnerID") FROM 'TableData/Shortlist.csv' DELIMITER ',' CSV HEADER;
\copy "Views"("HomeOwnerID", "ServiceID") FROM 'TableData/Views.csv' DELIMITER ',' CSV HEADER;