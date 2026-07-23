import sqlite3


conn = sqlite3.connect(
    "stock_history.db"
)


cursor = conn.cursor()


rows = cursor.execute(

"""
SELECT *
FROM daily_rank
ORDER BY id DESC
LIMIT 20

"""

).fetchall()



for row in rows:

    print(row)


conn.close()