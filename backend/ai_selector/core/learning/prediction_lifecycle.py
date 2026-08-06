class PredictionLifecycle:


    def __init__(
        self,
        tracker=None
    ):

        from core.learning.outcome.outcome_tracker import OutcomeTracker

        self.tracker = (
            tracker
            or OutcomeTracker()
        )


    def record_top10(
        self,
        results,
        date
    ):

        paths = []

        for item in results:


            if item is Ellipsis:

                code = "UNKNOWN"

                score = 0


            elif isinstance(item, dict):

                code = item.get(
                    "code",
                    "UNKNOWN"
                )

                score = item.get(
                    "score",
                    0
                )


            else:

                code = getattr(
                    item,
                    "code",
                    "UNKNOWN"
                )

                score = getattr(
                    item,
                    "score",
                    0
                )


            path = (
                self.tracker
                .save_prediction_outcome(
                    code=code,
                    prediction_date=date,
                    score=score
                )
            )


            paths.append(path)


        return paths