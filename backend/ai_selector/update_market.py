from stock_pool import get_stock_pool
from stock_factor import get_history



stocks=get_stock_pool()



for code in stocks:


    try:

        get_history(code)


        print(
            code,
            "更新完成"
        )


    except:

        pass