import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(
    0,
    str(ROOT)
)


from core.ranking.pipeline import RankingPipeline


def test_ranking_pipeline():

    data = [

        {
            "code": "000001",
            "score": 0.5,
            "factors": {
                "momentum": 0.1,
                "trend": 1,
                "volume_factor": 1.5
            }
        },

        {
            "code": "000002",
            "score": 1.2,
            "factors": {
                "momentum": 0.02,
                "trend": 0,
                "volume_factor": 0.8
            }
        }

    ]


    result = RankingPipeline().run(
        data
    )


    assert result[0].code == "000002"

    assert result[0].rank == 1

    assert isinstance(
        result[0].signals,
        list
    )