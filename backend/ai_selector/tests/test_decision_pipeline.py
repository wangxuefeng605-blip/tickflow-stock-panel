from core.decision import DecisionPipeline



def test_decision_pipeline():


    pipeline = DecisionPipeline()


    ranking = [

        {
            "code":"000001",
            "score":0.8,
            "market_state":"BULL",
            "confidence":0.8
        }

    ]


    result = pipeline.run(
        ranking
    )


    assert len(result)==1