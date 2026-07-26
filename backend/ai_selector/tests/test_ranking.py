import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(
    0,
    str(ROOT)
)


from core.ranking.ranker import Ranker
from core.ranking.ranker import Ranker


def test_rank_order():


    data = [

        {
            "code":"000001",
            "score":0.5
        },

        {
            "code":"000002",
            "score":1.2
        }

    ]


    result = Ranker().rank(data)


    assert result[0].code == "000002"

    assert result[0].rank == 1

    assert result[1].rank == 2