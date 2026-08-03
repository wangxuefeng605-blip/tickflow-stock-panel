from typing import List, Dict


class PortfolioAttribution:

    def calculate(
        self,
        positions: List[Dict]
    ):

        results = []

        for item in positions:

            contribution = (
                item.get("return", 0)
                *
                item.get("weight", 0)
            )

            factors = item.get(
                "factors",
                {}
            )

            drivers = [
                key
                for key, value in factors.items()
                if value > 0
            ]

            results.append(
                {
                    "code": item.get("code"),
                    "contribution": contribution,
                    "drivers": drivers
                }
            )

        return results