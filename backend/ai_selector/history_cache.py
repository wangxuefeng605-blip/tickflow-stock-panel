import os
import pandas as pd

from kline_cache import load_kline


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
    from kline_cache import load_kline


def get_history(code):

    data = load_history(code)


    if data is not None:
        return data


    data = load_kline(code)


    if data is not None:
        save_history(
            code,
            data
        )


    return data