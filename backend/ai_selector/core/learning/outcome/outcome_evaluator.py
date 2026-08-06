import json

from pathlib import Path


class OutcomeEvaluator:


    def __init__(
        self,
        base_dir="data/learning/outcomes"
    ):

        self.base_dir = Path(base_dir)



    def evaluate(self):

        files = list(
            self.base_dir.glob("*.json")
        )


        if not files:

            return {
                "samples":0,
                "success_rate":0,
                "avg_return":0,
                "factor_scores":{}
            }


        success_count = 0
        total_return = 0

        samples = 0


        for file in files:

            with open(
                file,
                encoding="utf-8"
            ) as f:

                data = json.load(f)


            result = data.get(
                "result",
                {}
            )


            samples += 1


            if result.get(
                "success",
                False
            ):

                success_count += 1


            total_return += result.get(
                "return_5d",
                0
            )


        return {

            "samples":
                samples,


            "success_rate":
                success_count / samples,


            "avg_return":
                total_return / samples,


            "factor_scores":
                {}

        }