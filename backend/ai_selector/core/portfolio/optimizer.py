class PortfolioOptimizer:


    def optimize(
        self,
        portfolio,
        risk,
        market_state
    ):

        allocation = {}

        changes = []


        positions = portfolio.get(
            "positions",
            []
        )


        for position in positions:

            code = position.get(
                "code"
            )

            weight = position.get(
                "weight",
                0
            )

            score = position.get(
                "score",
                0
            )


            target = weight


            if (
                market_state == "BULL"
                and score > 0.8
            ):
                target = min(
                    weight + 0.15,
                    1.0
                )


            allocation[code] = target


            if target != weight:

                changes.append(
                    {
                        "code": code,
                        "from": weight,
                        "to": target,
                        "reason": "momentum strength"
                    }
                )


        confidence = 0.8


        return {

            "allocation": allocation,

            "changes": changes,

            "confidence": confidence

        }