import os
import pandas as pd


RESULT="scan_result.csv"



def get_finished():

    if not os.path.exists(
        RESULT
    ):
        return set()


    df=pd.read_csv(
        RESULT,
        dtype={
            "code":str
        }
    )


    return set(
        df.code
    )
