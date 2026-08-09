from core.ranking.realtime_ranking import RealtimeRanking


def test_realtime_ranking():

    engine = RealtimeRanking()

    result = engine.rank(
        [
            {
                "code":"000001",
                "score":3.5
            },
            {
                "code":"000002",
                "score":5.2
            }
        ]
    )


    assert result[0]["code"]=="000002"
    assert result[0]["rank"]==1