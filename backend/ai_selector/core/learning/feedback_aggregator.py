class LearningFeedbackAggregator:


    def __init__(self):

        self.feedbacks = []


    def collect(
        self,
        feedback
    ):

        self.feedbacks.append(
            feedback
        )


    def aggregate(self):


        result = {


            "ranking_adjustment": {}

        }


        for feedback in self.feedbacks:


            ranking = feedback.signal.get(
                "ranking",
                {}
            )


            for factor, value in ranking.items():


                result[
                    "ranking_adjustment"
                ][factor] = (
                    result[
                        "ranking_adjustment"
                    ].get(
                        factor,
                        0
                    )
                    +
                    value
                )


        return result