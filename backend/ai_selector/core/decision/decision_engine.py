from .decision_record import DecisionRecord


class DecisionEngine:


    def decide(
        self,
        ranking
    ):


        score = ranking.score

        confidence = ranking.confidence

        market = ranking.market_state


        if (
            score >= 0.6
            and confidence >= 0.5
            and market != "BEAR"
        ):

            action = "BUY"


        elif score >= 0.3:

            action = "HOLD"


        else:

            action = "SKIP"



        return DecisionRecord(

            code=ranking.code,

            action=action,

            score=score,

            confidence=confidence,

            market_state=market,

            signals=ranking.signals,

            weights={}

        )