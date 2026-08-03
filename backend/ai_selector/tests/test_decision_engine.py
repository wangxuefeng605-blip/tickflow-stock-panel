from core.decision import DecisionEngine
from core.ranking.types import RankingResult


def test_decision_engine():


    ranking = RankingResult(

        code="603580",

        score=0.72,

        confidence=0.85,

        market_state="BULL",

        signals=[
            "Strong momentum"
        ]

    )


    engine = DecisionEngine()


    decision = engine.decide(
        ranking
    )


    assert decision.action=="BUY"

    assert decision.code=="603580"