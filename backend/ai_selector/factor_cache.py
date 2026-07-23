import os
import pandas as pd


CACHE_FILE="factor_cache.csv"



def load_factor(code):


    if not os.path.exists(
        CACHE_FILE
    ):

        return None



    try:

        df=pd.read_csv(
            CACHE_FILE,
            dtype={
                "code":str
            }
        )


        row=df[
            df.code==str(code)
        ]


        if len(row):

            return row.iloc[0].to_dict()


    except:

        return None



    return None





def save_factor(
    code,
    factor
):


    new=pd.DataFrame(
        [
            factor
        ]
    )


    if os.path.exists(
        CACHE_FILE
    ):

        try:

            old=pd.read_csv(
                CACHE_FILE,
                dtype={
                    "code":str
                }
            )


        except:

            old=pd.DataFrame()


        old=old[
            old.code!=str(code)
        ]


        df=pd.concat(
            [
                old,
                new
            ],
            ignore_index=True
        )


    else:

        df=new



    df.to_csv(
        CACHE_FILE,
        index=False,
        encoding="utf-8-sig"
    )