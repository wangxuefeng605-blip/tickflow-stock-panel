import sqlite3


DB_NAME = "stock_history.db"


def get_connection():

    return sqlite3.connect(DB_NAME)



def init_db():

    conn = get_connection()

    cursor = conn.cursor()


    # 每日AI排名

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS daily_rank(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            code TEXT,

            name TEXT,

            score REAL

        )
        """
    )


    # 回测统计

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS backtest_result(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            period TEXT,

            avg_return REAL,

            win_rate REAL,

            max_drawdown REAL

        )
        """
    )


    conn.commit()

    conn.close()



if __name__ == "__main__":

    init_db()

    print("数据库初始化完成")