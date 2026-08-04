import os
import json
from datetime import datetime


FEEDBACK_FILE = "data/cache/runtime_feedback.json"


class RuntimeDecisionFeedback:


    def __init__(self):

        os.makedirs(
            os.path.dirname(FEEDBACK_FILE),
            exist_ok=True
        )


        if not os.path.exists(FEEDBACK_FILE):

            with open(
                FEEDBACK_FILE,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    [],
                    f
                )



    def record(
        self,
        result
    ):

        with open(
            FEEDBACK_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        result["timestamp"] = (
            datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S")
        )


        data.append(result)


        with open(
            FEEDBACK_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=2
            )


        return result



    def latest(self):

        with open(
            FEEDBACK_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        if not data:
            return None


        return data[-1]