class RiskEngine:


    def __init__(
        self,
        max_position_ratio=0.3
    ):

        self.max_position_ratio = max_position_ratio



    def evaluate(
        self,
        portfolio
    ):

        cash = portfolio.get(
            "cash",
            0
        )


        positions = portfolio.get(
            "positions",
            {}
        )


        total_value = cash


        exposure = 0


        for pos in positions.values():

            value = (
                pos["qty"]
                *
                pos["price"]
            )

            total_value += value
            exposure += value



        ratio = 0


        if total_value > 0:

            ratio = exposure / total_value



        allowed = (
            ratio <= self.max_position_ratio
        )


        return {

            "risk":
                "LOW"
                if allowed
                else "HIGH",


            "exposure":
                ratio,


            "allowed":
                allowed

        }
    def check(
        self,
        order
    ):

        result = self.evaluate(order)

        return result