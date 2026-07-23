import pandas as pd
import numpy as np



FACTORS=[

"momentum",
"volume_factor",
"trend",
"value",
"quality",
"growth",
"volatility",
"liquidity"

]



def calc_ic(df):


    result={}


    future=df["future_return"]



    for factor in FACTORS:


        if factor not in df:

            continue


        ic=df[factor].corr(
            future
        )


        result[factor]=round(
            ic,
           4
        )


    return result




def rolling_ic(
    history,
    window=60
):


    data=[]


    for i in range(
        window,
        len(history)
    ):


        sample=history.iloc[
            i-window:i
        ]


        data.append(
            calc_ic(sample)
        )


    return pd.DataFrame(data)