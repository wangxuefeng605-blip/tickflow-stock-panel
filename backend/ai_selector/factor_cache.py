import os
import pandas as pd
_FACTOR_CACHE = {}

_FACTOR_HIT = 0
_FACTOR_MISS = 0


CACHE_FILE="factor_cache.csv"



def load_factor(code):

    global _FACTOR_HIT
    global _FACTOR_MISS


    code = str(code)


    # memory hit

    if code in _FACTOR_CACHE:

        _FACTOR_HIT += 1

        return _FACTOR_CACHE[code]



    _FACTOR_MISS += 1



    if not os.path.exists(
        CACHE_FILE
    ):

        return None



    try:

        df = pd.read_csv(
            CACHE_FILE,
            dtype={
                "code": str
            }
        )


        row = df[
            df.code == code
        ]


        if len(row):

            factor = row.iloc[0].to_dict()


            _FACTOR_CACHE[code] = factor


            return factor



    except Exception:

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
    _FACTOR_CACHE[str(code)] = factor
def factor_cache_report():

    total = (
        _FACTOR_HIT
        +
        _FACTOR_MISS
    )


    rate = 0

    if total:
        rate = (
            _FACTOR_HIT
            /
            total
            *
            100
        )


    print(
        "================================"
    )

    print(
        "Factor Cache Report"
    )

    print(
        f"hit  : {_FACTOR_HIT}"
    )

    print(
        f"miss : {_FACTOR_MISS}"
    )

    print(
        f"rate : {rate:.2f}%"
    )

    print(
        "================================"
    )