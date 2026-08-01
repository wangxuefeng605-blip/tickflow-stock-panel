from core.learning import RankingLearningHook


def test_ranking_learning_hook():

    hook = RankingLearningHook()


    result = [
        {
            "code": "000001",
            "rank": 1,
            "score": 0.95
        }
    ]


    output = hook.after_rank(result)


    assert output == result