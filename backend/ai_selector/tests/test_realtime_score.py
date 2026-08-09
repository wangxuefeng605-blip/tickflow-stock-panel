def test_realtime_score():

    engine = RealtimeScoreEngine()

    result = engine.calculate(
        {
          "momentum":0.8,
          "trend":0.7
        }
    )


    assert result["score"] > 0