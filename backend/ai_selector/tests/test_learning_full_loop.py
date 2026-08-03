from core.ranking.pipeline import RankingPipeline
from core.learning.weight_provider import LearningWeightProvider


def test_learning_full_loop():

    provider = LearningWeightProvider(
        {
            "momentum": 2,
            "trend": 1
        }
    )


    pipeline = RankingPipeline(
        provider
    )


    results = [

        {
            "code": "000001",
            "score": 1,
            "factors": {
                "momentum": 1
            }
        },

        {
            "code": "000002",
            "score": 1.2,
            "factors": {
                "trend": 1
            }
        }

    ]


    ranked = pipeline.run(
        results
    )


    assert ranked[0].code == "000001"
    assert ranked[1].code == "000002"