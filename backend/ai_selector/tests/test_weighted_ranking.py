from core.ranking.scoring import calculate_rank_score



def test_weighted_rank_score():


    item={

        "score":0.5,

        "factors":{
            "momentum":0.8,
            "trend":1,
            "quality":0.7
        },

        "market_state":"BULL",

        "confidence":0.8

    }


    result = calculate_rank_score(
        item
    )


    assert result > 0.5