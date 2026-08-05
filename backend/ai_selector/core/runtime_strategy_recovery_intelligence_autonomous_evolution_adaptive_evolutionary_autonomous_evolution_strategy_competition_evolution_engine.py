class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyCompetitionEvolutionEngine:
    """
    Evolves strategies through competition.
    """

    def __init__(self):

        self.population = {}

        self.history = []



    def add_strategy(
        self,
        name,
        score=0.5
    ):

        self.population[name] = {

            "score": score,

            "generation": 1,

            "active": True

        }


        result = {

            "strategy": name,

            "added": True

        }


        self.history.append(
            {
                "action": "add",
                "result": result
            }
        )


        return result



    def update_score(
        self,
        name,
        score
    ):

        if name not in self.population:

            return None


        self.population[name]["score"] = score


        self.history.append(
            {
                "action": "score_update",
                "strategy": name,
                "score": score
            }
        )


        return self.population[name]



    def eliminate_weak(
        self,
        threshold=0.3
    ):

        removed = []


        for name in list(self.population.keys()):

            if (
                self.population[name]["score"]
                <
                threshold
            ):

                self.population[name]["active"] = False

                removed.append(name)


        result = {

            "removed": removed

        }


        self.history.append(
            {
                "action": "eliminate",
                "result": result
            }
        )


        return result



    def evolve_best(self):

        active = {

            k:v
            for k,v
            in self.population.items()
            if v["active"]

        }


        if not active:

            return None


        best = max(
            active,
            key=lambda x:
            active[x]["score"]
        )


        self.population[best]["generation"] += 1


        result = {

            "strategy": best,

            "generation":
                self.population[best]["generation"]

        }


        self.history.append(
            {
                "action": "evolve",
                "result": result
            }
        )


        return result



    def get_population(self):

        return self.population



    def get_history(self):

        return self.history