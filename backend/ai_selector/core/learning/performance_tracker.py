from core.history_cache import get_history


class PerformanceTracker:


    def calculate_return(
        self,
        history,
        days
    ):

        if history is None:
            return None


        if len(history) <= days:
            return None


        start = history.iloc[-days-1]["close"]

        end = history.iloc[-1]["close"]


        return round(
            (end - start) / start,
            4
        )


    def evaluate(
        self,
        prediction
    ):

        code = prediction["code"]


        history = get_history(
            code
        )


        if history is None:

            return {
                **prediction,
                "status":"NO_DATA"
            }


        prediction["future_return_5d"] = (
            self.calculate_return(
                history,
                5
            )
        )


        prediction["future_return_10d"] = (
            self.calculate_return(
                history,
                10
            )
        )


        prediction["status"] = "DONE"


        return prediction