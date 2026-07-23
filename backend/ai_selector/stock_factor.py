import akshare as ak
import pandas as pd
import numpy as np

from factor_cache import (
    load_factor,
    save_factor
)



# =====================================================
# 获取历史行情
# 腾讯接口
# =====================================================

def get_history(code):


    try:

        if code.startswith("6"):

            symbol="sh"+code

        else:

            symbol="sz"+code



        print(
            "\n正在获取股票:",
            code
        )



        df = ak.stock_zh_a_hist_tx(
            symbol=symbol,
            start_date="20250101",
            end_date="20260714"
        )


        if df is None or df.empty:

            return None



        print(
            "原始字段:",
            df.columns.tolist()
        )



        rename_map={}



        for col in df.columns:


            col=str(col)



            if "日期" in col or col=="date":

                rename_map[col]="date"



            elif "开盘" in col:

                rename_map[col]="open"



            elif "最高" in col:

                rename_map[col]="high"



            elif "最低" in col:

                rename_map[col]="low"



            elif "收盘" in col:

                rename_map[col]="close"



            elif "成交额" in col:

                rename_map[col]="amount"



            elif "成交量" in col:

                rename_map[col]="volume"



        df=df.rename(
            columns=rename_map
        )



        # 腾讯接口没有volume

        if "volume" not in df.columns:


            print(
                "没有成交量字段，自动生成volume"
            )


            if "amount" in df.columns:

                df["volume"] = (
                    df["amount"]
                    /
                    df["close"]
                )


            else:

                return None



        # 类型转换

        for col in [

            "open",
            "high",
            "low",
            "close",
            "amount",
            "volume"

        ]:


            if col in df.columns:


                df[col]=pd.to_numeric(
                    df[col],
                    errors="coerce"
                )



        df=df.dropna()



        required=[

            "close",
            "volume",
            "amount"

        ]



        for c in required:


            if c not in df.columns:

                return None



        print(
            "标准字段:",
            df.columns.tolist()
        )


        return df



    except Exception as e:


        print(
            code,
            "行情异常:",
            e
        )


        return None






# =====================================================
# 动量因子
# =====================================================

def momentum_factor(df):


    close=df["close"]


    if len(close)<30:

        return 0



    score=(

        close.iloc[-1]

        /

        close.iloc[-30]

    )



    # 转收益率

    ret=score-1



    # 防止极端值

    ret=max(
        min(ret,0.5),
        -0.5
    )



    return round(
        float(ret),
        4
    )






# =====================================================
# 成交量因子
# =====================================================

def volume_factor(df):


    v=df["volume"]


    recent=v.tail(5).mean()


    avg=v.tail(30).mean()


    if avg==0:

        return 0



    return round(
        float(recent/avg),
        4
    )






# =====================================================
# 趋势
# =====================================================

def trend_factor(df):


    close=df["close"]


    ma5=close.tail(5).mean()


    ma20=close.tail(20).mean()



    if ma5>ma20:

        return 1


    return 0






# =====================================================
# 波动率
# =====================================================

def volatility_factor(df):


    ret=df["close"].pct_change()



    vol=ret.tail(30).std()



    if pd.isna(vol):

        return 1



    score=1-vol*10


    return round(

        float(max(score,0)),

        4

    )






# =====================================================
# 流动性
# =====================================================

def liquidity_factor(df):


    amount=df["amount"]


    avg=amount.tail(20).mean()



    if avg<=0:

        return 0



    score=avg/1000000



    return round(

        float(min(score/10,1)),

        4

    )






# =====================================================
# 固定因子
# 后续接财务数据
# =====================================================

def value_factor():

    return 0.65



def quality_factor():

    return 0.72



def growth_factor():

    return 0.55






# =====================================================
# 主函数
# =====================================================

def get_stock_factor(code):


    # --------------------
    # 缓存
    # --------------------

    cache=load_factor(code)


    if cache is not None:


        print(
            "因子缓存:",
            code
        )


        return cache




    # --------------------
    # 行情
    # --------------------

    df=get_history(code)



    if df is None:

        return None




    # --------------------
    # 因子计算
    # --------------------

    factor={


        "code":code,


        "momentum":
            momentum_factor(df),



        "volume_factor":
            volume_factor(df),



        "trend":
            trend_factor(df),



        "value":
            value_factor(),



        "quality":
            quality_factor(),



        "growth":
            growth_factor(),



        "volatility":
            volatility_factor(df),



        "liquidity":
            liquidity_factor(df)

    }




    # --------------------
    # 保存缓存
    # --------------------

    save_factor(
        code,
        factor
    )



    return factor




# 兼容旧代码

def get_stock_factors(code):

    return get_stock_factor(code)