import os
import pandas as pd


CACHE_DIR="history_cache"


os.makedirs(
    CACHE_DIR,
    exist_ok=True
)



def cache_file(code):

    return os.path.join(
        CACHE_DIR,
        f"{code}.csv"
    )



def load_history(code):

    file=cache_file(code)

    if os.path.exists(file):

        try:

            df=pd.read_csv(
                file
            )

            return df

        except:

            return None


    return None




def save_history(code,df):

    file=cache_file(code)

    df.to_csv(
        file,
        index=False
    )