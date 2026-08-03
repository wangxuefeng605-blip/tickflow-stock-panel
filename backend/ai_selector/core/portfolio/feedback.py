class PortfolioFeedback:

    def process(self, attribution):

        drivers = []

        for item in attribution:

            for d in item.get("drivers",[]):
                drivers.append(d)

        return {
            "feedback": True,
            "drivers": drivers
        }