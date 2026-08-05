class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPortfolioRiskManagementEngine:
    """
    Manages autonomous portfolio risk.
    """

    def __init__(self):

        self.positions = {}

        self.history = []



    def add_position(
        self,
        asset,
        weight
    ):

        self.positions[asset] = {

            "weight": weight,

            "risk": 0

        }


        result = {

            "asset": asset,

            "weight": weight

        }


        self.history.append(
            {
                "action": "add_position",
                "result": result
            }
        )


        return result



    def calculate_risk(
        self,
        asset,
        volatility
    ):

        if asset not in self.positions:

            return None


        risk = round(
            self.positions[asset]["weight"]
            *
            volatility,
            3
        )


        self.positions[asset]["risk"] = risk


        result = {

            "asset": asset,

            "risk": risk

        }


        self.history.append(
            {
                "action": "risk_calculation",
                "result": result
            }
        )


        return result



    def check_exposure(
        self,
        limit=0.3
    ):

        result = {}


        for asset, data in self.positions.items():

            result[asset] = (
                data["weight"] <= limit
            )


        self.history.append(
            {
                "action": "exposure_check",
                "result": result
            }
        )


        return result



    def get_history(self):

        return self.history