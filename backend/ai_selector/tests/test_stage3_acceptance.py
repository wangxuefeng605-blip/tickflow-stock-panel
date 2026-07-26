from core.ranking import rank_stocks


def test_stage3_ranking_acceptance():

    scan_results = [
        {
            "code": "000001",
            "score": 0.9,
            "factors": {
                "momentum": 0.8,
                "trend": 1
            }
        },
        {
            "code": "000002",
            "score": 0.5,
            "factors": {
                "momentum": 0.2,
                "trend": 0
            }
        }
    ]


    ranked = rank_stocks(
        scan_results
    )


    assert len(ranked) == 2

    assert ranked[0].rank == 1

    assert ranked[0].code == "000001"

    assert hasattr(
        ranked[0],
        "signals"
    )
