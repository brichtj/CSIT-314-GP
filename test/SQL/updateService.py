from DatabaseConnection import DB

db =DB()
conn = db.getConn()
cur = conn.cursor()

cur.execute("""
            SELECT "ServiceID"
            FROM "Service"
            """)

rows = cur.fetchall()

for row in rows:
    service_id = row[0]

    cur.execute('SELECT COUNT(*) FROM "Views" WHERE "ServiceID" = %s', (service_id,))
    view_count = cur.fetchone()[0]

    cur.execute('SELECT COUNT(*) FROM "Matches" WHERE "ServiceID" = %s', (service_id,))
    match_count = cur.fetchone()[0]

    cur.execute('SELECT COUNT(*) FROM "Shortlist_Record" WHERE "ServiceID" = %s', (service_id,))
    like_count = cur.fetchone()[0]

    cur.execute("""
                    UPDATE "Service"
                    SET "ViewCount" = %s,
                        "MatchCount" = %s,
                        "LikeCount" = %s
                    WHERE "ServiceID" = %s
                """, (view_count, match_count, like_count, service_id))

conn.commit()
