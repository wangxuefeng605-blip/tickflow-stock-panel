import numpy as np


def risk_check(factor, name):

    risk = []


    # ====================
    # 1. ST股票过滤
    # ====================

    if "ST" in name or "退" in name:

        risk.append(
            "ST风险"
        )



    # ====================
    # 2. 因子数据检查
    # ====================

    if factor is None:

        risk.append(
            "无因子数据"
        )



    # ====================
    # 3. 动量异常
    # ====================

    if factor:

        momentum = factor.get(
            "momentum",
            0
        )


        if momentum <= 0:

            risk.append(
                "动量弱"
            )



    # ====================
    # 4. 成交活跃度
    # ====================

    if factor:

        volume = factor.get(
            "volume_factor",
            0
        )


        if volume < 0.3:

            risk.append(
                "流动性不足"
            )



    # ====================
    # 5. 趋势过滤
    # ====================

    if factor:

        trend = factor.get(
            "trend",
            0
        )


        if trend == 0:

            risk.append(
                "下降趋势"
            )



    # ====================
    # 最终判断
    # ====================

    if len(risk) > 0:

        return False, risk


    return True, []