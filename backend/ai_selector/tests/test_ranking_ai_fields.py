from core.ranking.ranker import Ranker


def test_ranker_keep_ai_fields():

    results=[

        {
            "code":"000001",

            "score":0.8,

            "signals":[
                "Strong momentum"
            ],

            "confidence":0.9,

            "explanation":{
                "market_state":"BULL"
            }

        }

    ]


    ranked = Ranker().rank(results)


    item = ranked[0]


    assert item.signals == [
        "Strong momentum"
    ]

    assert item.confidence == 0.9

    assert (
        item.explanation["market_state"]
        ==
        "BULL"
    )