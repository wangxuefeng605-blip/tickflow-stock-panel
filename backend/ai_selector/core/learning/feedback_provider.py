"""
Feedback Data Provider

Load historical recommendation feedback.
"""

import json
from pathlib import Path

from core.performance_tracker import (
    run_tracker
)


class FeedbackProvider:


    def load(self):

        """
        Load feedback records.
        """

        try:

            result = run_tracker()

        except Exception:

            return []


        # tracker returns file path

        if isinstance(result, Path):

            path = result

        else:

            path = Path(result)


        if not path.exists():

            return []


        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                records = json.load(f)

        except Exception:

            return []


        if not isinstance(
            records,
            list
        ):

            return []


        feedbacks = []


        for item in records:

            feedbacks.append(
                {
                    "code": item.get(
                        "code"
                    ),

                    "score": item.get(
                        "score",
                        0
                    ),

                    "return": item.get(
                        "return",
                        0
                    )
                }
            )


        return feedbacks