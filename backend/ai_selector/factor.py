def get_factors(
    close_price,
    close_price_20,
    volume_today,
    volume_avg20,
    MA5,
    MA20
):

    momentum = (
        close_price / close_price_20
    )


    volume_factor = (
        volume_today / volume_avg20
    )


    trend = (
        1 if MA5 > MA20 else 0
    )


    factors = {

        "momentum": momentum,

        "volume_factor": volume_factor,

        "trend": trend

    }


    return factors



# 测试
if __name__ == "__main__":


    result = get_factors(

        close_price=110,

        close_price_20=100,

        volume_today=1500,

        volume_avg20=1000,

        MA5=108,

        MA20=105
    )


    print("因子结果:")
    print(result)