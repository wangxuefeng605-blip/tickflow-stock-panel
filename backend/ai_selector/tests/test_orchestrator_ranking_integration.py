from core.orchestrator.adapters.ranking_adapter import RankingAdapter



class MockRankingPipeline:


    def run(
        self,
        data
    ):

        return [
            "ranked"
        ]



def test_ranking_adapter():


    adapter = RankingAdapter(
        MockRankingPipeline()
    )


    result = adapter.run(
        "BULL"
    )


    assert result == [
        "ranked"
    ]