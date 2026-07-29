class StrategyOptimizer:


    def optimize(
        self,
        result
    ):


        if result.win_rate < 0.5:

            return {
                "risk":"reduce"
            }


        return {
            "risk":"keep"
        }