class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionParetoDecisionEngine:
    """
    Selects optimal strategies from Pareto candidates.
    """

    def __init__(self):

        self.candidates = []

        self.history = []



    def add_candidate(
        self,
        name,
        performance,
        risk,
        stability
    ):

        candidate = {

            "name": name,

            "performance": performance,

            "risk": risk,

            "stability": stability

        }


        self.candidates.append(
            candidate
        )


        self.history.append(
            {
                "action": "add",
                "candidate": candidate
            }
        )


        return candidate



    def calculate_score(
        self,
        candidate
    ):

        return round(
            candidate["performance"] * 0.5
            +
            candidate["stability"] * 0.4
            -
            candidate["risk"] * 0.1,
            3
        )



    def pareto_frontier(self):

        frontier = []


        for candidate in self.candidates:

            dominated = False


            for other in self.candidates:

                if other == candidate:

                    continue


                if (
                    other["performance"] >= candidate["performance"]
                    and
                    other["risk"] <= candidate["risk"]
                    and
                    other["stability"] >= candidate["stability"]
                ):

                    dominated = True

                    break


            if not dominated:

                frontier.append(candidate)


        self.history.append(
            {
                "action": "pareto",
                "result": frontier
            }
        )


        return frontier



    def select_best(self):

        frontier = self.pareto_frontier()


        if not frontier:

            return None


        return max(
            frontier,
            key=lambda x:
                self.calculate_score(x)
        )



    def get_history(self):

        return self.history