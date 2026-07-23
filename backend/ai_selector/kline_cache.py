import os
import pandas as pd


CACHE_DIR="kline_cache"



def load_kline(code):


    file=f"{CACHE_DIR}/{code}.csv"


    if not os.path.exists(file):

        return None



    try:

        df=pd.read_csv(
            file
        )


        return df


    except:


        return None