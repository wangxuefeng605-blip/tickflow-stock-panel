from .types import RankingResult


def explain(item: RankingResult):


    reasons = []

    risks = []


    factors = item.factors or {}


    momentum = factors.get(
        "momentum",
        0
    )


    volume_factor = factors.get(
        "volume_factor",
        0
    )


    volatility = factors.get(
        "volatility",
        0
    )


    signals = item.signals or []


    # 动能解释
    if (
        "strong_momentum" in signals
        or momentum > 0.05
    ):

        reasons.append(
            "20日價格動能強"
        )


    elif momentum > 0:

        reasons.append(
            "價格動能偏正"
        )


    # 趋势解释
    if "trend_up" in signals:

        reasons.append(
            "短中期趨勢向上"
        )


    # 成交量
    if volume_factor > 1.2:

        reasons.append(
            "成交量放大"
        )


    # 风险
    if volatility > 0.05:

        risks.append(
            "波動率偏高"
        )


    if not reasons:

        reasons.append(
            "缺少明顯正向訊號"
        )


    return {

        "reasons": reasons,

        "risks": risks,

        "summary": "；".join(
            reasons
        )

    }