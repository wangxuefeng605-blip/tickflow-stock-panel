class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionDynamicAssetAllocationEngine:
    """
    Dynamically adjusts portfolio allocation.
    """

    def __init__(self):

        self.allocations = {}

        self.history = []



    def set_asset(
        self,
        asset,
        weight
    ):

        self.allocations[asset] = weight


        result = {

            "asset": asset,

            "weight": weight

        }


        self.history.append(
            {
                "action": "set_asset",
                "result": result
            }
        )


        return result



    def adjust_by_market(
        self,
        market_state
    ):

        multiplier = {

            "BULL": 1.2,

            "BEAR": 0.6,

            "UNKNOWN": 1.0

        }.get(
            market_state,
            1.0
        )


        adjusted = {}


        for asset, weight in self.allocations.items():

            adjusted[asset] = round(
                min(
                    weight * multiplier,
                    1.0
                ),
                3
            )


        self.history.append(
            {
                "action": "adjust",
                "market": market_state,
                "result": adjusted
            }
        )


        return adjusted



    def normalize(self):

        total = sum(
            self.allocations.values()
        )


        if total == 0:

            return {}


        result = {

            k: round(v / total, 3)

            for k, v in self.allocations.items()

        }


        self.history.append(
            {
                "action": "normalize",
                "result": result
            }
        )


        return result



    def get_history(self):

        return self.history