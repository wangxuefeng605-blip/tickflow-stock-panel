import sqlite3
from datetime import datetime

from database import get_connection



def save_history(results):


    conn = get_connection()

    cursor = conn.cursor()


    today = datetime.now().strftime(
        "%Y-%m-%d"
    )


    for stock in results:


        cursor.execute(
        """
        INSERT INTO daily_rank
        (
        date,
        code,
        name,
        score
        )

        VALUES
        (?,?,?,?)

        """,

        (
            today,
            stock["code"],
            stock["name"],
            stock["score"]
        )

        )


    conn.commit()

    conn.close()


    print(
        "历史排名保存成功"
    )