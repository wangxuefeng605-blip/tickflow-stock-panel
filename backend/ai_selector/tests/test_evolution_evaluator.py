from core.evolution.evolution_evaluator import (
    EvolutionEvaluator
)



def test_evaluate_upgrade():

    evaluator = EvolutionEvaluator()


    result = evaluator.evaluate(
        {
            "score":80
        },
        {
            "score":90
        }
    )


    assert result["accepted"]



def test_rank_strategy():

    evaluator = EvolutionEvaluator()


    result = evaluator.rank(
        [
            {
                "score":50
            },
            {
                "score":90
            }
        ]
    )


    assert result[0]["score"] == 90