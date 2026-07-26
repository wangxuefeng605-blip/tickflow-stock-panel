from core.ranking.explain import explain
from core.ranking.types import RankingResult


def test_explain():

    result = RankingResult(

        code="603137",

        score=1.07,

        signals=[
            "strong_momentum",
            "trend_up"
        ]

    )


    output = explain(result)


    assert "20日價格動能強" in output["reasons"]

    assert "短中期趨勢向上" in output["reasons"]