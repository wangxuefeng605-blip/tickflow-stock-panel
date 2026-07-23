import os

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)

os.environ["NO_PROXY"] = "*"


import akshare as ak



def get_stock_list():

    """
    获取A股股票列表
    """

    try:

        df = ak.stock_info_a_code_name()


    except Exception as e:

        print(
            "股票列表接口失败:",
            e
        )

        return []


    stocks=[]


    for _,row in df.iterrows():

        stocks.append({

            "code":row["code"],

            "name":row["name"]

        })


    return stocks



if __name__=="__main__":


    stocks=get_stock_list()


    print(
        "股票数量:",
        len(stocks)
    )


    print(
        stocks[:10]
    )