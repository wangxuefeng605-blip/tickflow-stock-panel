from .types import RankingResult


def explain(result: RankingResult):

    reasons = []

    risks = []


    for signal in result.signals or []:

        if signal == "strong_momentum":

            reasons.append(
                "20日價格動能強"
            )


        elif signal == "trend_up":

            reasons.append(
                "短中期趨勢向上"
            )


        elif signal == "volume_breakout":

            reasons.append(
                "成交量明顯放大"
            )


    if result.score < 0.5:

        risks.append(
            "綜合評分偏低"
        )


    return {

        "reasons": reasons,

        "risks": risks

    }