class StrategyEvolutionEngine:


    def evolve(self, evaluation):

        level = evaluation.get("level")

        if level == "GOOD":

            return {
                "action":"KEEP",
                "strategy":evaluation.get("strategy")
            }


        if level == "NORMAL":

            return {
                "action":"MODIFY",
                "strategy":evaluation.get("strategy")
            }


        return {
            "action":"REMOVE",
            "strategy":evaluation.get("strategy")
        }