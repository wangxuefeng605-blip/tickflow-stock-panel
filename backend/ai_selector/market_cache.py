import sqlite3
import pandas as pd



DB="stock_history.db"



# =========================
# 保存行情
# =========================

def save_history(code,df):


    conn=sqlite3.connect(DB)


    table="stock_"+code



    df.to_sql(
        table,
        conn,
        if_exists="replace",
        index=False
    )


    conn.close()




# =========================
# 读取行情
# =========================

def load_history(code):


    conn=sqlite3.connect(DB)


    table="stock_"+code


    try:


        df=pd.read_sql(
            f"select * from {table}",
            conn
        )


    except:


        df=None



    conn.close()


    return df