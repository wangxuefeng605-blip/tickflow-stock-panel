"""
AI_Top10 v17.0

Factor Cache Module

功能:

1. 因子缓存
2. JSON高速读取
3. 自动更新
4. 支持Rolling IC
5. 支持Alpha Score

"""

import os
import json
import time
from datetime import datetime



# ==========================
# 缓存路径
# ==========================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


CACHE_DIR = os.path.join(
    BASE_DIR,
    "data",
    "cache",
    "factors"
)


os.makedirs(
    CACHE_DIR,
    exist_ok=True
)



# ==========================
# 参数
# ==========================


CACHE_EXPIRE_DAYS = 1



# ==========================
# 文件
# ==========================


def normalize_code(code):

    return str(code).zfill(6)




def get_factor_file(code):

    code = normalize_code(code)

    return os.path.join(
        CACHE_DIR,
        f"{code}.json"
    )




# ==========================
# 保存
# ==========================


def save_factor(
        code,
        factors
):


    code = normalize_code(code)


    data = {

        "code":code,

        "update":
            datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S"),

        "factors":factors

    }



    file=get_factor_file(code)



    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



# ==========================
# 读取
# ==========================


def load_factor(code):


    file=get_factor_file(code)



    if not os.path.exists(file):

        return None



    try:


        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:


            data=json.load(f)



        return data



    except Exception as e:


        print(
            "读取因子失败:",
            code,
            e
        )


        return None




# ==========================
# 判断是否过期
# ==========================


def factor_expired(data):


    if data is None:

        return True



    try:


        update_time=datetime.strptime(
            data["update"],
            "%Y-%m-%d %H:%M:%S"
        )


        diff=(
            datetime.now()
            -
            update_time
        ).days



        return diff >= CACHE_EXPIRE_DAYS



    except:


        return True




# ==========================
# 核心接口
# ==========================


def get_factor(
        code,
        calculator=None,
        refresh=False
):


    """
    获取股票因子


    calculator:

    外部传入:

        stock_factor.calculate()


    """


    code=normalize_code(code)



    data=load_factor(code)



    if (
        data is not None
        and
        not factor_expired(data)
        and
        not refresh
    ):


        return data["factors"]




    # ==================
    # 重新计算
    # ==================


    if calculator is None:


        return None



    try:


        factors=calculator(code)



        if factors:


            save_factor(
                code,
                factors
            )


            return factors



    except Exception as e:


        print(
            f"{code} 因子计算失败:",
            e
        )



    return None





# ==========================
# 批量缓存
# ==========================


def preload_factor(
        stock_list,
        calculator
):


    total=len(stock_list)



    for i,code in enumerate(stock_list,1):


        print(
            f"[{i}/{total}] 因子:"
            f"{code}"
        )



        get_factor(
            code,
            calculator
        )





# ==========================
# 删除缓存
# ==========================


def clear_factor(code):


    file=get_factor_file(code)



    if os.path.exists(file):

        os.remove(file)





# ==========================
# 测试
# ==========================


if __name__=="__main__":


    test_factor={

        "momentum":0.88,

        "trend":1,

        "volume_factor":0.76,

        "quality":0.65,

        "growth":0.55,

        "volatility":0.12

    }



    save_factor(
        "000001",
        test_factor
    )



    print(
        load_factor(
            "000001"
        )
    )