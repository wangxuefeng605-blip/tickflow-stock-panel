class StrategyBenchmark:

    def __init__(self):

        self.results = []


    def record(
        self,
        strategy,
        performance
    ):

        self.results.append(
            {
                "strategy": strategy,
                "performance": performance
            }
        )


    def get_results(self):

        return self.results