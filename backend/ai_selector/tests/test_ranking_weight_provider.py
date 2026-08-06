from core.ranking.ranking_weight_provider import RankingWeightProvider


def test_ranking_weight_provider():

    provider = RankingWeightProvider()

    value = provider.get_weight(
        "momentum"
    )

    assert value is not None