import json

from pathlib import Path

from core.learning.outcome.outcome_evaluator import OutcomeEvaluator



def test_outcome_evaluator(tmp_path):


    data = {

        "code":"000001",

        "result":{

            "success":True,

            "return_5d":0.08

        }

    }


    file = (
        tmp_path /
        "test.json"
    )


    file.write_text(
        json.dumps(data),
        encoding="utf-8"
    )


    evaluator = OutcomeEvaluator(
        tmp_path
    )


    report = evaluator.evaluate()


    assert report["samples"] == 1

    assert report["success_rate"] == 1

    assert report["avg_return"] == 0.08