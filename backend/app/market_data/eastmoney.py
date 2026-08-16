import requests
import pandas as pd


EASTMONEY_URL = (
    "https://82.push2delay.eastmoney.com"
    "/api/qt/clist/get"
)


def get_stock_spot():

    params = {
        "pn": 1,
        "pz": 5000,
        "po": 1,
        "np": 1,

        "ut":
        "bd1d9ddb04089700cf9c27f6f7426281",

        "fltt": 2,
        "invt": 2,

        "fid": "f12",

        "fs":
        "m:0+t:6,"
        "m:0+t:80,"
        "m:1+t:2,"
        "m:1+t:23",

        "fields":
        ",".join(
            [
                "f12",
                "f14",
                "f2",
                "f3",
                "f4",
                "f5",
                "f6"
            ]
        )
    }


    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }


    with requests.Session() as session:

        session.trust_env = False

        response = session.get(
            EASTMONEY_URL,
            params=params,
            headers=headers,
            timeout=10
        )


    response.raise_for_status()


    json_data = response.json()

    print("EASTMONEY RESPONSE KEYS=", json_data.keys())
    print("EASTMONEY DATA KEYS=", json_data.get("data", {}).keys())
    print(
        "EASTMONEY TOTAL=",
        json_data.get("data", {}).get("total")
    )
    print(
        "EASTMONEY DIFF LEN=",
        len(
            json_data.get("data", {}).get("diff", [])
        )
    )

    rows = (
        json_data
        .get("data", {})
        .get("diff", [])
    )


    df = pd.DataFrame(rows)


    df = df.rename(
        columns={
            "f12": "code",
            "f14": "name",
            "f2": "price",
            "f3": "change_pct",
            "f4": "change",
            "f5": "volume",
            "f6": "amount",
        }
    )


    return df
