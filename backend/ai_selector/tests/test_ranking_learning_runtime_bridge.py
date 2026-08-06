from core.ranking import rank_stocks
from core.ranking.learning_provider import LearningPipeline


def test_ranking_learning_runtime_bridge():

    data = [

        {
            "code":"000001",
            "score":100,
            "factors":{
                "momentum":1
            }
        },

        {
            "code":"000002",
            "score":80,
            "factors":{
                "momentum":0.5
            }
        }

    ]


    pipeline = LearningPipeline()


    result = rank_stocks(
        data,
        learning_pipeline=pipeline
    )


    assert len(result)==2

    assert result[0].rank==1