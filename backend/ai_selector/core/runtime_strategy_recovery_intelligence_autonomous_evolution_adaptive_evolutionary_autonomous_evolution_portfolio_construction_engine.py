class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioConstructionEngine:
    """
    Builds autonomous investment portfolios.
    """

    def __init__(self):

        self.assets = []

        self.history = []



    def add_strategy(
        self,
        name,
        score
    ):

        strategy = {

            "name": name,

            "score": score

        }


        self.assets.append(
            strategy
        )


        self.history.append(
            {
                "action": "add",
                "strategy": strategy
            }
        )


        return strategy



    def allocate_weights(self):

        if not self.assets:

            return None


        total_score = sum(
            x["score"]
            for x in self.assets
        )


        portfolio = []


        for item in self.assets:

            weight = round(
                item["score"]
                /
                total_score,
                3
            )


            portfolio.append(
                {
                    "name": item["name"],

                    "weight": weight
                }
            )


        self.history.append(
            {
                "action": "allocate",
                "portfolio": portfolio
            }
        )


        return portfolio



    def build_portfolio(self):

        return {

            "portfolio":
                self.allocate_weights(),

            "status":
                "constructed"

        }



    def get_history(self):

        return self.history