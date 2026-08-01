class IntelligenceScorer:


    def calculate(
        self,
        score,
        market_state,
        confidence
    ):

        market_factor = {

            "BULL": 1.10,

            "SIDEWAY": 1.00,

            "BEAR": 0.85

        }.get(
            market_state,
            1.0
        )


        confidence_factor = (
            0.95
            +
            confidence * 0.05
        )


        final_score = (
            score
            *
            market_factor
            *
            confidence_factor
        )


        return {

            "alpha_score": score,

            "market_factor": market_factor,

            "confidence_factor": confidence_factor,

            "intelligence_score": final_score

        }