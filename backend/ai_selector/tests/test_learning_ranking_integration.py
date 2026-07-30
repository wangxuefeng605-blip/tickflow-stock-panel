from core.ranking.pipeline import RankingPipeline
from core.learning.weight_provider import WeightProvider


def test_ranking_pipeline_uses_learning_weight():

    provider = WeightProvider(
        {
            "momentum":0.6
        }
    )


    pipeline = RankingPipeline(
        weight_provider=provider
    )


    result = pipeline.run(
        [
            {
                "code":"000001",
                "score":0.8,
                "factors":{
                    "momentum":1
                }
            }
        ]
    )


    assert result[0].rank == 1